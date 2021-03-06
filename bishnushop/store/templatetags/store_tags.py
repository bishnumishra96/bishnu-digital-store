from django import template
from math import floor

register = template.Library()

@register.simple_tag()
def sale_price(price , descount):
    return floor(price - (price * descount * 0.01))


@register.simple_tag()
def get_active_class(active_category, category):
    print(active_category, category)
    if active_category is '' and category == '':
        return 'active'
    if active_category is '':
        return ''
    if int(active_category) == category:
        return ' active'
    if int(active_category) != category:
        return ''
    return ''