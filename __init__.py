from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'antoni'

LOGGER = getLogger(__name__)


class HistDBSkill(MycroftSkill):

    def __init__(self):
        super(HistDBSkill, self).__init__(name="HistDBSkill")

    def initialize(self):
        history_intent = IntentBuilder("HistoryIntent").require("history").optionally("history.re").build()
        self.register_intent(history_intent, self.handle_history_intent)

    def handle_history_intent(self, message):
        print message.data.get("Question", None)
        self.speak_dialog("welcome")

    def stop(self):
        pass


def create_skill():
    return HistDBSkill()
