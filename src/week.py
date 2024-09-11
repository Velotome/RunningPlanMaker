import datetime
import calendar

from day import Day
from workout import Workout
import utils

class Week : 

  def __init__(self, id : int, first_day : datetime.date, type : utils.WeekType, workout_distribution, volume : float = 0.0):
    self.id = id
    self.first_day = first_day
    self.type = type
    self.volume = volume

    self.days = {}
    for day in calendar.Calendar().iterweekdays():
      date = self.first_day + datetime.timedelta(day)
      match day :
        case 0:
          self.days[calendar.MONDAY] = Day(date, Workout(workout_distribution[calendar.MONDAY], volume=round(0.0, 1)))
        case 1:
          self.days[calendar.TUESDAY] = Day(date, Workout(workout_distribution[calendar.TUESDAY], volume=round(0.1*self.volume, 1)))
        case 2:
          self.days[calendar.WEDNESDAY] = Day(date, Workout(workout_distribution[calendar.WEDNESDAY], volume=round(0.15*self.volume, 1)))
        case 3:
          self.days[calendar.THURSDAY] = Day(date, Workout(workout_distribution[calendar.THURSDAY], volume=round(0.1*self.volume, 1)))
        case 4:
          self.days[calendar.FRIDAY] = Day(date, Workout(workout_distribution[calendar.FRIDAY], volume=round(0.05*self.volume, 1)))
        case 5:
          self.days[calendar.SATURDAY] = Day(date, Workout(workout_distribution[calendar.SATURDAY], volume=round(0.35*self.volume, 1)))
        case 6:
          self.days[calendar.SUNDAY] = Day(date, Workout(workout_distribution[calendar.SUNDAY], volume=round(0.25*self.volume, 1)))

  def __str__(self) :
    result = f"Week {self.id} - {self.type.name} : {self.volume}km\n"
    for value in self.days.values():
      result = result + str(value)
    return result
  
  def toData(self):
    result = {'Week number'                                                            : self.id, 
              'First day'                                                              : str(self.first_day),
              'Week Type'                                                              : self.type.name,
              f'Monday : {self.days[calendar.MONDAY].workout.workout_type.name}'       : self.days[calendar.MONDAY].workout.volume,
              f'Tuesday : {self.days[calendar.TUESDAY].workout.workout_type.name}'     : self.days[calendar.TUESDAY].workout.volume,
              f'Wednesday : {self.days[calendar.WEDNESDAY].workout.workout_type.name}' : self.days[calendar.WEDNESDAY].workout.volume, 
              f'Thursday : {self.days[calendar.THURSDAY].workout.workout_type.name}'   : self.days[calendar.THURSDAY].workout.volume,
              f'Friday  : {self.days[calendar.FRIDAY].workout.workout_type.name}'      : self.days[calendar.FRIDAY].workout.volume,
              f'Saturday : {self.days[calendar.SATURDAY].workout.workout_type.name}'   : self.days[calendar.SATURDAY].workout.volume,
              f'Sunday : {self.days[calendar.SUNDAY].workout.workout_type.name}'       : self.days[calendar.SUNDAY].workout.volume,
              'Total volume'                                                           : self.volume
              }
    return result
        
if __name__ == "__main__":
  test_date = datetime.date(2024, 9, 9)
  test_week = Week(1, test_date, utils.WeekType.BUILD, 50.0)
  print(test_week)
