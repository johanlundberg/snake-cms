from django.shortcuts import get_object_or_404, render_to_response
from snakelog.models import Category

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('snakelog/category_detail.html',
                              # Uses live_entry_set in the category model
                              {'object_list': category.live_entry_set(),
                               'category': category})

