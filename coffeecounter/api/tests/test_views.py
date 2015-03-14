from django.test import TestCase, Client
from django.contrib.auth.models import User
from api.models import Consumption, Badge, PoweredBadge, CoffeeUser
from api.serializers import BadgeSerializer, UserSerializer, ConsumptionSerializer
from rest_framework.renderers import JSONRenderer
import json

class TestViews(TestCase):

    def setUp(self):
        self.user_jacob = User.objects.create_user(
            username='jacob', email='jacob@dot.com',
            password='top_secret')
        self.user_perry = User.objects.create_user(
            username='perry', email='perry@dot.com',
            password='top_secret')
        self.client = Client()

    def tearDown(self):
        pass

    def test_post_badge(self):
        self.client.login(username='jacob', password='top_secret')
        json_badge = {
            'title': 'A lot of coffee',
            'description': 'Description'
        }
        response = self.client.post(
            '/badges/', json.dumps(json_badge),
            content_type="application/json"
        )
        self.assertEqual(response.data['title'], 'A lot of coffee')
        badges = Badge.objects.all()
        self.assertEqual(len(badges), 1)

    def test_get_badge(self):
        Badge.objects.create(pk=1, title='A lot of coffee', description='Description')
        self.client.login(username='jacob', password='top_secret')
        response = self.client.get(
            '/badges/1',
            content_type="application/json"
        )
        self.assertEqual(response.data['title'], 'A lot of coffee')

    def test_get_badges(self):
        Badge.objects.create(pk=1, title='A lot of coffee', description='Description 1')
        Badge.objects.create(pk=2, title='Two days w/o coffee', description='Description 2')
        Badge.objects.create(pk=3, title='Green tea man', description='Description 3')

        self.client.login(username='jacob', password='top_secret')
        response = self.client.get(
            '/badges/',
            content_type="application/json"
        )
        self.assertEqual(len(response.data), 3)

    def test_put_badge(self):
        self.client.login(username='jacob', password='top_secret')
        Badge.objects.create(pk=1, title='A lot of coffee', description='Description 1')
        json_badge = {
            'title': 'A lot of strong coffee',
            'description': 'Description'
        }
        response = self.client.put(
            '/badges/1', json.dumps(json_badge),
            content_type="application/json"
        )
        self.assertEqual(response.data['title'], 'A lot of strong coffee')
        badges = Badge.objects.all()
        self.assertEqual(len(badges), 1)

    def test_patch_badge(self):
        self.client.login(username='jacob', password='top_secret')
        Badge.objects.create(pk=1, title='A lot of coffee', description='Description 1')
        json_badge = {
            'title': 'A lot of strong coffee',
        }
        response = self.client.patch(
            '/badges/1', json.dumps(json_badge),
            content_type="application/json"
        )
        self.assertEqual(response.data['title'], 'A lot of strong coffee')
        badges = Badge.objects.all()
        self.assertEqual(len(badges), 1)

    def test_delete_badge(self):
        Badge.objects.create(pk=1, title='Green tea man', description='Description')

        self.client.login(username='jacob', password='top_secret')
        response = self.client.delete(
            '/badges/1',
            content_type="application/json"
        )
        self.assertEqual(len(Badge.objects.all()), 0)