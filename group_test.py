import unittest

from group import Group, getAvailablePairs, getRatingGames
from pair import Pair


class MyTestCase(unittest.TestCase):
    def test_should_get_all_pairs(self):
        expected_pairs = [Pair('A', 'B'), Pair('B', 'C'), Pair('A', 'C')]
        actual_pairs = Group('A', 'B', 'C').allPairs()

        self.assertEqual(len(expected_pairs), len(actual_pairs))
        for expected in expected_pairs:
            self.assertIn(expected, actual_pairs)

    def test_get_available_pairs_simple(self):
        pairs = getAvailablePairs(Group('A', 'D', 'E'), [Pair('D', 'A'), Pair('E', 'D')])
        self.assertEqual(len(pairs), 1)
        self.assertIn(Pair('A', 'E'), pairs)

    def test_get_available_pairs(self):
        pairs = getAvailablePairs(Group('A', 'B', 'D', 'E'), [Pair('D', 'A'), Pair('E', 'D')])
        self.assertEqual(len(pairs), 4)
        self.assertIn(Pair('A', 'E'), pairs)
        self.assertIn(Pair('A', 'B'), pairs)
        self.assertIn(Pair('B', 'D'), pairs)
        self.assertIn(Pair('B', 'E'), pairs)

    def test_get_rating_games(self):
        group = Group('A', 'B', 'D', 'E')
        excluded_pairs = [Pair('A', 'D'), Pair('D', 'E')]
        available_players = ['B', 'D', 'A']
        rating_games = getRatingGames(group, excluded_pairs, available_players)
        print(rating_games)
        self.assertEqual(len(rating_games), 1)
        self.assertNotIn(rating_games[0], excluded_pairs)
        self.assertIn(rating_games[0], getAvailablePairs(group, excluded_pairs))


if __name__ == '__main__':
    unittest.main()
