from datetime import datetime

import graphene
from django import http

from data import models, serializers
from data.user_views import token
from data import encrypt
from data.graphql_schema.types import SubmissionType
from data.graphql_schema.inputs import SubmissionCreationInput

from data.graphql_schema import except_resp as Exresp

# creating a submission
class CreateSubmission(graphene.Mutation):

    class Arguments:
        submission_data = SubmissionCreationInput(required=True)
    
    ok = graphene.Boolean()
    submission = graphene.Field(SubmissionType)

    def mutate(self, info, submission_data):

        # id validation
        try:
            realuser = token.confirm_validate_token(info.context.META['HTTP_TOKEN'])
            realuser = models.User.objects.get(username=realuser)
        except:
            try:
                realuser = models.User.objects.get(wechat=encrypt.getHash(info.context.META['HTTP_TOKEN']))
            except:
                return Exresp.forbidden_resp
        
        # type validation
        if 'addfile' in submission_data:
            if models.HWFAssignment.objects.get(pk=submission_data['assignment']).type == 'image':
                return Exresp.invalid_type_resp

        # time validation
        if datetime.now() > models.HWFAssignment.objects.get(pk=submission_data['assignment']).deadline.replace(tzinfo=None):
            return Exresp.deadline_expired_resp
        
        viewing_course = models.HWFAssignment.objects.get(pk=submission_data['assignment']).course_class

        # is authentic student
        if len(viewing_course.students.filter(pk=realuser.pk)) == 0:
            return Exresp.forbidden_resp
        
        # field supplement
        submission_data['submitter'] = realuser.pk

        serial = serializers.HWFSubmissionSerializer(data=submission_data)
        if serial.is_valid():
            new_submission = serial.save()
            return CreateSubmission(ok=True, submission=new_submission)