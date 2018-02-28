from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'postquestionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    gender = models.IntegerField(
        label='1. What is your gender?',
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [0, 'Prefer Not Tell'],
        ],
        widget=widgets.RadioSelect,
    )
    age = models.IntegerField(
        label='2. How old are you?',
        min=0,
        max=80,
        blank=True
    )
    education = models.IntegerField(
        label='3. What is your highest education?',
        choices=[
            [1,'Elementary School'],
            [2,'High School'],
            [3, 'University'],
            [4,'Graduate School or Diplom'],
            [5,'PhD'],
            [6,'Prefer Not Tell']
        ],
        widget=widgets.RadioSelect,
    )

    experience = models.BooleanField(
        label = '4. Have you had any experience in forecasting?',
        choices=[[True, 'Yes'],[False, 'No']
                 ],
        widget=widgets.RadioSelect,
    )
    course = models.IntegerField(
        label='4.1 Where have you gained the experience in forecasting?',
        choices=[[1, 'From university courses'], [2, 'From work'], [3, 'From both']],
        widget=widgets.RadioSelect
    )

    forecasting_years =models.IntegerField(
        label='4.2 How many years of forecasting experience in total do you have?',
        choices=[
            [0,'No experience in forecasting'],
            [1,'Up to 1 year'],
            [2,'1~2 years'],
            [3,'2~5 years'],
            [4,'more than 5 years']
        ],
        widget=widgets.RadioSelect,
    )

    perceived_accuracy = models.IntegerField(
        label='5. In your opinion, how accurate was the model forecast?',
        choices=[
            [1,'Highly inaccurate'],
            [2,'Slightly inaccurate'],
            [3,'Somewhat accurate'],
            [4,'Very accurate'],
        ],
        widget=widgets.RadioSelect
    )
    accepted_accuracy = models.IntegerField(
        label='6. Please enter a value to fill in the blank above.',
        min=0,
        max=100,
    )

    challenge = models.IntegerField(
        label='7. How challenging was the game?',
        choices=[
            [0,'Easy'],
            [1,'Slightly challenging'],
            [2, 'Moderately challenging'],
            [3, 'Very Challenging']
        ],
        widget=widgets.RadioSelect,
    )

    calculator = models.BooleanField(
        choices=[
            [True, 'Yes'],
            [False, 'No']
        ],
        label='8. Did you use a calculator or calculate on a piece of paper?',
        widget=widgets.RadioSelect
    )
    initial_strategy = models.LongStringField(
        label='9. Please describe your strategy for the initial forecast: ',
        blank=True
    )
    final_strategy =models.LongStringField(
        label='10. Please describe your strategy for the final forecast:',
        blank=True
    )
    final_comment = models.LongStringField(
        label='11. Please leave any comment you have regarding the game here.',
        blank=True
    )