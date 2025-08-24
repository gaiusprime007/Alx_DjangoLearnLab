from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )
    add_fieldsets = (
        (None, {
            
            'fields': ('date_of_birth', 'profile_photo')}
        ),
        
    )
    
    search_fields = ('username', 'email')
    ordering = ('username',)
    
admin.site.register(CustomUser, CustomUserAdmin)
    
    # The models are already registered using the @admin.register decorator above.ad
   