from django.contrib import admin
from .models import FitnessActivity, UserProfile, DietaryLog, FitnessGoal, WeightEntry

@admin.register(FitnessActivity)
class FitnessActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration', 'intensity', 'calories_burned', 'date_time')
    list_filter = ('activity_type', 'date_time')
    search_fields = ('user__username', 'activity_type')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'height', 'weight', 'fitness_level')
    search_fields = ('user__username',)

@admin.register(DietaryLog)
class DietaryLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_item', 'calories', 'carbs', 'proteins', 'fats', 'quantity', 'date_time')
    list_filter = ('date_time',)
    search_fields = ('user__username', 'food_item')

@admin.register(FitnessGoal)
class FitnessGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal_type', 'target_value', 'start_date', 'end_date', 'current_progress')
    list_filter = ('goal_type', 'start_date', 'end_date')
    search_fields = ('user__username', 'goal_type')

@admin.register(WeightEntry)
class WeightEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'date')
    list_filter = ('date',)
    search_fields = ('user__username',)

