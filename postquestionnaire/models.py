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
        ],
        widget=widgets.RadioSelect,
    )
    age = models.IntegerField(
        label='2. How old are you?',
        min=0,
        max=80,
    )
    education = models.IntegerField(
        label='3. What is your highest education?',
        choices=[
            [1,"Highschool (ex. Abitur)"],
            [2,"Apprenticeship (ex. Ausbildung)"],
            [3,"Bachelor's degree or equivalent (ex. Diplom)"],
            [4,"Master's degree or equivalent (ex. Magister, MBA)"],
            [5,'PhD or above'],
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
        choices=[[1, 'From courses and trainings'], [2, 'From work'], [3, 'From both']],
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

    calculator = models.BooleanField(
        choices=[
            [True, 'Yes'],
            [False, 'No']
        ],
        label='5. Did you use a calculator or calculate on a piece of paper?',
        widget=widgets.RadioSelect
    )
    initial_strategy = models.LongStringField(
        label='6. How did you come up with the initial forecast? Please briefly describe your strategy.',
    )
    final_strategy =models.LongStringField(
        label='7. How did you come up with the final forecast? Please briefly describe your strategy.',
    )
    final_comment = models.LongStringField(
        label='8. Please leave any comment you have regarding the game.',
    )