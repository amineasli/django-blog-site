from django import template

from ..models import Tag

register = template.Library()

@register.inclusion_tag("blog/tag_list.html")
def tag_list():
    tags = Tag.objects.all()
    return {'tags': tags}