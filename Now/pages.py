from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1




class PreRound(Page):

    form_model = 'player'
    form_fields = ['initial_forecast',]

    def vars_for_template(self):
        # an axis excluding this round
        x_axis = Constants.historical_axis[:]
        all_axis = [i for i in range(1, Constants.num_rounds + 1)]
        for i in range(1, self.round_number):
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

        briefing.append({
           'name': 'Sales',
           'dashStyle': 'solid',
           'data': saleshistory,
        })



        return {
            'startseries': briefing,
            'the_axis': x_axis,
            # 'initial_forecast_label': 'Please enter your forecast for period {}'.format(self.player.round_number)
        }


class Round(Page):

    # timeout_seconds = 120
    form_model = 'player'
    form_fields = ['forecast_amount',]

    def vars_for_template(self):
        # an axis excluding this round
        x_axis = Constants.historical_axis[:]
        all_axis = [i for i in range(1, Constants.num_rounds + 1)]
        for i in range(1, self.round_number):
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

        briefing.append({
            'name': 'Model forecast',
            'dashStyle': 'shortdot',
            'data': previous_forecast,
        })
        briefing.append({
            'name': 'Sales',
            'dashStyle': 'solid',
            'data': saleshistory,
        })

        return {
            'startseries': briefing,
            'the_axis': x_axis,
            'forecasted': Constants.model_forecast[(self.player.round_number - 1)],
         }

class Results(Page):

    def vars_for_template(self):

        # an axis including this round
        x_axis = Constants.historical_axis[:]
        all_axis = [i for i in range(1, self.round_number + 1)]
        x_axis.extend(all_axis)
        # all_axis = [i for i in range(1, Constants.num_rounds + 1)]
        # for i in range(1, self.round_number + 1):
        #     e = all_axis.pop(0)
        #     f = [e]
        #     x_axis.extend(f)

        briefing = []

        # a series of sales including this round's result
        saleshistory = Constants.historical_sales[:]
        all_sales = Constants.actual_sales[:]
        for i in range(1, self.round_number + 1):
            a = all_sales.pop(0)
            b = [a]
            saleshistory.extend(b)

            # a series of model forecast including this round's result
        previous_forecast = Constants.historical_forecast[:]
        all_forecast = Constants.model_forecast[:]
        for i in range(1, self.round_number + 1):
            c = all_forecast.pop(0)
            d = [c]
            previous_forecast.extend(d)

            # a series of a player's final forecast including this round's result

        human_forecast = Constants.mencast[:]
        human = self.player
        updates = [p.forecast_amount for p in human.in_all_rounds()]
        if updates == None:
            human_forecast
        else:
            human_forecast.extend(updates)

        briefing.append({
            'name': 'Model forecast',
            'dashStyle': 'shortdot',
            'data': previous_forecast,
        })
        briefing.append({
            'name': 'Sales',
            'dashStyle': 'solid',
            'data': saleshistory,
        })
        briefing.append({
            'name': 'Your forecast',
            'dashStyle': 'shortdash',
            'data': human_forecast,
        })

        return {
            'startseries': briefing,
            'the_axis': x_axis,
            'forecasted': Constants.model_forecast[(self.player.round_number - 1)],
            'actual': Constants.actual_sales[(self.player.round_number - 1)],

        }



class ResultsOverview(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        # an axis including this round
        x_axis = Constants.historical_axis[:]
        all_axis = [i for i in range(1, Constants.num_rounds + 1)]
        x_axis.extend(all_axis)

        briefing = []

        # a series of sales including this round's result
        saleshistory = Constants.historical_sales[:]
        all_sales = Constants.actual_sales[:]
        saleshistory.extend(all_sales)

        # a series of model forecast including this round's result
        previous_forecast = Constants.historical_forecast[:]
        all_forecast = Constants.model_forecast[:]
        previous_forecast.extend(all_forecast)

        # a series of a player's final forecast including this round's result

        human_forecast = Constants.mencast[:]
        human = self.player  # this gets always only P1....
        updates = [p.forecast_amount for p in human.in_all_rounds()]
        human_forecast.extend(updates)

        briefing.append({
            'name': 'Model forecast',
            'dashStyle': 'shortdot',
            'data': previous_forecast,
        })
        briefing.append({
            'name': 'Sales',
            'dashStyle': 'solid',
            'data': saleshistory,
        })
        briefing.append({
            'name': 'Your forecast',
            'dashStyle': 'shortdash',
            'data': human_forecast,
        })

        return {
            'startseries': briefing,
            'the_axis': x_axis,
          }


class IU(Page):

    def is_displayed(self):
        if self.round_number == Constants.occurence and self.player.role() == 'treatment':
            return True
        else:
            return False








page_sequence = [
    Instructions,
    PreRound,
    Round,
    Results,
    IU,
    ResultsOverview,

]