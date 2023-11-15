import unittest
from app import app, check_requirement, check_if_is_list

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<input type="text" id="Input" name="Input" ', response.data)


    def test_check_requirement(self):
        # Test the check_requirement function
        self.assertTrue(check_requirement('correctLength'))
        self.assertFalse(check_requirement('short'))

    def test_check_if_is_list(self):
        # Test the check_if_is_list function
        self.assertTrue(check_if_is_list('password'))
        self.assertFalse(check_if_is_list('enhpj509yu9308h'))

if __name__ == '__main__':
    unittest.main()

