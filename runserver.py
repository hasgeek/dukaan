#!/usr/bin/env python
import sys
from dukaan import app

try:
    port = int(sys.argv[1])
except (IndexError, ValueError):
    port = 7200
app.run('0.0.0.0', port=port, debug=True)
