import enum
from workout import Workout, WorkoutType

class Day(enum.Enum) :
  MONDAY = 1
  TUESDAY = 2
  WEDNESDAY = 3
  THURSDAY = 4
  FRIDAY = 5
  SATURDAY = 6
  SUNDAY = 7

class WeekType(enum.Enum) :
  BUILD = 1
  REDUCED = 2
  RACE = 3
  TAPER = 4

class Week : 
  def __init__(self, week_number : int, week_type : WeekType):
    self.week_number = week_number
    self.week_type = week_type

    days = {}
    for day in Day._member_names_:
      match day :
        case 'MONDAY':
          days[day] = {Workout(WorkoutType.REST)}
        case 'TUESDAY':
          days[day] = {Workout(WorkoutType.SPEED)}
        case 'WEDNESDAY':
          days[day] = {Workout(WorkoutType.BASE)}
        case 'THURSDAY':
          days[day] = {Workout(WorkoutType.INTERVALS)}
        case 'FRIDAY':
          days[day] = {Workout(WorkoutType.RECOVERY_RUN)}
        case 'SATURDAY':
          days[day] = {Workout(WorkoutType.LONG_RUN)}
        case 'SUNDAY':
          days[day] = {Workout(WorkoutType.LONG_RUN)}
    self.days = days
  
  def __str__(self) :
    result = ""
    for key, value in self.days.items():
      result = result + f"{key} : {value} \n"
    return result
        