from django import template
from splunkdj.templatetags.tagutils import component_context
register = template.Library()
@register.inclusion_tag('splunkdj:components/component.html', takes_context=True)
def heatwave(context, id, *args, **kwargs):       # The template tag
    return component_context(
        context,
        "heatwave",                           # The custom view's CSS class name
        id,
        "view",
        "testapp/heatwave",             # Path to the JavaScript class/file for the view
        kwargs
    )