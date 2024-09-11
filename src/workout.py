import utils

class Workout() :

  def __init__(self, workout_type : utils.WorkoutType, volume : float) :
    self.workout_type = workout_type
    self.volume = volume

  def __str__(self) :
    return f"{self.workout_type.name} for {self.volume}km"
  
if __name__ == "__main__":
  test_workout = Workout(utils.WorkoutType.BASE, volume=10.5)
  print(test_workout)