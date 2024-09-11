import datetime
import calendar
import csv
import os

import utils
from week import Week


class Plan():

  def __init__(self, 
               start_date : datetime.date, 
               race_date : datetime.date, 
               race_km : int, 
               starting_volume : int = 0):
    
    # race specific info
    self.race_km = race_km
    self.race_date = race_date

    # plan parameters
    self.nb_taper = 2
    self.build_cycle = 4
    self.starting_volume = starting_volume
    self.workout_distribution = {calendar.MONDAY : utils.WorkoutType.REST,
                                 calendar.TUESDAY : utils.WorkoutType.SPEED,
                                 calendar.WEDNESDAY : utils.WorkoutType.BASE,
                                 calendar.THURSDAY : utils.WorkoutType.INTERVALS,
                                 calendar.FRIDAY : utils.WorkoutType.RECOVERY_RUN,
                                 calendar.SATURDAY : utils.WorkoutType.LONG_RUN,
                                 calendar.SUNDAY : utils.WorkoutType.LONG_RUN}

    self.cal = calendar.Calendar(firstweekday = 0)
    
    # make it so the plan begin on the next monday
    self.start_date = utils.findMonday(start_date, of_next_week=True)
    self.duration_days = (self.race_date - self.start_date).days
    self.duration_weeks = self.duration_days // 7 + 1

    self.plan = {}
    self.plan_list = []

  def __str__(self) -> str:
    
    if len(self.plan) == 0 :
      return "[WARNING] Plan has not been generated"
    
    result = ""
    for key, value in self.plan.items():
      result = result + f"{value}\n"
    return result
  
  def toData(self):
    result = []
    for week in self.plan.values():
      result.append(week.toData())
    return result

  def generatePlan(self):
    monday = utils.findMonday(self.race_date)
    volume = self.starting_volume
    for week in range(1, self.duration_weeks):
      match week :
        # Race week
        case week if week == self.duration_weeks - 1:
          self.plan[week] = Week(week, utils.findMonday(self.race_date), utils.WeekType.RACE, self.workout_distribution, 0.0)
        # Taper week
        case week if week >= self.duration_weeks - 1 - self.nb_taper:
          self.plan[week] = Week(week, monday, utils.WeekType.TAPER, self.workout_distribution, 0.5 * volume)
        # Reduced week
        case week if week % self.build_cycle == 0:
          self.plan[week] = Week(week, monday, utils.WeekType.REDUCED, self.workout_distribution, 0.5 * volume)
        # Build week
        case _ :
          volume = round(1.1 * volume, 1)
          self.plan[week] = Week(week, monday, utils.WeekType.BUILD, self.workout_distribution, volume)
      monday = monday - datetime.timedelta(7)

  def exportPlan(self, plan_name = 'latest_plan.csv'):
    
    filename = "plans/" + plan_name

    data = self.toData()
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
      fieldnames = ['Week number', 'First day', 'Week Type', 
                    f"Monday : {self.workout_distribution[calendar.MONDAY].name}",
                    f"Tuesday : {self.workout_distribution[calendar.TUESDAY].name}",
                    f"Wednesday : {self.workout_distribution[calendar.WEDNESDAY].name}", 
                    f"Thursday : {self.workout_distribution[calendar.THURSDAY].name}",
                    f"Friday  : {self.workout_distribution[calendar.FRIDAY].name}",
                    f"Saturday : {self.workout_distribution[calendar.SATURDAY].name}",
                    f"Sunday : {self.workout_distribution[calendar.SUNDAY].name}",
                    'Total volume']
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(data)


if __name__ == "__main__":
  start_date = datetime.date(2024, 9, 9)
  race_date = datetime.date(2024, 9, 9) + datetime.timedelta(21)

  test_plan = Plan(start_date=start_date,
                   race_date=race_date,
                   race_km=100,
                   starting_volume=50)
  
  test_plan.generatePlan()
  test_plan.exportPlan()
  