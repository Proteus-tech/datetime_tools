from django import template
register = template.Library()

from datetime_tools.convert_functions import convert_json_datetime_string_to_default_format, convert_json_date_string_to_default_format

@register.simple_tag
def datetime_default_format(datetime_string, value_if_not_available=''):
    if not datetime_string:
        return  value_if_not_available
    return convert_json_datetime_string_to_default_format(datetime_string)

@register.simple_tag
def date_default_format(date_string, value_if_not_available=''):
    if not date_string:
        return  value_if_not_available
    return convert_json_date_string_to_default_format(date_string)
  