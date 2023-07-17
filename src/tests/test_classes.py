from exercise import Exercise
from target import Target
from exercise_log import ExerciseLog
from routine import Routine

def test_exercise():
    exercise = Exercise('pushups', ['upper body', 'strength'], 5)
    assert exercise.name == 'pushups'
    assert exercise.tags == ['upper body', 'strength']
    assert exercise.suitable_duration == 5
    exercise.add_tag('endurance')
    assert 'endurance' in exercise.tags
    exercise.remove_tag('strength')
    assert 'strength' not in exercise.tags

def test_target():
    exercise = Exercise('pushups', ['upper body', 'strength'], 5)
    target = Target(exercise, 4, 3, 'strength', 'weekly', 100)
    assert target.exercise == exercise
    assert target.frequency == 4
    assert target.intensity == 3
    assert target.effect == 'strength'
    assert target.period == 'weekly'
    assert target.goal == 100

def test_exercise_log():
    exercise = Exercise('pushups', ['upper body', 'strength'], 5)
    log = ExerciseLog(exercise, 4, 25, 3, 'upper body', 'strength', 'daily')
    assert log.exercise == exercise
    assert log.sets == 4
    assert log.reps == 25
    assert log.intensity == 3
    assert log.muscle_group == 'upper body'
    assert log.effect == 'strength'
    assert log.period == 'daily'
    assert log.volume == 4 * 25

def test_routine():
    exercise1 = Exercise('pushups', ['upper body', 'strength'], 5)
    exercise2 = Exercise('squats', ['lower body', 'strength'], 10)
    routine = Routine('Strength Training', [exercise1])
    assert routine.name == 'Strength Training'
    assert routine.exercises == [exercise1]
    routine.add_exercise(exercise2)
    assert routine.exercises == [exercise1, exercise2]
    routine.remove_exercise(exercise1)
    assert routine.exercises == [exercise2]

