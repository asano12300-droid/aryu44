import os
import shutil
from pathlib import Path

def git_move(ex, to):
    name = os.getlogin()
    shutil.move(ex, to)       