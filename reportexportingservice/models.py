from sqlalchemy import Column, Integer, String
from database import Base


class Report(Base):
    """Model for the reports table"""
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    type = Column(String())

    def __init__(self, name=type):
        self.type = type

    def __repr__(self):
        return '<id %r>' % (self.type)
