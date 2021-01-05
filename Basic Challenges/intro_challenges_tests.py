import intro_challenges
import unittest

class ChallengesTestCase(unittest.TestCase):

    def test_find_range(self):
        self.assertEqual(intro_challenges.find_range([3, 4, 2, 5, 10]), (2, 10))

    def test_fizzbuzz(self):
        self.assertIn('fizzbuzz', intro_challenges.fizzbuzz())
    
    def test_find_longest_word(self):
        self.assertIn('12', intro_challenges.find_longest_word(["Balloonicorn", "Hackbright"]))
    
    def test_decode(self):
        self.assertEqual(intro_challenges.decode("0h1ae2bcy"), 'hey')

if __name__ == '__main__':
    unittest.main()
