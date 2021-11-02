from dataclasses import dataclass, field


from sqlalchemy import create_engine, Column, String, Integer, Table, ForeignKey, Date
from sqlalchemy.orm import registry, declarative_base, sessionmaker


Base = declarative_base()
# mapper_registry = registry()
#
# @mapper_registry.mapped
# @dataclass
class Exercises(Base):
    __tablename__ = 'exercise_list'

    ex_id = Column(Integer, primary_key=True)
    name = Column(String(40))

class Tags(Base):
    __tablename__ = 'tags'

    tag_id = Column(Integer, primary_key=True)
    name = Column(String(50))

class Exercise_Tags(Base):
    __tablename__ = 'exercise_tags'

    et_id = Column(Integer, primary_key=True)
    ex_id = Column(ForeignKey(Exercises.ex_id))
    tag_id = Column(ForeignKey(Tags.tag_id))

class Routine(Base):
    __tablename__ = 'routines'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    date = Column(Date)

class Routine_exercise(Base):
    __tablename__ = 'routine_exercises'

    id = Column(Integer, primary_key=True)
    r_id = Column(ForeignKey(Routine.id))
    ex_id = Column(ForeignKey(Exercises.ex_id))

class Workouts(Base):
    __tablename__ = 'workouts'

    date = Column(Date, primary_key=True)
    r_id = Column(ForeignKey(Routine.id))

class Workout_Log(Base):
    __tablename__ = 'workout_log'

    date = Column(Date, primary_key=True)
    ex_id = Column(ForeignKey(Exercises.ex_id))
    target = Column(Integer)
    sets = Column(Integer)
    reps = Column(Integer)

engine = create_engine("sqlite+pysqlite:///workout_log.db", future=True, echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)



    # set_of_muscle_groups = {'Push', 'Pull', 'Calves', 'Hamstring', 'Quad', 'Glute', 'Leg', 'Stabiliser', 'Rotation', 'Core', 'Chest', 'Back', 'Arm', 'Shoulder'}
    # muscle_groups: list
    # days_trained: dict
    # target: int = 0
    #
    # @property
    # def muscle_group(self):
    #     return self.muscle_groups
    #
    # @muscle_group.setter
    # def muscle_group(self, *value) -> None:
    #     for v in value:
    #         if v not in self.set_of_muscle_groups:
    #             raise AttributeError('Group doesn\'t exist')
    #         else:
    #             self.muscle_groups.append(v)
    #
    # @property
    # def weekly_target(self) -> int:
    #     return self.target
    #
    # @weekly_target.setter
    # def weekly_target(self, v: int) -> None:
    #     self.target = v
    #
    # def add_group(self, v: str) -> None:
    #     self.set_of_muscle_groups.add(v)
    #
    # def record_day(self, date, volume=int):
    #     self.days_trained.update({date: volume})
