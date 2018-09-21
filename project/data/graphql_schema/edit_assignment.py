import graphene
from django import http

from data import models, serializers
from data.user_views import token
from data import encrypt
from data.graphql_schema.types import AssignmentType
from data.graphql_schema.inputs import AssignmentEditionInput

forbidden_resp = http.HttpResponseForbidden('{"error": "forbidden"}',content_type="application/json")

# editing an assignment
class EditAssignment(graphene.Mutation):

    class Arguments:
        assignment_data = AssignmentEditionInput(required=True)

    ok = graphene.Boolean()
    assignment = graphene.Field(AssignmentType)

    def mutate(self, info, assignment_data):

        try:
            realuser = token.confirm_validate_token(info.context.META['HTTP_TOKEN'])
            realuser = models.User.objects.get(username=realuser)
            editing_assignment = models.HWFAssignment.objects.get(pk=assignment_data['id'])
        except:
            try:
                realuser = models.User.objects.get(wechat=encrypt.getHash(info.context.META['HTTP_TOKEN']))
                editing_assignment = models.HWFAssignment.objects.get(pk=assignment_data['id'])
            except:
                return forbidden_resp

        if len(editing_assignment.course_class.teachers.filter(pk=realuser.id)) == 0 or len(editing_assignment.course_class.teaching_assistants.filter(pk=realuser.id)) == 0:
            return forbidden_resp
        else:
            if 'name' in assignment_data:
                editing_assignment.name = assignment_data['name']
            if 'description' in assignment_data:
                editing_assignment.description = assignment_data['description']
            if 'addfile' in assignment_data:
                for file_id in assignment_data['addfile']:
                    editing_assignment.addfile.add(models.HWFFile.objects.get(pk=file))
            if 'deadline' in assignment_data:
                editing_assignment.deadline = assignment_data['deadline']
            editing_assignment.save()
            return EditAssignmento(ok=True, assignment=editing_assignment)
