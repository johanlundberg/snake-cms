from django import template
from django.db.models import get_model

from snakelog.models import Entry

def do_latest_content(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise template.TemplateSyntaxError("'get_latest_content' \
            tag takes exactly four arguments")
    model_args = bits[1].split('.')
    if len(model_args) != 2:
        raise template.TemplateSyntaxError("First argument to 'get_latest_content' \
            must be an 'application name'.model name' string")
    model = get_model(*model_args)
    if model is None:
        raise template.TemplateSyntaxError("'get_latest_content' tag got an \
            invalid model: %s" % bits[1])
    return LatestContentNode(model, bits[2], bits[4])

class LatestContentNode(template.Node):
    def __init__(self, model, num, varname):
        self.model = model
        self.num = int(num)
        self.varname = varname

    def render(self, context):
        manager = self.model._default_manager
        if self.model.__name__ == 'Entry':    # Work around for the live manager
            manager = self.model.live         # effing up the admin interface if default
        context[self.varname] = manager.all()[:self.num]
        return ''

register = template.Library()
register.tag('get_latest_content', do_latest_content)

# Not very flexible but works
#===============================================================================
# def do_latest_entries(parser, token):
#    return LatestEntriesNode()
#
# class LatestEntriesNode(template.Node):
#    def render(self, context):
#        context['latest_entries'] = Entry.live.all()[:3]
#        return ''
#
# register = template.Library()
# register.tag('get_latest_entries', do_latest_entries)
#===============================================================================