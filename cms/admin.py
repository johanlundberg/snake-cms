# # setup flatpages to use tiny_mce
# from django.contrib import admin
# from django import forms
# from tinymce.widgets import TinyMCE
# from django.contrib.flatpages.models import FlatPage
# from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

# class FlatPageForm(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE())
    
    # class Meta:
        # model = FlatPage

# class FlatPageAdmin(FlatPageAdminOld):
    # form = FlatPageForm

# # We have to unregister it, and then reregister
# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdmin)

# from django.contrib import admin
# from django import forms
# from tinymce.widgets import TinyMCE

# class TinyMCEAdmin(admin.ModelAdmin):
    # tinymce_fields = list('content')
    
    # def formfield_for_dbfield(self, db_field, **kwargs):
          # if db_field.name in self.tinymce_fields:
              # return db_field.formfield(widget=TinyMCE())
          # return super(TinyMCEAdmin, self).formfield_for_dbfield(db_field, **kwargs)

from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = ['/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', '/media/admin/tinymce_setup/tinymce_setup_en.js',]

# We have to unregister it, and then reregister
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

