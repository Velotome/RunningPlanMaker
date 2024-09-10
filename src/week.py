import datetime
import calendar

from day import Day
from workout import Workout
import utils

class Week : 

  def __init__(self, id : int, first_date : datetime.date, type : utils.WeekType, volume : float = 0.0):
    self.id = id
    self.type = type
    self.volume = volume

    self.days = {}
    for day in calendar.Calendar().iterweekdays():
      date = first_date + datetime.timedelta(day)
      match day :
        case 0:
          self.days[calendar.MONDAY] = {Day(date, Workout(utils.WorkoutType.REST))}
        case 1:
          self.days[calendar.TUESDAY] = {Day(date, Workout(utils.WorkoutType.SPEED))}
        case 2:
          self.days[calendar.WEDNESDAY] = {Day(date, Workout(utils.WorkoutType.BASE))}
        case 3:
          self.days[calendar.THURSDAY] = {Day(date, Workout(utils.WorkoutType.INTERVALS))}
        case 4:
          self.days[calendar.FRIDAY] = {Day(date, Workout(utils.WorkoutType.RECOVERY_RUN))}
        case 5:
          self.days[calendar.SATURDAY] = {Day(date, Workout(utils.WorkoutType.LONG_RUN))}
        case 6:
          self.days[calendar.SUNDAY] = {Day(date, Workout(utils.WorkoutType.LONG_RUN))}
  
  def __str__(self) :
    result = f"Week {self.id} - {self.type.name} : {self.volume}km\n"
    for value in self.days.values():
      result = result + str(next(iter(value)))
    return result
        
if __name__ == "__main__":
  test_date = datetime.date(2024, 9, 9)
  test_week = Week(1, test_date, utils.WeekType.BUILD, 50.0)
  print(test_week)
