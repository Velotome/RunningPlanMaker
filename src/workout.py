import utils

class Workout() :

  def __init__(self, workout_type : utils.WorkoutType) :
    self.workout_type = workout_type

  def __str__(self) :
    return self.workout_type.name
  
if __name__ == "__main__":
  test_workout = Workout(utils.WorkoutType.BASE)
  print(test_workout)