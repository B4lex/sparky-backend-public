from django.contrib import admin

from sparky.activities.models import Activity, ActivityCategory, ActivityEvent, OngoingActivity


class OngoingActivityInline(admin.StackedInline):
    model = OngoingActivity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "weight", "duration")
    search_fields = ("title", "category__name", "description")
    inlines = (OngoingActivityInline,)


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(ActivityEvent)
class ActivityEventAdmin(admin.ModelAdmin):
    list_display = ("ongoing_activity", "scheduled_on", "is_completed")
    search_fields = ("ongoing_activity__activity__title", "ongoing_activity__activity__description")
