from django.contrib import admin
from electronics import models

admin.site.register(models.Parameter)

class ParameterInline(admin.StackedInline):
    model = models.Parameter
    extra = 3

class ComponentTypeAdmin(admin.ModelAdmin):
    inlines = [ParameterInline]
    
#admin.site.register(models.ComponentType, ComponentTypeAdmin)
admin.site.register(models.ComponentType)

class ComponentParameterValueInline(admin.StackedInline):
    model = models.ComponentParameterValue
    extra = 3

class ComponentAdmin(admin.ModelAdmin):
    inlines = [ComponentParameterValueInline]

admin.site.register(models.Component, ComponentAdmin)

admin.site.register(models.ComponentCategory)
admin.site.register(models.Location)
admin.site.register(models.Stock)
admin.site.register(models.WishItem)
admin.site.register(models.Label)

class OrderComponentInline(admin.StackedInline):
    model = models.OrderComponent
    extra = 3

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderComponentInline]

admin.site.register(models.Order, OrderAdmin)

# Register your models here.
