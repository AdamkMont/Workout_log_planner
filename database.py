from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# First, let's define the SQLAlchemy models

class DBExercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = relationship('DBTag', secondary='exercise_tags')
    suitable_duration = Column(Integer)

class DBTag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String)

exercise_tags = Table('exercise_tags', Base.metadata,
    Column('exercise_id', Integer, ForeignKey('exercises.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class DBTarget(Base):
    __tablename__ = 'targets'

    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    exercise = relationship('DBExercise')
    frequency = Column(Integer)
    intensity = Column(Integer)
    effect = Column(String)
    period = Column(String)
    goal = Column(Integer)

class DBExerciseLog(Base):
    __tablename__ = 'exercise_logs'

    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    exercise = relationship('DBExercise')
    sets = Column(Integer)
    reps = Column(Integer)
    intensity = Column(Integer)
    muscle_group = Column(String)
    effect = Column(String)
    time = Column(String)

class DBRoutine(Base):
    __tablename__ = 'routines'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    exercises = relationship('DBExercise', secondary='routine_exercises')

routine_exercises = Table('routine_exercises', Base.metadata,
    Column('routine_id', Integer, ForeignKey('routines.id')),
    Column('exercise_id', Integer, ForeignKey('exercises.id'))
)

class DBUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    targets = relationship('DBTarget')
    logs = relationship('DBExerciseLog')
    routines = relationship('DBRoutine')

# Now we define the DatabaseManager class

class DatabaseManager:
    """
    Handles interactions with the database.
    """
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        """
        Creates the necessary tables in the database.
        """
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """
        Returns a new Session object for database operations.
        """
        return self.Session()

