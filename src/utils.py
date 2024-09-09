import enum
import datetime

class WeekType(enum.Enum) :
  BUILD = 1
  REDUCED = 2
  RACE = 3
  TAPER = 4

class WorkoutType(enum.Enum) :
    BASE = 1
    INTERVALS = 2
    LONG_RUN = 3
    RECOVERY_RUN = 4
    REST = 5
    SPEED = 6

def findMonday(date : datetime.date, of_next_week : bool = False) -> datetime.date :
   if of_next_week :
      return date - datetime.timedelta(date.weekday() + 7)
   else :
      return date - datetime.timedelta(date.weekday())
