import datetime
import random
import string

from django.db import models

class Parameter(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return '%s (%s)' % (self.name, self.description)

class ComponentCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return unicode(self.name)
    
        
class ComponentType(models.Model):
    name = models.CharField(max_length=40)
    parameters = models.ManyToManyField(Parameter, blank=True)
    notes = models.TextField(blank=True, default='')
    category = models.ForeignKey(ComponentCategory, null=True)

    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=40)
    type = models.ForeignKey(ComponentType)
    datasheet = models.URLField(blank=True)
    notes = models.TextField(blank=True, default='')
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.type)

class ComponentParameterValue(models.Model):
    component = models.ForeignKey(Component)
    parameter = models.ForeignKey(Parameter)
    value = models.CharField(max_length=10)

class Location(models.Model):
    designation = models.CharField(max_length=40)
    description = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ['designation']
    
    def __unicode__(self):
        if self.description:
            return "%s: %s" % (self.designation, self.description)
        return self.designation

def random_tag():
    return ''.join([random.choice(string.letters + string.digits) for _ in xrange(5)])
        
class Stock(models.Model):
    component = models.ForeignKey(Component)
    number = models.IntegerField()
    location = models.ForeignKey(Location)
    subslot = models.CharField(max_length=40, blank=True)
    tag = models.CharField(max_length=5, default=random_tag)
    last_check = models.DateField(default=datetime.datetime.utcnow)
    notes = models.TextField(blank=True, default='')

    def __unicode__(self):
        return "%s: %i %s in %s" % (self.tag, self.number, self.component, self.location)

class Label(models.Model):
    stock = models.ForeignKey(Stock)

class WishItem(models.Model):
    component = models.ForeignKey(Component)
    notes = models.TextField(blank=True, default='')

    def __unicode__(self):
        return unicode(self.component)

class Order(models.Model):
    reference = models.CharField(max_length=500)
    shipping_num = models.CharField(max_length=20, blank=True)
    supplier = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True, default='')
    date = models.DateField(default=datetime.datetime.now)
    
class OrderComponent(models.Model):
    order = models.ForeignKey(Order)
    component = models.ForeignKey(Component)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(blank=True) # cents
    
    
