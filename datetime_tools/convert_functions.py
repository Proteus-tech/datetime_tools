from datetime import datetime, date

from django.conf import settings

dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime) or isinstance(obj, date) else None

def convert_json_datetime_string_to_default_format(datetime_string):
    if not datetime_string:
        return datetime_string
    return datetime.strftime(datetime.strptime(datetime_string,'%Y-%m-%d %H:%M:%S'), settings.DATETIME_FORMAT)

def convert_json_date_string_to_default_format(date_string):
    if not date_string:
        return date_string
    return datetime.strftime(datetime.strptime(date_string,'%Y-%m-%d'), settings.DATE_FORMAT)

def string_to_datetime(string_in, format='%Y-%m-%d', sep=0):
    """
    sep = separator
    """
    if sep:
        string_in = unicode(string_in)[:sep]
    try:
        return datetime.strptime(string_in, format)
    except:
        return None

def flexible_isoformat_str2datetime(s):
    parts = s.split('.')
    dt = datetime.strptime(parts[0], "%Y-%m-%dT%H:%M:%S")
    microsecond = 0
    if len(parts) > 1:
        microsecond = int(parts[1])
    return dt.replace(microsecond=microsecond)