import unittest     # Import the Python unit testing framework
from logger import Logger        # Our code to test

class LoggerTest(unittest.TestCase):
    ''' Unit tests for our logger functions. '''
    text = ""

    def target(self, text = ""):
        ''' Create a target. '''
        self.text = text
        

    def test_info(self):
        ''' Tests the info function. '''
        # Arrange
        log = Logger(self.target)
        string = "test string"
        expected = "[INFO] {}".format(string)
        
        # Act
        log.info(string)
        
        # Assert
        self.assertEqual(self.text, expected)
    
    def test_error(self):
        ''' Tests the error function. '''
        # Arrange
        log = Logger(self.target)
        string = "test string"
        expected = "[WARNING] {}".format(string)
        
        # Act
        log.error(string)
        
        # Assert
        self.assertEqual(self.text, expected)

# This allows running the unit tests from the command line (python test_logger.py)
if __name__ == '__main__':
    unittest.main()