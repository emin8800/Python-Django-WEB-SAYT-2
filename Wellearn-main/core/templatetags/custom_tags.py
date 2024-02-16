
from core.models import Blog

from django import template    

register = template.Library()

@register.simple_tag
def get_blog(order,offset=None, limit=None):
    if order == 0:
        return Blog.objects.filter(is_published=True).order_by('-updated_at')[offset : limit]
    return Blog.objects.filter(is_published=True).order_by('-created_at')[offset : limit]

