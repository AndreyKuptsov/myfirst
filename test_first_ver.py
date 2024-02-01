import unittest
from first_ver import main


class TestIPFound(unittest.TestCase):

    def test_from_doc(self):
        self.assertEqual(main("C:\4\ipv4", "4"), "192.168.0.0/23")

    def test_new_data(self):
        self.assertEqual(main("C:\4\ipv41", "4"), "192.168.0.0/25")
        self.assertEqual(main("C:\4\ipv42", "4"), "192.168.0.0/23")
        self.assertEqual(main("C:\4\ipv46", "4"), "0.0.0.0/0")
        self.assertEqual(main("C:\4\ipv48", "4"), "192.168.1.0/27")

    def test_error(self):
        self.assertRaises(ValueError, main, "C:\4\ipv43", "4")
        self.assertRaises(ValueError, main, "C:\4\ipv44", "4")
        self.assertRaises(ValueError, main, "C:\4\ipv45", "4")
        self.assertRaises(ValueError, main, "C:\4\ipv47", "4")


# Import time module
import time

# record start time
start = time.time()

# define a sample code segment
a = 0
for i in range(1000):
	a += (i**100)

# record end time
end = time.time()

# print the difference between start 
# and end time in milli. secs
print("The time of execution of above program is :",
	(end-start) * 10**3, "ms")