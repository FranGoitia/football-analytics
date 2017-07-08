from sqlalchemy import (Column, Boolean, Integer, String, ForeignKey, DateTime,
                        UniqueConstraint)
from sqlalchemy.orm import relationship

from model import Base


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return '%s' % (self.name,)


class Stadium(Base):
    __tablename__ = 'stadiums'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country_id = Column(ForeignKey('countries.id'), nullable=True)
    country = relationship('Country', backref='stadiums')
    state = Column(String)
    address = Column(String)
    zipcode = Column(String)
    teams = relationship('Team', secondary='stadiums_teams')

    UniqueConstraint(name, country_id)

    def __repr__(self):
        return self.name


class StadiumTeam(Base):
    __tablename__ = 'stadiums_teams'

    id = Column(Integer, primary_key=True)
    stadium_id = Column(ForeignKey('stadiums.id'), index=True, nullable=False)
    team_id = Column(ForeignKey('teams.id'), index=True, nullable=False)


class League(Base):
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    season = Column(String, nullable=False)
    country_id = Column(ForeignKey('countries.id'), nullable=False, index=True)
    country = relationship('Country', backref='leagues', uselist=False)

    UniqueConstraint(name, season, country_id)

    def __repr__(self):
        return '{league: %s - %s, country: %s}' % (self.name, self.season, self.country)


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country_id = Column(ForeignKey('countries.id'), nullable=False, index=True)
    country = relationship('Country', backref='teams')
    coast = Column(String)
    division = Column(String)
    players = relationship('Player', secondary='contracts')
    stadiums = relationship('Stadium', secondary='stadiums_teams')

    UniqueConstraint(name, country_id)

    def __repr__(self):
        return '{name: %s, country: %s}' % (self.name, self.country.name)


class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    league_id = Column(ForeignKey('leagues.id'), nullable=False, index=True)
    league = relationship('League', backref='matches')
    home_id = Column(ForeignKey('teams.id'), nullable=False, index=True)
    home = relationship('Team', foreign_keys=[home_id], backref='home_matches')
    away_id = Column(ForeignKey('teams.id'), nullable=False, index=True)
    away = relationship('Team', foreign_keys=[away_id], backref='away_matches')
    stadium_id = Column(ForeignKey('stadiums.id'), nullable=True, index=True)
    stadium = relationship('Stadium', backref='matches')
    result = Column(String, nullable=True)
    aggregated = Column(Boolean, default=False)

    UniqueConstraint(date, home_id, away_id)

    def __repr__(self):
        return '{date: %s, league: %s, home: %s, away: %s, result: %s}' \
            % (self.date, self.league.name, self.home.name,
               self.away.name, self.result)
