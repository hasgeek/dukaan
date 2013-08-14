#! /usr/bin/env python

from coaster.manage import init_manager

from dukaan import app, db, init_for


if __name__ == "__main__":
    manager = init_manager(app, db, init_for)
    manager.run()
