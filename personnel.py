#!/usr/bin/env python
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date, UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from model import Base, enums


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    dob = Column(Date, nullable=True)
    country_id = Column(ForeignKey('countries.id'), nullable=True, index=True)
    country = relationship('Country', backref='players')
    position = Column(enums.positions)
    position_type = Column(enums.positions_types)
    positions = Column(ARRAY(String), nullable=True)
    availability = Column(enums.availability)
    teams = relationship('Team', secondary='contracts')
    number = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    foot = Column(enums.foots)
    whoscored_id = Column(Integer, nullable=False)
    grandt_id = Column(Integer)
    grandt_value = Column(Float)
    transfermarkt_value = Column(Float)
    transfermarkt_id = Column(Integer)

    UniqueConstraint(whoscored_id)

    def __repr__(self):
        return 'Player({0}, {1}, {2}, {3})'.format(self.id, self.name,
                                                   self.dob, self.position)


class Official(Base):
    __tablename__ = 'officials'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    birth_date = Column(Date, nullable=True)
    country_id = Column(ForeignKey('countries.id'), nullable=True, index=True)
    country = relationship('Country', backref='officials')


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', backref='contracts')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', backref='contracts')
    starts = Column(Date, nullable=True)
    ends = Column(Date, nullable=True)
    wage = Column(Integer, nullable=True)


class PlayersInjuries(Base):
    __tablename__ = 'players_injuries'

    id = Column(Integer, primary_key=True)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', backref='injuries')
    description = Column(String)
    starts = Column(Date)
    ends = Column(Date)
