from unittest import TestCase
from day_6.orbiter import count_orbits


class OrbiterTestCase(TestCase):
    def test_counter(self):
        self.assertEqual(
            42,
            count_orbits(['K)L', 'COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K'])
        )

    def test_counter_with_mixed_order(self):
        self.assertEqual(
            3,
            count_orbits(['K)L', 'J)K'])
        )
