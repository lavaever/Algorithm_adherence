from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
from ._builtin import Page, WaitPage
import json
import random
from random import sample, choice
from itertools import groupby
from otree.models_concrete import ParticipantToPlayerLookup, RoomToSession
from otree.common_internal import (
    random_chars_8, random_chars_10, get_admin_secret_code, get_app_label_from_name
)
import otree.common_internal
from django.core.urlresolvers import reverse

def get_new_sequence_of_apps(app_sequence):
    the_rest = app_sequence[1:4]
    random.shuffle(the_rest)
    app_sequence = [app_sequence[0]] + the_rest + [app_sequence[4]]
    return app_sequence

def get_players(participant, app_sequence):
    lst = []
    print('NEW APP SEQ::', app_sequence)
    for app in app_sequence:
        models_module = otree.common_internal.get_models_module(app)
        players = models_module.Player.objects.filter(
            participant=participant
        ).order_by('round_number')
        lst.extend(list(players))
    return lst

def build_participant_to_player_lookup(participant, subsession_app_names):
    views_modules = {}
    for app_name in subsession_app_names:
        views_modules[app_name] = (
            otree.common_internal.get_views_module(app_name)
        )

    def views_modules_for_players(player):
        return views_modules[player._meta.app_config.name]

    records_to_create = []

    page_index = 0
    for player in get_players(participant, subsession_app_names):
        for View in views_modules_for_players(player).page_sequence:
            page_index += 1
            records_to_create.append(
                ParticipantToPlayerLookup(
                    participant=participant,
                    page_index=page_index,
                    app_name=player._meta.app_config.name,
                    player_pk=player.pk,
                    session_pk=player.session.pk,
                    subsession_pk=player.subsession.pk,
                    url=reverse(View.url_name(),
                                args=[participant.code,page_index])
                )
            )
        participant._max_page_index = page_index
        participant.save()
    ParticipantToPlayerLookup.objects.bulk_create(records_to_create)

class Instructions(Page):
    def is_displayed(self):
        print('OLD APP SEQ', self.participant.session.config['app_sequence'])
        if not self.player.sequence_of_apps:
            print('SETTING A NEW RANDOM SEQUENCE...')
            ParticipantToPlayerLookup.objects.filter(participant=self.participant).delete()
            self.player.sequence_of_apps = get_new_sequence_of_apps(self.session.config['app_sequence'])
            build_participant_to_player_lookup(self.participant,self.player.sequence_of_apps)
        return True

class Understanding1(Page):
    form_model = 'player'
    form_fields = ['aim']
    def aim_error_message(self, choice):
        if choice != 2:
            return 'Please study the instructions carefully and enter a valid answer.'

class Understanding2(Page):
    form_model = 'player'
    form_fields = ['measurement']
    def measurement_error_message(self, choice):
        if choice != 3:
            return 'Please study the instructions below carefully and enter a valid answer.'

class Understanding3(Page):
    form_model = 'player'
    form_fields = ['accuracy']
    def accuracy_error_message(self, choice):
        if choice !=2:
            return 'Please study the instructions below carefully and enter a valid answer.'

class Wait(Page):
    pass

page_sequence = [
    Instructions,
    Understanding1,
    Understanding2,
    Understanding3,
    Wait,
]
