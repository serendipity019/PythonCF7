import unittest
import test

def main():
    """Main function to run the unit tests."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(test.TestApp)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result

if __name__ == '__main__':
    main()