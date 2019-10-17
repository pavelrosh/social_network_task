from django.test import TestCase
from . models import Post, User
from rest_framework.test import APIClient
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED
)


class UserPostTest(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create_user(username='testuser1', email='testuser1@mail.com',
                                             password='top_secret')
        self.user2 = User.objects.create_user(username='testuser2', email='testuser2@mail.com',
                                              password='top_secret')
        self.post1 = Post.objects.create(content='First Post of user', user=self.user1)
        self.post2 = Post.objects.create(content='Second Post of user', user=self.user1)
        self.post3 = Post.objects.create(content='First Post of user2', user=self.user2)
        self.post4 = Post.objects.create(content='Second Post of user2', user=self.user2)

        self.client = APIClient()

    def test_get_from_db(self):
        user1 = User.objects.get(username='testuser1')
        user2 = User.objects.get(username='testuser2')

        post1 = Post.objects.filter(user=user1)
        post2 = Post.objects.filter(user=user2)

        self.assertEqual(user1.username, 'testuser1')
        self.assertEqual(user2.username, 'testuser2')

        self.assertEqual(len(post1), 2)
        self.assertEqual(len(post2), 2)

    def test_get_user_response(self):
        response = self.client.post(path='/api/rest-auth/registration/',
                                    data={"username": "testuserPavlo",
                                          "email": "testtest@mail.com",
                                          "password1": "top_secret",
                                          "password2": "top_secret"
                                          })
        self.assertEqual(response.status_code, HTTP_201_CREATED)

        response = self.client.post(path='/api/rest-auth/login/',
                                    data={"username": "testuserPavlo",
                                          "email": "testtest@mail.com",
                                          "password": "top_secret"
                                          })
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_create_post_response(self):
        response = self.client.post(path='/api/post/',
                                    data={
                                        "content": "Hello, some content!",
                                        "likes": 0,
                                    })
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user1)
        response = self.client.post(path='/api/post/',
                                    data={
                                        "content": "Hello, some content!",
                                        "likes": 0,
                                    })
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_like_post_response(self):
        response = self.client.get(path=f'/api/post/like/{self.post1.id}/')
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

        response = self.client.get(path=f'/api/post/unlike/{self.post1.id}/')
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user1)

        response = self.client.get(path=f'/api/post/like/{self.post1.id}/')
        self.assertEqual(response.status_code, HTTP_200_OK)

        response = self.client.get(path=f'/api/post/unlike/{self.post1.id}/')
        self.assertEqual(response.status_code, HTTP_200_OK)
