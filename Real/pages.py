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
           'color':'#000000',
           'dashStyle': 'solid',
           'data': saleshistory,
        })

        return {
            'startseries': briefing,
            'the_axis': x_axis,
        }


class Round(Page):

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

        human_forecast = Constants.mencast[:]
        human = self.player
        updates = [p.forecast_amount for p in human.in_previous_rounds()]
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
            # 'forecast_amount_label': 'Enter your forecast for sales in period {}:'.format(self.player.round_number),
        }

class Results(Page):

    def vars_for_template(self):
        return ({
                'forecasted': Constants.model_forecast[(self.player.round_number - 1)],
                'actual': Constants.actual_sales[(self.player.round_number - 1)],
            })
    # def vars_for_template(self):
    #     common = self.subsession.vars_for_admin_report()
    #     if True:
    #         common.update({
    #             'actual': Constants.actual_sales[(self.player.round_number - 1)],
    #         })
    #     return common


class ResultsOverview(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        # an axis including this round
        x_axis = Constants.historical_axis[:]
        all_axis = [i for i in range(1, Constants.num_rounds + 1)]
        x_axis.extend(all_axis)

        briefing = []

        # entire sales history
        saleshistory = Constants.historical_sales[:]
        all_sales = Constants.actual_sales[:]
        saleshistory.extend(all_sales)
            # including results of current round
        # saleshistory = Constants.historical_sales[:]
        # all_sales = Constants.actual_sales[:]
        # for i in range(1, self.round_number + 1):
        #     a = all_sales.pop(0)
        #     b = [a]
        #     saleshistory.extend(b)

        # entire model forecast history
        previous_forecast = Constants.historical_forecast[:]
        all_forecast = Constants.model_forecast[:]
        previous_forecast.extend(all_forecast)
            # a series of model forecast including this round's result
        # previous_forecast = Constants.historical_forecast[:]
        # all_forecast = Constants.model_forecast[:]
        # for i in range(1, self.round_number + 1):
        #     c = all_forecast.pop(0)
        #     d = [c]
        #     previous_forecast.extend(d)


        # a series of a player's final forecast including this round's result

        human_forecast = Constants.mencast[:]
        human = self.player
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

class Evaluation1(Page):

    form_model = 'player'
    form_fields = ['self_evaluation']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class Evaluation2(Page):

    form_model = 'player'
    form_fields = ['task_challenge']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds



class MAE(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        forecaster = self.player
        # calculate MAE Final Forecast and round it to 1 digit
        mencast_sum = 0
        mencast_list = [p.forecast_amount for p in forecaster.in_all_rounds()]
        for i in range(Constants.num_rounds):
            ae = abs(mencast_list[i]-Constants.actual_sales[i])
            mencast_sum += ae
        raw_mencast_mae = mencast_sum/Constants.num_rounds
        mencast_mae = round(raw_mencast_mae, 1)

        # calculate MAE Model Forecast and round it to 1 digit
        modelcast_sum =0
        for i in range(Constants.num_rounds):
            model_ae = abs(Constants.model_forecast[i]-Constants.actual_sales[i])
            modelcast_sum += model_ae
        raw_modelcast_mae = modelcast_sum/Constants.num_rounds
        modelcast_mae = round(raw_modelcast_mae, 1)

        return {
            'mencast_mae':mencast_mae,
            'modelcast_mae':modelcast_mae
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
    Evaluation1,
    Evaluation2,
    MAE,
]
