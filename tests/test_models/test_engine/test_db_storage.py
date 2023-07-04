import unittest
from models import DBStorage, User

class TestDBStorage(unittest.TestCase):

    def setUp(self):
        """Set up for the DBStorage tests"""
        # You might want to change this to your test database
        self.storage = DBStorage()

    def tearDown(self):
        """Tear down for the DBStorage tests"""
        self.storage.close()

    def test_new(self):
        """Test the new method"""
        # Create a new User
        user = User()
        user.id = "123"
        user.name = "MyName"
        self.storage.new(user)
        self.storage.save()

        # Fetch the user back from the DB
        users = self.storage.all(User)
        self.assertIn("User.123", users)

    def test_delete(self):
        """Test the delete method"""
        user = User()
        user.id = "123"
        user.name = "MyName"
        self.storage.new(user)
        self.storage.save()

        # Now delete the user
        self.storage.delete(user)
        self.storage.save()

        # Fetch the user back from the DB
        users = self.storage.all(User)
        self.assertNotIn("User.123", users)

    def test_all(self):
        """Test the all method"""
        user1 = User()
        user1.id = "123"
        user1.name = "MyName"
        self.storage.new(user1)
        
        user2 = User()
        user2.id = "456"
        user2.name = "AnotherName"
        self.storage.new(user2)

        self.storage.save()

        # Fetch the users back from the DB
        users = self.storage.all(User)
        self.assertIn("User.123", users)
        self.assertIn("User.456", users)

# Run the tests
if __name__ == "__main__":
    unittest.main()