from django.shortcuts import get_object_or_404, render_to_response
from snakelog.models import Category

#def entries_index(request):
#    return render_to_response('snakelog/entry_index.html',
#                     {'entry_list': Entry.objects.all() })

# Replaced by a generic view
#def entry_detail(request, year, month, day, slug):
#    import datetime, time
#    date_stamp = time.strptime(year+month+day, "%Y%b%d")
#    pub_date = datetime.date(*date_stamp[:3])
#    entry = get_object_or_404(Entry, pub_date__year=pub_date.year,
#                                        pub_date__month=pub_date.month,
#                                        pub_date__day=pub_date.day,
#                                        slug=slug)
#    return render_to_response('snakelog/entry_detail.html',
#                              {'entry': entry})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('snakelog/category_detail.html',
                              # Uses live_entry_set in the category model
                              {'object_list': category.live_entry_set(),
                               'category': category})

## This wraps a generic view in a function which does a little bit of more filtering
## the end result is like the category_detail above but with a generic view.
#from django.views.generic.list_detail import object_list
#
#def category_detail(request, slug):
#    category = get_object_or_404(Category, slug=slug)
#    return object_list(request, queryset=category.entry_set.all(),
#                       extra_context={'category': category})