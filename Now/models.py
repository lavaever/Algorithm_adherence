from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'IFAGPPM1DEU'
    players_per_group = None
    num_rounds = 10

    historical_sales = [213,199,178,190,171,169,193,171,167,150,164,143,149,]
    actual_sales = [133,127,133,112,234,107,110,118,115,100,]

    historical_forecast = ['null', 'null', 'null',197,193,182,176,184,178,172,161,163,153,]
    model_forecast = [151,142,134,134,123,117,112,111,115,115,]


    mencast = ['null','null','null','null','null','null','null','null','null','null','null','null','null',]
    historical_axis = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]

    occurence = 5
    product_name = 'IFAG-PPM1DEU'



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    initial_forecast = models.IntegerField(min=0, label=False)
    forecast_amount = models.IntegerField(min=0, label=False)

    def role(self):
        if self.id_in_group % 2 == 0:
            return 'treatment'
        else:
            return 'control'

