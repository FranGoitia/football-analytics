from sqlalchemy import Enum

outcomes = ('Failed', 'Completed')
shots_outcomes = ('Saved', 'Blocked', 'Off Target', 'Post', 'Goal')
body_parts = ('Head', 'Left', 'Right')
block_types = ('Cross', 'Pass', 'Shot')
error_types = ('Shot', 'Goal')
gk_types = ('Save', 'Claim', 'Punch')
types = ('Defense', 'Attack')
cards_types = ('Red', 'Yellow', '2nd Yellow')
positions = ('GK', 'D', 'DC', 'DL', 'DR', 'DMC', 'M', 'MC', 'MR', 'ML', 'AM', 'AMC', 'AML', 'AMR', 'FW')
positions_types = ('Goalkeeper', 'Defender', 'Midfielder', 'Forward')
availability = ('Starter', 'Bench', 'Out')
locations = ('Home', 'Away')
foots = ('Right', 'Left', 'Both')

vars_ = locals().copy()
for k, v in vars_.items():
    if isinstance(v, tuple):
        locals()[k] = Enum(*v, name=k)
