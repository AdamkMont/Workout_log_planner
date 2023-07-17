from dataclasses import dataclass
from typing import List

from main import ExerciseLog, Routine, Target
from suggester import ExerciseSuggester

@dataclass
class User:
    """
    Represents a user of the app.
    """
    targets: List[Target]
    logs: List[ExerciseLog]
    routines: List[Routine]
    suggester: ExerciseSuggester

    def __post_init__(self):
        self.suggester = ExerciseSuggester(self)

    def log_exercise(self, log: ExerciseLog):
        """
        Logs an exercise.
        """
        self.logs.append(log)

    def add_target(self, target: Target):
        """
        Adds a target.
        """
        self.targets.append(target)

    def remove_target(self, target: Target):
        """
        Removes a target.
        """
        if target in self.targets:
            self.targets.remove(target)

    def add_routine(self, routine: Routine):
        """
        Adds a routine.
        """
        self.routines.append(routine)

    def remove_routine(self, routine: Routine):
        """
        Removes a routine.
        """
        if routine in self.routines:
            self.routines.remove(routine)

