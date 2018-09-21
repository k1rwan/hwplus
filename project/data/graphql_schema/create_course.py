import graphene
from django import http

from data import models, serializers
from data.user_views import token
from data import encrypt
from data.graphql_schema.types import CourseType
from data.graphql_schema.inputs import CourseCreationInput

forbidden_resp = http.HttpResponseForbidden('{"error": "forbidden"}',content_type="application/json")

# creating a course
class CreateCourse(graphene.Mutation):

    class Arguments:
        course_data = CourseCreationInput(required=True)

    ok = graphene.Boolean()
    course = graphene.Field(CourseType)

    def mutate(self, info, course_data):
        
        try:
            realuser = token.confirm_validate_token(info.context.META['HTTP_TOKEN'])
            realuser = models.User.objects.get(username=realuser)
        except:
            try:
                realuser = models.User.objects.get(wechat=encrypt.getHash(info.context.META['HTTP_TOKEN']))
            except:
                return forbidden_resp
        
        if realuser.usertype.lower() == 'teacher':
            serial = serializers.HWFCourseClassSerializer(data=course_data)
            if serial.is_valid():
                new_course = serial.save()
                new_course.teachers.add(realuser)
            return CreateCourse(ok=True, course=new_course)
        else:
            return http.HttpResponseForbidden('{"error":"you are not a teacher"}', content_type="application/json")

