from django.contrib import admin

from .models import Component, Drink, Ingredient, Step


class ComponentInline(admin.TabularInline):
    model = Component


class StepInline(admin.StackedInline):
    model = Step


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    inlines = [ComponentInline, StepInline]


admin.site.register(Component)
admin.site.register(Ingredient)
admin.site.register(Step)
