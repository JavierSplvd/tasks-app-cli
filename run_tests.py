import unittest
import sys, os

if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(__file__))
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("src", pattern="test_*.py")
    unittest.TextTestRunner().run(test_suite)
