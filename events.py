from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.types import Boolean
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from model import Base, enums


class Shot(Base):
    __tablename__ = 'shots'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    end_x = Column(Float)
    end_y = Column(Float)
    end_z = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', foreign_keys=[player_id], backref='shots')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', backref='shots')
    assister_id = Column(ForeignKey('players.id'), index=True)
    assister = relationship('Player', foreign_keys=[assister_id])
    pass_graph = Column(ARRAY(Integer))
    is_own = Column(Boolean, default=False)
    body_part = Column(enums.body_parts)
    big_chance = Column(Boolean, default=False)
    open_play = Column(Boolean)
    assist = Column(Boolean, default=False)
    penalty = Column(Boolean, default=False)
    freekick = Column(Boolean, default=False)
    outcome = Column(enums.shots_outcomes)


class Pass(Base):
    __tablename__ = 'passes'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    end_x = Column(Float)
    end_y = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', backref='passes')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', backref='passes')
    assist = Column(Boolean, default=False)
    headed = Column(Boolean, default=False)
    cross = Column(Boolean, default=False)
    corner = Column(Boolean, default=False)
    set_piece = Column(Boolean, default=False)
    throw_in = Column(Boolean, default=False)
    key_pass = Column(Boolean, default=False)
    big_chance_created = Column(Boolean, default=False)
    long_ball = Column(Boolean, default=False)
    through_ball = Column(Boolean, default=False)
    outcome = Column(enums.outcomes)


class Dribble(Base):
    __tablename__ = 'dribbles'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', foreign_keys=[player_id], backref='dribbles')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', foreign_keys=[team_id], backref='dribbles')
    other_player_id = Column(ForeignKey('players.id'), index=True)
    other_player = relationship('Player', foreign_keys=[other_player_id], backref='passed_by')
    other_team_id = Column(ForeignKey('teams.id'), index=True)
    other_team = relationship('Team', foreign_keys=[other_team_id], backref='passed_by')
    outcome = Column(enums.outcomes)


class Tackle(Base):
    __tablename__ = 'tackles'
    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', foreign_keys=[player_id], backref='tackles')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', foreign_keys=[team_id], backref='tackles')
    other_player_id = Column(ForeignKey('players.id'), index=True)
    other_player = relationship('Player', foreign_keys=[other_player_id], backref='tackled')
    other_team_id = Column(ForeignKey('teams.id'), index=True)
    other_team = relationship('Team', foreign_keys=[other_team_id], backref='dispossessed')
    regain_possession = Column(Boolean)


class AerialDuel(Base):
    __tablename__ = 'aerial_duels'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', foreign_keys=[player_id], backref='aerial_duels_won')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', foreign_keys=[team_id], backref='aerial_duels_won')
    other_team_id = Column(ForeignKey('teams.id'), index=True)
    other_team = relationship('Team', foreign_keys=[other_team_id], backref='aerial_duels_lost')
    other_player_id = Column(ForeignKey('players.id'), index=True)
    other_player = relationship('Player', foreign_keys=[other_player_id], backref='aerial_duels_lost')
    type = Column(enums.types)


class Interception(Base):
    __tablename__ = 'interceptions'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team')
    won = Column(Boolean)


class Clearance(Base):
    __tablename__ = 'clearances'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', backref='clearances')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', backref='clearances')
    headed = Column(Boolean, default=False)
    effective = Column(Boolean, default=False)
    off_the_line = Column(Boolean, default=False)


class Block(Base):
    __tablename__ = 'blocks'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    type = Column(enums.block_types)
    headed = Column(Boolean)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', foreign_keys=[player_id], backref='blocks')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', foreign_keys=[team_id], backref='blocks')
    other_player_id = Column(ForeignKey('players.id'), index=True)
    other_player = relationship('Player', foreign_keys=[other_player_id], backref='blocked')
    other_team_id = Column(ForeignKey('teams.id'), index=True)
    other_team = relationship('Team', foreign_keys=[other_team_id], backref='blocked')


class Turnover(Base):
    __tablename__ = 'turnovers'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', foreign_keys=[player_id], backref='turnovers')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', foreign_keys=[team_id], backref='turnovers')


class Error(Base):
    __tablename__ = 'errors'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    type = Column(enums.error_types)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', foreign_keys=[player_id], backref='errors')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', foreign_keys=[team_id], backref='errors')


class GoalKeep(Base):
    __tablename__ = 'goalkeeping'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    headed = Column(Boolean)
    type = Column(enums.gk_types)
    penalty = Column(Boolean)
    player_id = Column(ForeignKey('players.id'), index=True)
    team_id = Column(ForeignKey('teams.id'), index=True)


class Offside(Base):
    __tablename__ = 'offsides'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', backref='offsides')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', backref='offsides')


class Foul(Base):
    __tablename__ = 'fouls'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', foreign_keys=[player_id], backref='fouls')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', foreign_keys=[team_id], backref='fouls')
    other_player_id = Column(ForeignKey('players.id'), index=True)
    other_player = relationship('Player', foreign_keys=[other_player_id], backref='fouled')
    other_team_id = Column(ForeignKey('teams.id'), index=True)
    other_team = relationship('Team', foreign_keys=[other_team_id], backref='fouled')


class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    match = relationship('Match')
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', backref='cards')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', backref='cards')
    type = Column(enums.cards_types)


class Substitution(Base):
    __tablename__ = 'substitutions'

    id = Column(Integer, primary_key=True)
    match_id = Column(ForeignKey('matches.id'), index=True)
    mins = Column(Integer)
    secs = Column(Integer)
    mins_exp = Column(Integer)
    player_id = Column(ForeignKey('players.id'), index=True)
    player = relationship('Player', foreign_keys=[player_id], backref='subs_in')
    other_player_id = Column(ForeignKey('players.id'), index=True)
    other_players = relationship('Player', foreign_keys=[other_player_id], backref='subs_out')
    team_id = Column(ForeignKey('teams.id'), index=True)
    team = relationship('Team', backref='substitutions')
