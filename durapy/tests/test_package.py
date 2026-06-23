import durapy, unittest

class DuraPyPackageTests(unittest.TestCase):
    def test_package_imports_and_exposes_unimath(self):
        from durapy import unimath

        self.assertTrue(callable(unimath.pythagoras))
        self.assertEqual(unimath.pythagoras(A=3, B=4), 5.0)

    def test_constants_are_available_from_top_level_package(self):
        self.assertEqual(durapy.constants.PI.value, 3.141592653589793)


if __name__ == "__main__":
    unittest.main()
