#!/usr/bin/env python3


import unittest
import logging

import ecks3


logging.basicConfig(level=logging.FATAL)


class TestEcks(unittest.TestCase):
    def test_plugins_with_responding_host(self):
        e = ecks3.Ecks(timeout=5)
        for plugin in e.plugins:
            data = e.get_data("localhost", 161, "public", plugin)
            self.assertTrue(data)

    def test_plugins_with_unresponding_host(self):
        e = ecks3.Ecks(timeout=5)
        for plugin in e.plugins:
            data = e.get_data("localhost", 161, "private", plugin)
            self.assertTrue(not data)

    def test_plugins_with_unreachable_host(self):
        e = ecks3.Ecks(timeout=5)
        for plugin in e.plugins:
            data = e.get_data("127.1.1.1", 161, "public", plugin)
            self.assertTrue(not data)


if __name__ == '__main__':
    unittest.main()
