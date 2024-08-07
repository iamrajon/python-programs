from time import time, ctime, localtime
from datetime import datetime

"""
working with date time in python
"""

# epoch = time()
# print(epoch)
#
# et = ctime(epoch)
# print(et)

# stobj = localtime()
# print(stobj)
# print("date is:")
# print(stobj.tm_mday, end="/")
# print(stobj.tm_mon, end="/")
# print(stobj.tm_year)
#
# print("current Time is:")
# print(stobj.tm_hour, end=":")
# print(stobj.tm_min, end="")


"""
datetime module in python
"""
dt = datetime(year=2023, month=12, day=7, hour=14, minute=32)
print(dt)

# methods of datetime: now(), today()
ct = datetime.now()
print(ct)
print(ct.month)






