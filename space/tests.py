from urllib import request
from django.test import TestCase
from space.models.spacemodel import SpaceModel
from django.contrib.auth.models import User


class ModelTesting(TestCase):

    def setUp(self):
        a=User.objects.create_user("test2")
        self.space = Space.objects.create(title="test1", author =a, content="test3", created_date="test4", slug="test5")

    def test_post_model(self):
        data=self.space
        self.assertTrue(isinstance(data, Space))
        self.assertEqual(str(data), "test1")
