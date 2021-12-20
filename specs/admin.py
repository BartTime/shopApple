from django.contrib import admin

from .models import *


class CategoryFeatureAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'
    search_fields = ['feature_name', 'feature_filter_name', 'unit']
    list_display = ['category', 'feature_name', 'feature_filter_name', 'unit']
    list_filter = ['category', 'feature_name', 'feature_filter_name', 'unit']


class FeatureValidatorAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'
    search_fields = ['valid_feature_value']

class ProductFeaturesAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'
    search_fields = ['value']


admin.site.register(ProductFeatures)
admin.site.register(FeatureValidator, FeatureValidatorAdmin)
admin.site.register(CategoryFeature, CategoryFeatureAdmin)
