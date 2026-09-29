from rest_framework import serializers
from .models import UserProfile, Meal, MealPlan, Progress
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'age', 'weight', 'height', 'activity_level', 'dietary_preferences', 'health_goals']


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'name', 'ingredients', 'calories', 'protein', 'fat', 'carbs']


class MealPlanSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = MealPlan
        fields = ['id', 'user_profile', 'date', 'meals']


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'user_profile', 'date', 'weight', 'calories_consumed', 'meal_adherence']
