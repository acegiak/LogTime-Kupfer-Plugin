__kupfer_name__ = _("Logtime")
__kupfer_actions__ = ("Log", )
__description__ = _("Log time into a text file to check later")
__version__ = ""
__author__ = "Ashton McAllan at Brightcookie. Brightcookie.com.au"


import datetime
from kupfer.objects import Action, TextLeaf, OperationError
from kupfer import utils
from kupfer import plugin_support
from kupfer import kupferstring



class Log (Action):
    def __init__(self):
        Action.__init__(self, _("Log"))
    def activate(self, leaf):
        text = leaf.object
        with open("timelog - "+datetime.datetime.now().strftime("%Y-%m-%d")+".txt", "a") as myfile:
            myfile.write(datetime.datetime.now().strftime("%H:%M:%S")+": "+text+"\r\n")

    def item_types(self):
        yield TextLeaf
    def get_description(self):
        return _("Log time into a text file")
    def get_icon_name(self):
        return "time"