import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        # Arrange
        first = 10
        second = 5
        expected = 15
        
        # Act
        result = maths.add(first, second)
        
        #Assert
        self.assertEqual(result, expected)
        
    def test_add_convert_base_2(self):
        ''' Tests the optional base (2) conversion in the add function. '''
        # Arrange
        first = 10
        second = 5
        base = 2
        expected = '1111'
        
        # Act
        result = maths.add(first, second, base)
        
        #Assert
        self.assertEqual(result, expected)
        
    def test_add_convert_base_8(self):
        ''' Tests the optional base (8) conversion in the add function. '''
        # Arrange
        first = 10
        second = 5
        base = 8
        expected = '17'
        
        # Act
        result = maths.add(first, second, base)
        
        #Assert
        self.assertEqual(result, expected)
        
    def test_add_convert_base_16(self):
        ''' Tests the optional base (16) conversion in the add function. '''
        # Arrange
        first = 10
        second = 5
        base = 16
        expected = 'F'
        
        # Act
        result = maths.add(first, second, base)
        
        #Assert
        self.assertEqual(result, expected)
        
    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        # Arrange
        length = 5
        expected = 5
        
        #Act
        result = maths.fibonacci(length)
        
        #Assert
        self.assertEqual(result, expected)
    
    def test_convert_base_2(self):
        ''' Tests the convert_base function for base 2. '''
        #Arrange
        number = 10
        base = 2
        expected = '1010'
        
        #Act
        result = maths.convert_base(number, base)
        
        #Assert
        self.assertEqual(result, expected)
        
    def test_convert_base_8(self):
        ''' Tests the convert_base function for base 8. '''
        #Arrange
        number = 10
        base = 8
        expected = '12'
        
        #Act
        result = maths.convert_base(number, base)
        
        #Assert
        self.assertEqual(result, expected)
        
    def test_convert_base_over_16(self):
        ''' Tests the convert_base function for base 16. '''
        #Arrange
        number = 10
        base = 16
        expected = 'A'
        
        #Act
        result = maths.convert_base(number, base)
        
        #Assert
        self.assertEqual(result, expected)

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
