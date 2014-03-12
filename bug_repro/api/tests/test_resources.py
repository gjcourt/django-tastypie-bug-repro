from django.contrib.auth.models import User
from tastypie.test import ResourceTestCase
from bug_repro.api.views import UserResource


class ApiTest(ResourceTestCase):
    def test_create_forum(self):
	user=User.objects.create(username='gjcourt')
        ur=UserResource()
        resp = self.api_client.post('/api/1/forum/', format='json', data={
            'name': 'Test Forum',
            'members': ['/api/1/user/{0}/'.format(user.id)],
            'moderators': ['/api/1/user/{0}/'.format(user.id)],
        })
        self.assertHttpCreated(resp)
        data = self.deserialize(resp)
        self.assertEqual(len(data['moderators']), 1)
        self.assertEqual(len(data['members']), 1)
