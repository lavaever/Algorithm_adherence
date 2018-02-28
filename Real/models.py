from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'IFAGCMD2INT'
    players_per_group = None
    num_rounds = 10

    historical_sales = [228,204,230,221,210,210,197,213,220,202,229,217,226,]
    actual_sales = [223,208,234,104,233,212,196,206,195,200,]

    historical_forecast = ['null', 'null', 'null',221,221,215,213,205,209,214,208,219,218,]
    model_forecast = [222,222,215,225,229,231,222,209,207,201,]

    mencast = ['null','null','null','null','null','null','null','null','null','null','null','null','null',]
    historical_axis = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]

    occurence = 5
    product_name = 'IFAG-CMD2INT'



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


class Player(BasePlayer):

    initial_forecast = models.IntegerField(min=0, label=False)
    forecast_amount = models.IntegerField(min=0, label=False)

    def role(self):
        if self.id_in_group % 2 == 0:
            return 'treatment'
        else:
            return 'control'

