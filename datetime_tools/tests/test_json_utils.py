# -*- coding: utf-8 -*-
from unittest import TestCase
from datetime import datetime
import simplejson
from datetime_tools.json_utils import dthandler

class TestDTHandler(TestCase):

    def test_dumps_date_time(self):
        date_time_object = datetime(2015, 1, 1)
        dumped_date_time = simplejson.dumps(date_time_object, default=dthandler)
        self.assertEqual(dumped_date_time, '"2015-01-01T00:00:00"')
