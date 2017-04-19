from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import requests

__author__ = 'antoni'

LOGGER = getLogger(__name__)


class HistDBSkill(MycroftSkill):

    def __init__(self):
        super(HistDBSkill, self).__init__(name="HistDBSkill")

    def initialize(self):
        history_intent = IntentBuilder("HistoryIntent").require("History").require("Question").build()
        self.register_intent(history_intent, self.handle_history_intent)

    def handle_history_intent(self, message):
        print message.data.get("Question", None)
        r = requests.post('http://13.58.68.155/api/histdb/question', data={'question': message.data.get("Question", None)})
        self.speak(r.json()['answer'])

    def stop(self):
        pass


def create_skill():
    return HistDBSkill()
