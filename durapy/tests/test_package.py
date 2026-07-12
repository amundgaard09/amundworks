import durapy, unittest

from durapy.src.frameworks.phys_dtypes import Quantity, UNITS


class DuraPyPackageTests(unittest.TestCase):
    def test_package_imports_and_exposes_unimath(self):
        from durapy import unimath

        self.assertTrue(callable(unimath.pythagoras))
        self.assertEqual(unimath.pythagoras(A=3, B=4), 5.0)

    def test_constants_are_available_from_top_level_package(self):
        self.assertEqual(durapy.constants.PI.value, 3.141592653589793)

    def test_quantity_can_convert_between_units_of_same_dimension(self):
        distance = Quantity(5, UNITS["m"])
        converted = distance.to(UNITS["cm"])

        self.assertEqual(converted.unit, UNITS["cm"])
        self.assertAlmostEqual(converted.value, 500.0)

    def test_quantity_can_convert_velocity_units(self):
        speed = Quantity(100, UNITS["km/h"])
        converted = speed.to(UNITS["m/s"])

        self.assertAlmostEqual(converted.value, 27.77777777777778)


if __name__ == "__main__":
    unittest.main()
