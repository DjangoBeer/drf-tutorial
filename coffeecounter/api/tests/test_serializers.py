from django.test import TestCase
from api.serializers import BadgeSerializer

class TestSerializers(TestCase):

	def setUp(self):
		pass

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