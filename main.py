from dataclasses import dataclass
import datetime as dt
from typing import List

from database_manager import DatabaseManager

@dataclass
class Exercise:
    """
    Represents an individual exercise.
    """
    name: str
    tags: List[str]
    min_duration: int
    max_duration: int
    dependencies: List[str]

    def add_tag(self, tag: str):
        """
        Adds a tag to the exercise.
        """
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str):
        """
        Removes a tag from the exercise.
        """
        if tag in self.tags:
            self.tags.remove(tag)


@dataclass
class Target:
    """
    Represents a user-defined target for a given exercise, frequency, intensity, and desired effect over a certain period (daily, weekly, monthly).
    """
    exercise: Exercise
    frequency: int  # times per period
    intensity: int  # on a scale of 1-3
    effect: str  # Strength, hypertrophy, cardio, endurance, mobility, flexibility
    period: str  # daily, weekly, monthly
    goal: int  # goal for the period

    def check_progress(self, logs: List['ExerciseLog']):
        """
        Checks the progress of the target based on the provided exercise logs.
        """
        logs_for_target = [log for log in logs if log.exercise == self.exercise and log.period == self.period]
        return sum(log.volume for log in logs_for_target) / self.goal  # returns the progress as a fraction of the goal


@dataclass
class ExerciseLog:
    """
    Represents a completed exercise session.
    """
    exercise: Exercise
    sets: int
    reps: int
    intensity: int  # perceived intensity
    muscle_group: str
    effect: str  # training effect/goal
    time: dt.datetime  # daily, weekly, monthly

    @property
    def volume(self):
        """
        Calculates the volume of the exercise session.
        """
        return self.sets * self.reps

# Now we define the Routine class

@dataclass
class Routine:
    """
    Represents a set of exercises meant to be performed together as a part of a workout routine or module.
    """
    name: str
    exercises: List[Exercise]

    def add_exercise(self, exercise: Exercise):
        """
        Adds an exercise to the routine.
        """
        if exercise not in self.exercises:
            self.exercises.append(exercise)

    def remove_exercise(self, exercise: Exercise):
        """
        Removes an exercise from the routine.
        """
        if exercise in self.exercises:
            self.exercises.remove(exercise)



def main():
    # Create the database manager
    db_manager = DatabaseManager('sqlite:///exercise_tracker.db')

    # Create the database tables
    db_manager.create_tables()

    # The rest of the application setup and run code will go here
    pass

if __name__ == '__main__':
    main()
