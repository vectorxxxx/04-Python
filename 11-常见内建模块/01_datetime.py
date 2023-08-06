# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    zone = int(re.match(r'UTC([+-]\d+):00', tz_str).group(1))
    time_zone = time.replace(tzinfo=timezone(timedelta(hours=zone)))
    return time_zone.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
