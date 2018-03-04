from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from radiogrid import RadioGridField


author = 'Your name here'

doc = """
bodong
"""


class Constants(BaseConstants):
    name_in_url = 'IFAGATV3EMEA'
    players_per_group = None
    num_rounds = 10

    historical_sales = [217,257,254,229,244,243,255,225,211,246,261,248,216,]
    actual_sales = [252,254,236,119,254,237,234,226,226,228]

    historical_forecast = ['null', 'null', 'null',248,235,241,242,251,234,213,237,253,250,]
    model_forecast = [227,244,251,241,238,243,241,236,223,227]

    mencast = ['null','null','null','null','null','null','null','null','null','null','null','null','null',]
    # actual_axis = [1,2,3,]
    historical_axis = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]

    occurence = 4
    product_name = 'IFAG-ATV3EMEA'

    instructions_template = 'Future/InstructionsInsert.html'



class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

ROWS = (
    (1, 'My initial forecast'),
    (2, 'The model forecast'),
    (3, 'My final forecast'),
)

VALUES = (
    (1,"Very inaccurate"),
    (2,"Slightly inaccurate"),
    (3,"Neither inaccurate nor accurate"),
    (4,"Moderately accurate"),
    (5,"Very accurate"),
)

TASK = (
    (1, 'Making initial forecast'),
    (2, 'Making final forecast'),
)

CHALLENGE_LEVEL = (
    (1,"Very easy"),
    (2,"Slightly easy"),
    (3,"Neither easy nor challenging"),
    (4,"A bit challenging"),
    (5,"Very challenging"),
)

class Player(BasePlayer):

    initial_forecast = models.IntegerField(min=0, max=400, label=False)
    forecast_amount = models.IntegerField(min=0, max=400, label=False)

    self_evaluation = RadioGridField(
        rows=ROWS,
        values=VALUES,
        require_all_fields=True,
        verbose_name=False,
    )

    task_challenge = RadioGridField(
        rows=TASK,
        values=CHALLENGE_LEVEL,
        require_all_fields=True,
        verbose_name=False,
    )
    def role(self):
        if self.id_in_group % 2 == 0:
            return 'treatment'
        else:
            return 'control'

