import sys
import os.path
sys.path.insert(0, os.path.dirname(__file__))
from dukaan import app as application, init_for
init_for('production')