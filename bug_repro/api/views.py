from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from bug_repro.api.models import Forum


class UserResource(ModelResource):
    class Meta:
        authorization = Authorization()
        queryset = User.objects.all()
        resource_name = 'user'


class ForumResource(ModelResource):
    moderators = fields.ManyToManyField(UserResource, 'moderators', full=True)
    members = fields.ManyToManyField(UserResource, 'members', full=True)

    class Meta:
        authorization = Authorization()
        queryset = Forum.objects.all()
        resource_name = 'forum'
        always_return_data = True
