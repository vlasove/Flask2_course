import unittest
from app import app, db 
from app.models import User 

class UserTest(unittest.TestCase):
    def setUp(self): #до всех тестов 
        #print("BEFORE TESTS")
        app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite://'
        db.create_all()

    def tearDown(self): #после всех тестов 
        #print("AFTER TESTS")
        db.session.remove()
        db.drop_all()

    def test_set_password_hash(self):
        user1 = User(username='testuser', email='testuser@user')
        pass_user1 = 'testuser'
        user1.set_password(pass_user1)

        self.assertTrue( user1.check_password(pass_user1))
        self.assertFalse(user1.check_password('abcdefg'))


        user2 = User(username='testuser2', email='testuser2@mail')
        pass_user2 = ''
        user2.set_password(pass_user2)

        self.assertTrue( user2.check_password(pass_user2))
        self.assertFalse(user2.check_password(' '))

        user3 = User(username='testuser3', email='testuser3@mail')
        pass_user3 = '@@###12314"saud108951241212312#;;$$'
        user3.set_password(pass_user3)

        self.assertTrue( user3.check_password(pass_user3))
        self.assertFalse(user3.check_password('@@@'))


        user4 = User(username='testuser4', email='testuser4@mail')
        pass_user4 = 'мой пароль'
        user4.set_password(pass_user4)

        self.assertTrue( user4.check_password(pass_user4))
        self.assertFalse(user4.check_password('твой пароль'))

    def test_chech_password(self):
        user1 = User(username='testuser', email='testuser@user')
        pass_user1 = 'testuser'
        user1.set_password(pass_user1)

        db.session.add(user1)
        db.session.commit()

        alt_user = User.query.filter_by(username=user1.username).first()

        self.assertTrue( alt_user.check_password(pass_user1))
        self.assertFalse(alt_user.check_password('abcdefg'))

        user2 = User(username='testuser2', email='testuser2@user')
        pass_user2 = ''
        user2.set_password(pass_user2)

        db.session.add(user2)
        db.session.commit()

        alt_user2 = User.query.filter_by(username=user2.username).first()

        self.assertTrue( alt_user2.check_password(pass_user2))
        self.assertFalse(alt_user2.check_password(' '))

    def test_avatar(self):
        user1 = User(username='testuser', email='testuser@user')
        self.assertEqual(user1.avatar(256)[-3:] ,'256')

        user2 = User(username='testuser2', email='testuser@user')
        self.assertEqual(user2.avatar(60)[-2:] ,'60')
        self.assertNotEqual(user2.avatar(60)[-2:], '100')


    def test_follow(self):
        user1 = User(username='testuser4', email='testuser4@user')
        user2 = User(username='testuser5', email='testuser5@user')

        db.session.add(user1)
        db.session.add(user2)
        

        user1.follow(user2)
        db.session.commit()

        self.assertTrue(user1.is_following(user2))
        self.assertFalse(user2.is_following(user1))



    def test_unfollow(self):
        pass 

    def test_is_following(self):
        pass 
        




if __name__ == "__main__":
    unittest.main()

