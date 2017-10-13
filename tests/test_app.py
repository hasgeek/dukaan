# -*- coding: utf-8 -*-

import unittest
from dukaan import app, db
from .fixtures import make_fixtures


class DukaanTestCase(unittest.TestCase):
    app = app

    def setUp(self):
        self.ctx = self.app.test_request_context()
        self.ctx.push()
        db.create_all()
        self.app = app.test_client()
        self.db = db

        make_fixtures()

    def test_noop(self):
        pass

    def tearDown(self):
        self.db.drop_all()
