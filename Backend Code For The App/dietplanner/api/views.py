from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import UserProfile, Meal, MealPlan, Progress
from .serializers import UserProfileSerializer, MealSerializer, MealPlanSerializer, ProgressSerializer
from rest_framework import status
from .utils import get_meals_from_spoonacular

# UserProfile API View
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=True, methods=['get'])
    def get_meal_plans(self, request, pk=None):
        user_profile = self.get_object()
        meal_plans = MealPlan.objects.filter(user_profile=user_profile)
        serializer = MealPlanSerializer(meal_plans, many=True)
        return Response(serializer.data)


# Meal API View
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


# MealPlan API View
class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

    @action(detail=True, methods=['get'])
    def generate_meal_plan(self, request, pk=None):
        # Get the user profile
        user_profile = self.get_object()

        # Example query generation based on dietary preferences
        dietary_restrictions = user_profile.dietary_preferences
        meals = get_meals_from_spoonacular(query="healthy", dietary_restrictions=dietary_restrictions)

        # Save the meals to MealPlan
        meal_plan = MealPlan.objects.create(user_profile=user_profile, date='2024-12-15')  # For example purposes
        for meal_data in meals:
            meal = Meal.objects.create(
                name=meal_data['title'],
                ingredients=meal_data['ingredients'],
                calories=meal_data['nutrition']['nutrients'][0]['amount'],
                protein=meal_data['nutrition']['nutrients'][1]['amount'],
                fat=meal_data['nutrition']['nutrients'][2]['amount'],
                carbs=meal_data['nutrition']['nutrients'][3]['amount']
            )
            meal_plan.meals.add(meal)
        
        meal_plan.save()
        
        return Response({'status': 'Meal plan generated successfully'})

    @action(detail=True, methods=['get'])
    def get_progress(self, request, pk=None):
        meal_plan = self.get_object()
        progress = Progress.objects.filter(user_profile=meal_plan.user_profile, date=meal_plan.date)
        serializer = ProgressSerializer(progress, many=True)
        return Response(serializer.data)


# Progress API View
class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
