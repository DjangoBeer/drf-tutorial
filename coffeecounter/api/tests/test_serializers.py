from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Consumption, Badge, PoweredBadge, CoffeeUser
from api.serializers import BadgeSerializer, UserSerializer, ConsumptionSerializer
from rest_framework.renderers import JSONRenderer


class TestSerializers(TestCase):

	def setUp(self):
		self.user_jacob = User.objects.create_user(
			username='jacob', email='jacob@dot.com',
            password='top_secret')
		self.user_perry = User.objects.create_user(
			username='perry', email='perry@dot.com',
            password='top_secret')


	def tearDown(self):
		pass


	def test_badge_serializer_valid(self):
		data = {'pk': 2, 'title': u'Coffee tester', 'description': u'<3 @ 180bpm'}
		serializer = BadgeSerializer(data=data)
		self.assertTrue(serializer.is_valid())


	def test_badge_serializer_not_valid(self):
		data = {'pk': 2, 'tile': u'Coffee tester', 'description': u'<3 @ 180bpm'}
		serializer = BadgeSerializer(data=data)
		self.assertFalse(serializer.is_valid())


	def test_consumption_serializer(self):
		consumption1 = Consumption.objects.create(user=self.user_perry)
		consumption2 = Consumption.objects.create(user=self.user_perry)
		consumption3 = Consumption.objects.create(user=self.user_jacob)

		consumption_serializer1 = ConsumptionSerializer(consumption1)
		consumption_serializer2 = ConsumptionSerializer(consumption2)
		consumption_serializer3 = ConsumptionSerializer(consumption3)

		self.assertEqual(consumption_serializer1.data['user'], self.user_perry.pk)
		self.assertEqual(consumption_serializer2.data['user'], self.user_perry.pk)
		self.assertEqual(consumption_serializer3.data['user'], self.user_jacob.pk)


	def test_badge_serializer(self):
		badge1 = Badge.objects.create(title='Badge 1', description='A lot of coffee')
		badge2 = Badge.objects.create(title='Badge 2', description='Two days w/o coffee')
		badge3 = Badge.objects.create(title='Badge 3', description='Green tea man')

		pwbadge1 = PoweredBadge.objects.create(user=self.user_perry, badge=badge1)
		pwbadge2 = PoweredBadge.objects.create(user=self.user_perry, badge=badge2)
		pwbadge3 = PoweredBadge.objects.create(user=self.user_jacob, badge=badge3, power=2)

		perry_serializer = UserSerializer(self.user_perry)
		jacob_serializer = UserSerializer(self.user_jacob)

		self.assertEqual(len(perry_serializer.data['badges']), 2)
		self.assertEqual(len(jacob_serializer.data['badges']), 1)
		self.assertEqual(jacob_serializer.data['badges'][0]['power'], 2)


	def test_user_serializer(self):
		coffeeuser_perry = CoffeeUser.objects.create(user=self.user_perry, twitter='@perry')

		user_serializer1 = UserSerializer(self.user_perry)
		user_serializer2 = UserSerializer(self.user_jacob)

		self.assertEqual(user_serializer1.data['twitter'], '@perry')
		self.assertEqual(user_serializer2.data['twitter'], None)
