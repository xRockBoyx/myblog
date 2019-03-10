from django.contrib import admin
from .models import Post,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text','created_date') #選擇在列表時要顯示哪些欄位
    #fields  = ('title', 'text','published_date') #fields 新增或修改物件 會出現哪些欄位
    search_fields = ('title',)
    inlines = [TagInline] 
    fieldsets = (
        ['Main',{
            'fields':('title','text'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('created_date',),
        }]
 
    )
 
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)