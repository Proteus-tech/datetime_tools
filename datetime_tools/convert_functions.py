import datetime
import time

from django.conf import settings

def convert_json_datetime_string_to_default_format(datetime_string):
    if not datetime_string:
        return datetime_string
    return time.strftime(settings.DATETIME_FORMAT,time.strptime(datetime_string,'%Y-%m-%d %H:%M:%S'))

def convert_json_date_string_to_default_format(date_string):
    if not date_string:
        return date_string
    return time.strftime(settings.DATE_FORMAT,time.strptime(date_string,'%Y-%m-%d'))

def string_to_datetime(string_in, format='%Y-%m-%d', sep=0):
    """
    sep = separator
    """
    if sep:
        string_in = unicode(string_in)[:sep]
    try:
        return datetime.datetime.strptime(string_in, format)
    except:
        return None

def flexible_isoformat_str2datetime(s):
    parts = s.split('.')
    dt = datetime.strptime(parts[0], "%Y-%m-%dT%H:%M:%S")
    return dt.replace(microsecond=int(parts[1]))