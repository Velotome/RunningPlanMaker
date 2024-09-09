import datetime
import calendar

from day import Day
from workout import Workout
from utils import WeekType, WorkoutType

class Week : 

  def __init__(self, first_date : datetime.date, week_type : WeekType):
    self.week_type = week_type

    self.days = {}
    for day in calendar.Calendar().iterweekdays():
      date = first_date + datetime.timedelta(day)
      match day :
        case 0:
          self.days[calendar.MONDAY] = {Day(date, Workout(WorkoutType.REST))}
        case 1:
          self.days[calendar.TUESDAY] = {Day(date, Workout(WorkoutType.SPEED))}
        case 2:
          self.days[calendar.WEDNESDAY] = {Day(date, Workout(WorkoutType.BASE))}
        case 3:
          self.days[calendar.THURSDAY] = {Day(date, Workout(WorkoutType.INTERVALS))}
        case 4:
          self.days[calendar.FRIDAY] = {Day(date, Workout(WorkoutType.RECOVERY_RUN))}
        case 5:
          self.days[calendar.SATURDAY] = {Day(date, Workout(WorkoutType.LONG_RUN))}
        case 6:
          self.days[calendar.SUNDAY] = {Day(date, Workout(WorkoutType.LONG_RUN))}
  
  def __str__(self) :
    result = ""
    for value in self.days.values():
      result = result + str(next(iter(value)))
    return result
        
if __name__ == "__main__":
  test_date = datetime.date(2024, 9, 9)
  test_week = Week(test_date, week_type = WeekType.BUILD)
  print(test_week)
