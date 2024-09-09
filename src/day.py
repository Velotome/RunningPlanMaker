import datetime

from workout import Workout
import utils

class Day:

  def __init__(self, date : datetime.date, workout : Workout):

    self.date = date
    self.weekday = date.weekday()
    self.workout = workout

    match self.weekday :
      case 0:
        self.day_name = 'MONDAY'
      case 1: 
        self.day_name = 'TUESDAY'
      case 2: 
        self.day_name = 'WEDNESDAY'
      case 3: 
        self.day_name = 'THURSDAY'
      case 4: 
        self.day_name = 'FRIDAY'
      case 5: 
        self.day_name = 'SATURDAY'
      case 6: 
        self.day_name = 'SUNDAY'

  def __str__(self) -> str:
    return f"{self.day_name} {self.date} : {str(self.workout)} \n"

if __name__ == "__main__":
  test_date = datetime.date(2024, 9, 9)
  test_day = Day(test_date, workout = Workout(utils.WorkoutType.BASE))
  print(test_day)
