import unittest
from pytiny import PyTiny


class TestMethods(unittest.TestCase):

    def test_search(self):
        db = PyTiny()
        db.set("key", "value")
        self.assertEqual(db.get("key"), "value")

    def test_delete(self):
        db = PyTiny()
        db.set("key", "value")
        db.delete("key")
        self.assertFalse(db.get("key"))

    def test_reset(self):
        db = PyTiny()
        self.assertTrue(db.reset())


if __name__ == '__main__':
    unittest.main()
