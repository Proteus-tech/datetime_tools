# -*- coding: utf-8 -*-
from datetime import datetime, date

dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime) or isinstance(obj, date) else None
