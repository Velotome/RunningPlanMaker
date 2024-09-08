import enum

class WorkoutType(enum.Enum) :
    BASE = 1
    INTERVALS = 2
    LONG_RUN = 3
    RECOVERY_RUN = 4
    REST = 5
    SPEED = 6

class Workout() :

    def __init__(self, workout_type : WorkoutType) :
        self. workout_type = workout_type