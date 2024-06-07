import sys
sys.dont_write_bytecode = True

from app.Waves.waves import Waves
from app.app import App
from app.Conf.conf import *
from app.Entity.allyTeam import *
from app.menu import *
import time

# init
menu = Menu()

while True:
    # Start menu
    menu.runMenu()
