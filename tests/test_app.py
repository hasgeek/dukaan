# -*- coding: utf-8 -*-

import unittest
from dukaan import app, db, init_for
from .fixtures import make_fixtures


class DukaanTestCase(unittest.TestCase):
    def setUp(self):
        init_for('testing')
        app.config['TESTING'] = True
        db.create_all()
        self.app = app.test_client()
        self.db = db

        make_fixtures()

    def test_noop(self):
        pass

    def tearDown(self):
        self.db.drop_all()
