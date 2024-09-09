import datetime
import calendar

import utils
from week import Week


class Plan():

  def __init__(self, 
               start_date : datetime.date, 
               race_date : datetime.date, 
               race_km : int, 
               starting_weekly_km : int = 0):
    
    # race specific info
    self.race_km = race_km
    self.race_date = race_date

    # plan parameters
    self.nb_taper = 2
    self.build_cycle = 4

    self.cal = calendar.Calendar(firstweekday = 0)
    
    # make it so the plan begin on the next monday
    self.start_date = utils.findMonday(start_date, of_next_week=True)
    self.duration_days = (race_date - start_date).days
    self.duration_weeks = self.duration_days // 7

    self.plan = {}



  def __str__(self) -> str:
    
    if len(self.plan) == 0 :
      return "[WARNING] Plan has not been generated"
    
    result = ""
    for key, value in self.plan.items():
      result = result + f"Week {key} :\n{next(iter(value))}\n"
    return result



  def generatePlan(self):
    monday = utils.findMonday(self.race_date)
    race_week = self.duration_weeks + 1
    for week in range(1, race_week):
      match week :
        # Race week
        case 0 if week == race_week:
          self.plan[week] = {Week(utils.findMonday(self.race_date), utils.WeekType.RACE)}
        # Taper week
        case 1 if week > race_week - self.nb_taper:
          self.plan[week] = {Week(monday, utils.WeekType.TAPER)}
        # Reduced week
        case 2 if week % self.build_cycle == 0:
          self.plan[week] = {Week(monday, utils.WeekType.REDUCED)}
        # Build week
        case _ :
          self.plan[week] = {Week(monday, utils.WeekType.BUILD)}
      monday = monday - datetime.timedelta(7)

if __name__ == "__main__":
  start_date = datetime.date(2024, 9, 9)
  race_date = datetime.date(2024, 9, 9) + datetime.timedelta(21)

  test_plan = Plan(start_date=start_date,
                   race_date=race_date,
                   race_km=100,
                   starting_weekly_km=50)
  
  test_plan.generatePlan()

  print(test_plan)