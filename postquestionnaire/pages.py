from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender','age','education','experience',]


class Experience(Page):
    form_model = 'player'
    form_fields = ['course','forecasting_years',]

    def is_displayed(self):
        return self.player.experience == True


class Thoughts(Page):
    form_model = 'player'
    form_fields = ['calculator','initial_strategy','final_strategy','final_comment']

class Goodbye(Page):
    pass



page_sequence = [
    Demographics,
    Experience,
    Thoughts,
    Goodbye
]
