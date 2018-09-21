import graphene
from django import http

from data import models, serializers
from data.graphql_schema.types import UserType
from data.graphql_schema.inputs import UserCreationInput

forbidden_resp = http.HttpResponseForbidden('{"error": "forbidden"}',content_type="application/json")

# creating a user
class CreateUser(graphene.Mutation):

    class Arguments:
        user_data = UserCreationInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    def mutate(self, info, user_data):
        if user_data['usertype'].lower() == 'teacher':
            user = models.User.objects.create(
                username=user_data['username'],
                name=user_data['name'],
                gender=user_data['gender'],
                usertype=user_data['usertype'],
                email=user_data['email'],
                phone=user_data['phone'],
                is_active=False
            )
            if 'bupt_id' in user_data:
                user.bupt_id = user_data['bupt_id']
            if 'class_number' in user_data:
                user.class_number = user_data['class_number']
            user.set_password(user_data['password'])
            user.save()
            ok = True
            return CreateUser(user=user, ok=ok)

        elif user_data['usertype'].lower() == 'assistant':
            user = models.User.objects.create(
                username=user_data['username'],
                name=user_data['name'],
                gender=user_data['gender'],
                usertype=user_data['usertype'],
                email=user_data['email'],
                phone=user_data['phone'],
                is_active=False
            )
            if 'bupt_id' in user_data:
                user.bupt_id = user_data['bupt_id']
            if 'class_number' in user_data:
                user.class_number = user_data['class_number']
            user.set_password(user_data['password'])
            user.save()
            ok = True
            return CreateUser(user=user, ok=ok)

        elif user_data['usertype'].lower() == 'student':
            user = models.User.objects.create(
                username=user_data['username'],
                name=user_data['name'],
                gender=user_data['gender'],
                usertype=user_data['usertype'],
                bupt_id=user_data['bupt_id'],
                class_number=user_data['class_number'],
                email=user_data['email'],
                phone=user_data['phone'],
                is_active=False
            )
            user.set_password(user_data['password'])
            user.save()
            ok = True
            return CreateUser(user=user, ok=ok)
