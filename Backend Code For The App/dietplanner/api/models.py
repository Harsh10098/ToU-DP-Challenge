from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    activity_level = models.CharField(max_length=100)
    dietary_preferences = models.TextField()
    health_goals = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username} Profile'


class Meal(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    calories = models.IntegerField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()

    def __str__(self):
        return self.name


class MealPlan(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='meal_plans', on_delete=models.CASCADE)
    date = models.DateField()
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return f'Meal Plan for {self.user_profile.user.username} on {self.date}'


class Progress(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='progress', on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    calories_consumed = models.IntegerField()
    meal_adherence = models.FloatField()  # Percentage of meals followed from the plan

    def __str__(self):
        return f'Progress for {self.user_profile.user.username} on {self.date}'
