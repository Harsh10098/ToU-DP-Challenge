from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, MealViewSet, MealPlanViewSet, ProgressViewSet

router = DefaultRouter()
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'meals', MealViewSet)
router.register(r'meal_plans', MealPlanViewSet)
router.register(r'progress', ProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
