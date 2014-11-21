from django.contrib import admin
from django.template.response import TemplateResponse
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
    list_display = ('name', 'type')

admin.site.register(models.Component, ComponentAdmin)

admin.site.register(models.ComponentCategory)
admin.site.register(models.Location)

class StockAdmin(admin.ModelAdmin):
    def component_name(self, obj):
        return obj.component.name
        
    def component_type(self, obj):
        return obj.component.type
        
    list_display = ('component_name', 'component_type', 'number', 'location')
    list_filter = ('component__type',)

admin.site.register(models.Stock, StockAdmin)
admin.site.register(models.WishItem)

class LabelAdmin(admin.ModelAdmin):
    def print_labels(self, request, queryset):
        opts = self.model._meta
        app_label = opts.app_label

        # The user has already confirmed the deletion.
        # Do the deletion and return a None to display the change list view again.
        if request.POST.get('post'):
            n = queryset.count()
            for label in queryset:
                print label
            print request.POST.getlist('used')
            used = [(map(int, v.split(','))) for v in request.POST.getlist('used')]
            
            import electronics.labeler
            electronics.labeler.write_labels(queryset, used)
            print used
            print 'PRINTING!'
            return

        if len(queryset) == 1:
            objects_name = opts.verbose_name
        else:
            objects_name = opts.verbose_name_plural

        context = {
            "title": "Print labels",
            "objects_name": objects_name,
            'queryset': queryset,
            "opts": opts,
            'xrange': range(1, 6),
            'yrange': range(1, 14),
        }

        # Display the confirmation page
        return TemplateResponse(request, "admin/print_labels.html",
                                context, current_app=self.admin_site.name)


    actions = [print_labels]
        
admin.site.register(models.Label, LabelAdmin)

class OrderComponentInline(admin.StackedInline):
    model = models.OrderComponent
    extra = 3

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderComponentInline]

admin.site.register(models.Order, OrderAdmin)

# Register your models here.
