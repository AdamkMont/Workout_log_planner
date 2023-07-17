from collections import defaultdict
import datetime as dt
from typing import Optional

from main import Target, Exercise
from user import User

class ExerciseSuggester:
    """
    An algorithm that suggests exercises based on the user's targets, logged exercises, available time, and recovery.
    """
    def __init__(self, user: 'User'):
        self.user = user

    def suggest(self, available_time: Optional[int] = None) -> :
        """
        Suggests an exercise or routine based on the user's targets, logged exercises, available time, and recovery.
        """
        scores = defaultdict(0)  # Dictionary to hold the scores for each exercise

        # Prioritize exercises based on targets
        for target in self.user.targets:
            progress = target.check_progress(self.user.logs)
            scores[target.exercise] = (1 - progress) * 100  # The farther from the target, the higher the score
            #TODO prioritize daily over weekly/monthly

        # Consider recovery
        for log in self.user.logs:
            if log.exercise in scores:
                recovery_period = dt.datetime.now() - log.time
                if recovery_period.days < dt.timedelta(hours=36):
                    
                scores[log.exercise] -= 50  # Lower the score for recent high-intensity exercises

        # Consider available time
        if available_time is not None:
            for exercise in scores.keys():
                if exercise.suitable_duration > available_time:
                    scores[exercise] -= 50  # Lower the score for exercises that don't fit the available time

        # Rank exercises
        ranked_exercises = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        return ranked_exercises

if __name__ == '__main__':
    adam = User()
    adam.add_target(Target(Exercise('pushups'), 5, 2, 'weekly', 250))
    adam.log_exercise()