from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.html import format_html

from electronics import models
from electronics import actions

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

    add_form_template = 'admin/component_change_form.html'
    change_form_template = 'admin/component_change_form.html'
    actions = [create_wishlist_items]
    list_filter = ('type', )
    list_display = ('name', 'type', 'parameters')
    search_fields = ('name', 'type__name')

    def response_add(self, request, obj, post_url_continue=None):
        if '_addstock' in request.POST:
            return HttpResponseRedirect('%s?component=%s' % (
                reverse('admin:electronics_stock_add'),
                obj.id))
        return super(ComponentAdmin, self).response_add(request, obj, post_url_continue)
    
    def response_change(self, request, obj, post_url_continue=None):
        if '_addstock' in request.POST:
            return HttpResponseRedirect('%s?component=%s' % (
                reverse('admin:electronics_stock_add'),
                obj.id))
        return super(ComponentAdmin, self).response_add(request, obj, post_url_continue)
    

admin.site.register(models.Component, ComponentAdmin)

admin.site.register(models.ComponentCategory)

class LocationAdmin(admin.ModelAdmin):
    def num_components(self, obj):
        return obj.stock_set.count()
        
    list_display = ('designation', 'description', 'num_components')
    actions = [actions.print_labels]


    
admin.site.register(models.Location, LocationAdmin)

class StockAdmin(admin.ModelAdmin):
    def component_name(self, obj):
        return obj.component.name
        
    def component_type(self, obj):
        return obj.component.type
        
    list_display = ('component_name', 'component_type', 'number', 'location', 'subslot',
                    'tag')
    list_filter = ('component__type', 'location')
    search_fields = ('=tag', 'component__type__name',
                     'component__name', 'location__designation')

    def create_labels(self, request, queryset):
        for stock in queryset:
            label = models.Label(stock=stock)
            label.save()

    actions = [create_labels]

admin.site.register(models.Stock, StockAdmin)
admin.site.register(models.WishItem)

class LabelAdmin(admin.ModelAdmin):
    actions = [actions.print_labels]
        
admin.site.register(models.Label, LabelAdmin)

class OrderComponentInline(admin.StackedInline):
    model = models.OrderComponent
    extra = 3

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderComponentInline]

admin.site.register(models.Order, OrderAdmin)

# Register your models here.
