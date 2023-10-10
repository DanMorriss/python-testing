import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


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
    
    
    def test_apply_extension(self):
        print('test_apply_extension')
        old_end_date = self.student.end_date
        self.student.apply_extension(20)
        
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=20))


    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")
    
    
    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")

if __name__ == '__main__':
    unittest.main()