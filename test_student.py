import unittest
from student import Student

class TestStudent(unittest.TestCase):
    
    #runs before testing and tests, this is a class method not for the instance of a class
    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    
    
    #runs after testing, again a class method
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
    
    
    # runs before each test
    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')


    #runs after each test
    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')
    
    
    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
        
        self.assertTrue(self.student.naughty_list)
    
    
    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')


if __name__ == '__main__':
    unittest.main()