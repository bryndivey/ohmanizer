from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.html import format_html

from electronics import models
import electronics.labeler

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

    def create_wishlist_items(self, request, queryset):
        for obj in queryset:
            models.WishItem(component=obj).save()

    def parameters(self, obj):
        pout = []
        for param in obj.componentparametervalue_set.all():
            pout.append(format_html(u'<li>{0}: {1}</li>', param.parameter.name, param.value))
        return '<ul>%s</ul>' % (''.join(pout), )
    parameters.allow_tags = True

    actions = [create_wishlist_items]
    list_filter = ('type', )
    list_display = ('name', 'type', 'parameters')
    search_fields = ('name', 'type__name')
            

admin.site.register(models.Component, ComponentAdmin)

admin.site.register(models.ComponentCategory)
admin.site.register(models.Location)

class StockAdmin(admin.ModelAdmin):
    def component_name(self, obj):
        return obj.component.name
        
    def component_type(self, obj):
        return obj.component.type
        
    list_display = ('component_name', 'component_type', 'number', 'location', 'subslot',
                    'tag')
    list_filter = ('component__type',)
    search_fields = ('=tag', 'component__type__name',
                     'component__name', 'location__designation')

admin.site.register(models.Stock, StockAdmin)
admin.site.register(models.WishItem)

class LabelAdmin(admin.ModelAdmin):
    def print_labels(self, request, queryset):
        opts = self.model._meta
        app_label = opts.app_label

        if request.POST.get('post'):
            used = [(map(int, v.split(','))) for v in request.POST.getlist('used')]
            electronics.labeler.write_labels(queryset, used)
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
