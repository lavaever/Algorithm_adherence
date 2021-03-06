from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from radiogrid import RadioGridField


author = 'Your name here'

doc = """
shang
"""


class Constants(BaseConstants):
    name_in_url = 'IFAGCMD2INT'
    players_per_group = None
    num_rounds = 10

    historical_sales = [246,249,231,262,270,256,269,288,259,302,324,295,286,]
    actual_sales = [334,348,303,175,341,337,335,336,323,377,]

    historical_forecast = ['null', 'null', 'null',242,252,261,258,264,276,267,285,304,300,]
    model_forecast = [293,313,331,317,310,325,331,333,335,329]

    mencast = ['null','null','null','null','null','null','null','null','null','null','null','null','null',]
    historical_axis = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]

    occurence = 4
    product_name = 'IFAG-CMD2INT'

    instructions_template = 'Real/InstructionsInsert.html'



class Subsession(BaseSubsession):
    pass
    """def vars_for_admin_report(self):

        # create a chart with historical sales and FCST in all previous round

            # an axis excluding this round
        x_axis = Constants.historical_axis[:]
        all_axis = [i for i in range(1, Constants.num_rounds + 1)]
        for i in range(1,self.round_number):
            e = all_axis.pop(0)
            f = [e]
            x_axis.extend(f)

        briefing = []

            # a series of sales excluding this round's result
        saleshistory = Constants.historical_sales[:]
        all_sales = Constants.actual_sales[:]
        for i in range(1, self.round_number):
            a = all_sales.pop(0)
            b = [a]
            saleshistory.extend(b)

            # a series of model forecast excluding this round's result
        previous_forecast = Constants.historical_forecast[:]
        all_forecast = Constants.model_forecast[:]
        for i in range(1, self.round_number):
            c = all_forecast.pop(0)
            d = [c]
            previous_forecast.extend(d)

            # a series of a player's final forecast excluding this round's result

        human_forecast = ['null','null','null',]
        human = self.get_players()[0] #this gets always only P1....
        updates = [p.forecast_amount for p in human.in_previous_rounds()]
        if updates == None:
            human_forecast
        else:
            human_forecast.extend(updates)


        briefing.append({
            'name': 'Model forecast',
            'dashStyle':'shortdot',
            'data': previous_forecast,
        })
        briefing.append({
            'name': 'Sales',
            'dashStyle':'solid',
            'data': saleshistory,
        })
        briefing.append({
            'name': 'Your forecast',
            'dashStyle':'shortdash',
            'data':human_forecast,
        })

        # series.append({
        #     'name': 'Your forecast',
        #     'data': forecasted_sales})
            # 'data': forecast_overview
        # })
        # series.append({
        #     'name': 'Actual Sales',
        #     'data': sales_overview
        # })







        return {
                # 'highchartseries': series,
                # 'round_numbers': result_axis,
                'startseries': briefing,
                'the_axis': x_axis,
        }"""


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

