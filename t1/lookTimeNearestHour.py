#lookTimeNearestHour.py

import datetime                     #Python date/time
from django.utils import timezone   #Django date/time
from polls.models import Question
#import pytz


def creatNearestHour():
  #now_datetime = datetime.datetime.now()
  #print now_datetime
  #today_datetime = datetime.datetime.today()
  #print today_datetime
  #nearestHour_datetime = datetime.datetime(2015, 1, 23, 11, 0, 0)
  #print nearestHour_datetime
  #naive = datetime.datetime.utcnow()
  #print naive

  now_timezone = timezone.now()
  print now_timezone
  print now_timezone.year
  print now_timezone.month
  print now_timezone.day
  print now_timezone.hour
  print now_timezone.minute
  print now_timezone.second

  noon_timezone = timezone.datetime(now_timezone.year,
  now_timezone.month, now_timezone.day, 12, 0, 0)
  print noon_timezone
  #noon_timezone == now_timezone

  flg1 = timezone.is_naive(noon_timezone)
  print "flg_noon_timezone", flg1

  flg2 = timezone.is_naive(now_timezone)
  print "flg_now_timezone", flg2

  #Convert noon_timezone from naive to aware
  noon_timezone_convertedToaware = timezone.make_aware(noon_timezone, timezone='UTC')
  #noon_timezone_convertedToaware = timezone.make_aware(noon_timezone)
  #TypeError: tzinfo argument must be None or of a tzinfo subclass, not type 'str'
  print noon_timezone
  print noon_timezone_convertedToaware
  flg3 = timezone.is_naive(noon_timezone)
  print "flg_noon_timezone", flg3
  flg4 = timezone.is_naive(noon_timezone_convertedToaware)
  print "flg_noon_timezone_convertedToaware", flg4


  #paris_tz = pytz.timezone("Europe/Paris")
  #paris = paris_tz.localize(datetime.datetime(2012, 3, 3, 1, 30))
  #print paris

  #noon_timezone = timezone.make_aware(noon_timezone, timezone=USE_TZ)
  #print noon_timezone

  #if now_timezone > noon_timezone:
  #  print "noon_timezone is behind"
  #elif now_timezone == noon_timezone:
  #  print "noon_timezone is  same"
  #else:
  #  print "noon_timezone is ahead"
  #return 0

ans = creatNearestHour()






