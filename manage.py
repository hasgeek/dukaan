#!/usr/bin/env python

from coaster.manage import init_manager

from dukaan import app, db


if __name__ == "__main__":
    manager = init_manager(app, db)
    manager.run()
