from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug','status','created_on')
    list_filter=("status",)
    search_fields = ['title', 'content']
    summernote_fields=('content',)
    prepopulated_fields={'slug':('title',)}

# Register your models here.
admin.site.register(Post,PostAdmin)