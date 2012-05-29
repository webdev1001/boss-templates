
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation
from @module@.hub.api.version0 import auth
from @module@.hub import forms
from @module@.hub import db


class UserResource(ModelResource):
    class Meta:
        authentication = auth.@class_prefix@Authentication
        authorization = auth.@class_prefix@Authorization
        queryset = db.User.objects.all()
        resource_name = 'users'
        excludes = [
            'email',
            'password',
            'is_superuser',
            ]
        methods = ['get']

class ExampleResource(ModelResource):
    class Meta:
        queryset = db.Example.objects.all()
        resource_name = 'example'
        authorization = @class_prefix@Authorization()
        authentication = @class_prefix@Authentication()
        methods = ['get', 'put', 'post', 'delete']
        validation = FormValidation(form_class=forms.ExampleForm)
        
    user = fields.ToOneField(UserResource, 'user', full=True)