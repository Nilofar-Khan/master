import unittest
from programs.program2 import prog2

class TestProg2(unittest.TestCase):
    def test_prog2_func(self):
        obj = prog2("Hello, UST!")
        self.assertEqual(obj.name, "Hello, UST!")  # Verify number is set correctly
        obj.func()  # Run the function to check for errors

if __name__ == "__main__":
    unittest.main()
