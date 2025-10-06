import sys
import os
sys.path.append(os.getcwd())

from model.high_and_low import HighLowGame
from views.high_and_low_view import run_ui

if __name__ == "__main__":
    run_ui(HighLowGame)
