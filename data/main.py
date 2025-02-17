__author__ = 'justinarmstrong'

from . import setup,tools
from .states import main_menu,load_screen,level1,level2
from . import constants as c


def main():
    """Add states to control here."""
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.TIME_OUT: load_screen.TimeOut(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.GAME_CLEAR: load_screen.GameClear(),
                  c.LEVEL1: level1.Level1(),
                  c.LEVEL2: level2.Level2()}

    # main_menu.Menu()를 시작
    run_it.setup_states(state_dict, c.MAIN_MENU)

    # 메인 루프 시작 
    run_it.main()



