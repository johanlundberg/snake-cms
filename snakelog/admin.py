from django.contrib import admin
from snakelog.models import Category, Entry, Link

#class SearchKeywordInline(admin.TabularInline):
#    model = SearchKeyword
#
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class LinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# We have to unregister it if it registered
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Link, LinkAdmin)