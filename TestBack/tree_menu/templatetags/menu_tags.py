from django import template
import tree_menu.views as views
from tree_menu.models import *

register = template.Library()


@register.inclusion_tag('tags/d_menu.html')
def draw_menu(name_menu):
    Main_menu = my_menu.objects.get(name_menu=name_menu)
    dic_menu = {}
    dic_sub_menu = {}
    dic_sub2_menu = []
    for i in Main_menu.submenu_set.all():
        if len(i.submenu_set.all()) == 0:
            pass
        else:
            for p in i.submenu_set.all():
                for r in p.submenu_set.all():
                    dic_sub2_menu.append(r)
                dic_sub_menu[p] = dic_sub2_menu
            dic_menu[i] = dic_sub_menu
            dic_sub_menu = {}
            dic_sub2_menu = []
    return {'m_menu': dic_menu}
