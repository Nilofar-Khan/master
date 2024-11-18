import unittest
from programs.program1 import prog1

class TestProg1(unittest.TestCase):
    def test_prog1_func(self):
        obj = prog1("Hello, World!")
        self.assertEqual(obj.name, "Hello, World!")  # Verify name is set correctly
        obj.func()  # Run the function to check for errors

if __name__ == "__main__":
    unittest.main()
