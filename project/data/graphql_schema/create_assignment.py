import graphene
from django import http

from data import models, serializers
from data.user_views import token
from data import encrypt
from data.graphql_schema.types import AssignmentType
from data.graphql_schema.inputs import AssignmentCreationInput

forbidden_resp = http.HttpResponseForbidden('{"error": "forbidden"}',content_type="application/json")


# creating an assignment
class CreateAssignment(graphene.Mutation):

    class Arguments:
        assignment_data = AssignmentCreationInput(required=True)

    ok = graphene.Boolean()
    assignment = graphene.Field(AssignmentType)

    def mutate(self, info, assignment_data):

        if settings.DEBUG == True:
            serial = serializers.HWFAssignmentSerializer(data=assignment_data)
            if serial.is_valid():
                new_assignment = serial.save()
            return CreateAssignment(ok=True, assignment=new_assignment)

        try:
            realuser = token.confirm_validate_token(info.context.META['HTTP_TOKEN'])
            realuser = models.User.objects.get(username=realuser)
        except:
            try:
                realuser = models.User.objects.get(wechat=encrypt.getHash(info.context.META['HTTP_TOKEN']))
            except:
                return forbidden_resp

        if realuser.usertype.lower() == 'teacher':
            serial = serializers.HWFAssignmentSerializer(data=assignment_data)
            if serial.is_valid():
                new_assignment = serial.save()
            return CreateAssignment(ok=True, assignment=new_assignment)
        else:
            return http.HttpResponseForbidden('{"error":"you are not a teacher"}', content_type="application/json")
