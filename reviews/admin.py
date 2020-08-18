from django.contrib import admin
from .models import Review

# Register your models here.
# admin.site.register(Post)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'view_count',
        'created_at',

    )
    search_fields=(
        'title',

    )