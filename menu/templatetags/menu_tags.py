from django import template
from django.template import Template
from django.http.response import Http404

from menu.models import MenuItem
from menu.utils.tree import Tree, tree_string_visible_from_root
from menu.utils.functors import HTMLBuilder


register = template.Library()


def get_target_node(nodes_dict, request):
    for value in nodes_dict.values():
        if value.value is None:
            continue
        if value.value.get_url() == request.path:
            return value


@register.simple_tag(takes_context=True, name='draw_menu')
def draw_menu(context, menu_name, request, all_menu_items = None):

    if not all_menu_items:
        all_menu_items = MenuItem.objects.filter(menu__name=menu_name).order_by('parent', 'id')

    tree = Tree(all_menu_items)

    target_node = get_target_node(tree.ids_dict, request)

    if not target_node:
        return Http404()

    result = tree_string_visible_from_root(tree, target_node, HTMLBuilder(), 4, True)

    template = Template(result).render(context=context)

    return template
