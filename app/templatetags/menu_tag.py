from django import template
from app.models import Menu, MenuItem
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        menu_item = MenuItem.objects.get(menu=menu, url=context['request'].path)
    except:
        return ''

    item_generator = (x for x in menu_item.get_menu_list())
    output = menu_formatter(item_generator, menu_item)
    return mark_safe(output)


def menu_formatter(item_generator, active_item, tabs=0):
    try:
        item = next(item_generator)
    except StopIteration:
        return ''
    indent = '\t' * tabs
    current_level = item.get_current_level()
    output = '\n{0}<ul>\n'.format(indent)

    for node in current_level:
        active_class = 'class="text-success" ' if node == active_item else ''
        output += '{}<li><a {}href="{}">{}</a>'.format(indent+'\t', active_class, node.url, node.name)
        if node == item:
            output += menu_formatter(item_generator, active_item, tabs+1)
        output += '</li>\n'

    output += '\n{0}</ul>\n{0}'.format(indent)
    return output

