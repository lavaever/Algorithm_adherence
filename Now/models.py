from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from radiogrid import RadioGridField

author = 'Your name here'

doc = """
xia
"""


class Constants(BaseConstants):
    name_in_url = 'IFAGPPM1DEU'
    players_per_group = None
    num_rounds = 10

    historical_sales = [206,244,239,211,204,196,214,202,200,201,178,194,169,]
    actual_sales = [159,168,147,143,270,157,139,137,123,124]

    historical_forecast = ['null', 'null', 'null',230,220,212,204,209,206,203,202,190,192,]
    model_forecast = [180,170,169,158,150,147,152,145,141,132,]


    mencast = ['null','null','null','null','null','null','null','null','null','null','null','null','null',]
    historical_axis = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]

    occurence = 5
    product_name = 'IFAG-PPM1DEU'

    instructions_template = 'Now/InstructionsInsert.html'


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

