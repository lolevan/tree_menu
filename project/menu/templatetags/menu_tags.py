from django import template
from django.urls import resolve, Resolver404

from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.with_items().get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu': None}

    try:
        current_url = resolve(context['request'].path_info).url_name
    except Resolver404:
        current_url = None

    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                tree.append({
                    'item': item,
                    'children': build_tree(items, item)
                })
        return tree

    items = menu.items.all()
    menu_tree = build_tree(items)

    return {
        'menu': menu,
        'menu_tree': menu_tree,
        'current_url': current_url
    }
