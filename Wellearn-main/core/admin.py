from django.contrib import admin
# from core.translations import BlogAdmin
from modeltranslation.admin import TranslationAdmin
# Register your models here.
from core.models import *

from core.models import (
Blog, Category, Settings, Contact, 
About, Subscriber, Product, ProductCategory, 
Basket, ShopCategory, Shop,
)

admin.site.register(Subscriber)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Basket)

admin.site.register(Shop)
admin.site.register(ShopCategory)

admin.site.register(Time)
admin.site.register(Coursecategory)
admin.site.register(Level)
admin.site.register(Price)
admin.site.register(Course)
admin.site.register(Pricecat)
admin.site.register(FAQ)

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ( 'title', 'description', 'image', 'created_at' )


class CategoryAdmin(TranslationAdmin):
    list_display =('title',)

admin.site.register(Category, CategoryAdmin)


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ( 'title', 'category', 'is_published', 'created_at', 'image' )
    list_filter = ('category', 'is_published')
    search_fields = ('title', )
    list_editable = ('is_published',)
    list_per_page = 5
    # readonly_fields =( 'slug,', 'created_at', 'updated_at',)

    fieldsets = ( ( 'Blog', {'fields': ('title','description', 'image', 'is_published', 'category')}), )

@admin.register(Contact)
class BlogAdmin(admin.ModelAdmin):
    list_display = ( 'Fname', 'email', 'phone', 'created_at' )

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):


    def has_delete_permission(self, request, obj=None):
        if request.user.username == 'admin':
            return True
        else:
            return False
    
    def has_add_permission(self, request):
        if request.user.username == 'admin':
            return True
        else:
            return False