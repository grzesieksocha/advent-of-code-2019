from unittest import TestCase
from day_3.distance_measure import path_creator, find_intersections_for, get_min_distance_from_center_for_points


class DistanceMeasureTestCase(TestCase):
    def test_path_creator_third_point(self):
        self.assertEqual((158, -30), path_creator(['R75', 'D30', 'R83'])[-1])
        self.assertEqual((66, 117), path_creator(['U62', 'R66', 'U55'])[-1])
        self.assertEqual((124, 47), path_creator(['R98', 'U47', 'R26'])[-1])
        self.assertEqual((91, 78), path_creator(['U98', 'R91', 'D20'])[-1])

    def test_intersections_finder(self):
        self.assertEqual(
            {(3, 3), (6, 5)},
            find_intersections_for(
                path_creator(['R8', 'U5', 'L5', 'D3']),
                path_creator(['U7', 'R6', 'D4', 'L4'])
            )
        )

    def test_distance_measure(self):
        self.assertEqual(6, get_min_distance_from_center_for_points({(3, 3), (6, 5)}))
        self.assertEqual(6, get_min_distance_from_center_for_points({(6, 5), (3, 3)}))
        self.assertEqual(10, get_min_distance_from_center_for_points({(-5, -5)}))
        self.assertEqual(10, get_min_distance_from_center_for_points({(-5, 5)}))
        self.assertEqual(10, get_min_distance_from_center_for_points({(5, -5)}))

    def test_system(self):
        self.assertEqual(
            6,
            get_min_distance_from_center_for_points(
                find_intersections_for(
                    path_creator(['R8', 'U5', 'L5', 'D3']),
                    path_creator(['U7', 'R6', 'D4', 'L4'])
                )
            )
        )
