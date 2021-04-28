from django import template

from ..models import Tag

register = template.Library()

@register.inclusion_tag("blog/tag_names.html")
def tag_names():
    tags = Tag.objects.all()
    return {'names': tags}