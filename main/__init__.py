from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'main'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    device = models.StringField()


# PAGES
class MyPage(Page):
    @staticmethod
    def live_method(player, data):
        if data['type'] == 'device':
            player.device = data['device']


class redirect_screenout(Page):
    template_name = '_static/global/redirects/redirect_device.html'

    @staticmethod
    def is_displayed(player: Player):
        return player.device != 'Desktop'


class redirect_screenout2(Page):
    template_name = '_static/global/redirects/redirect_device2.html'

    @staticmethod
    def is_displayed(player: Player):
        return player.device != 'Desktop'

class Results(Page):
    pass


page_sequence = [MyPage, redirect_screenout, redirect_screenout2, Results]
