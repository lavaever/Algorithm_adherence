from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import csv
import json
from otree.models_concrete import ParticipantToPlayerLookup, RoomToSession
from otree.models.session import Session as BaseSession


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Intro'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'Intro/InstructionsInsert.html'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sequence_of_apps = models.LongStringField()

    aim = models.IntegerField(
        label="What should you aim for in this game?",
        choices=[
            [1, 'Attend to other obligations on my schedule'],
            [2, 'Achieve high forecast accuracy'],
            [3, 'Finish first'],
        ],
        widget=widgets.RadioSelect,
    )

    measurement = models.IntegerField(
        label="What will be taken to measure your forecast accuracy?",
        choices=[
            [1, 'My initial forecast'],
            [2, 'Model forecast'],
            [3, 'My final forecast'],
        ],
        widget=widgets.RadioSelect,
    )

    accuracy = models.IntegerField(
        label="Which one of the following forecast values has the lowest mean absolute error when the actual sales is 100?",
        choices=[
            [1,'150'],
            [2,'101'],
            [3,'50'],
            [4,'30']
        ],
        widget=widgets.RadioSelect,
    )

    def role(self):
        if self.id_in_group % 2 == 0:
            return 'treatment'
        else:
            return 'control'