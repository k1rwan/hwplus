import graphene
from django import http

from data import models, serializers
from data.user_views import token
from data import encrypt
from data.graphql_schema.types import CourseType
from data.graphql_schema.inputs import CourseEditionInput

forbidden_resp = http.HttpResponseForbidden('{"error": "forbidden"}',content_type="application/json")

# editing a course
class EditCourse(graphene.Mutation):

    class Arguments:
        course_data = CourseEditionInput(required=True)

    ok = graphene.Boolean()
    course = graphene.Field(CourseType)

    def mutate(self, info, course_data):

        try:
            realuser = token.confirm_validate_token(info.context.META['HTTP_TOKEN'])
            realuser = models.User.objects.get(username=realuser)
            editing_course = models.HWFCourseClass.objects.get(pk=course_data['id'])
        except:
            try:
                realuser = models.User.objects.get(wechat=encrypt.getHash(info.context.META['HTTP_TOKEN']))
                editing_course = models.HWFCourseClass.objects.get(pk=course_data['id'])
            except:
                return forbidden_resp

        if len(editing_course.teachers.filter(pk=realuser.id)) == 0:
            if len(editing_course.teaching_assistants.filter(pk=realuser.id)) == 0:
                return forbidden_resp
            else:
                if 'description' in course_data:
                    editing_course.description = course_data['description']
                if 'marks' in course_data:
                    editing_course.marks = course_data['marks']
                if 'students' in course_data:
                    for student_id in course_data['students']:
                        editing_course.students.add(models.User.objects.get(pk=student_id))
                if 'school' in course_data:
                    editing_course.school = course_data['school']
                if 'start_time' in course_data:
                    editing_course.start_time = course_data['start_time']
                if 'end_time' in course_data:
                    editing_course.end_time = course_data['end_time']
                editing_course.save()
                return EditCourse(ok=True, course=editing_course)
        else:
            if 'name' in course_data:
                editing_course.name = course_data['name']
            if 'description' in course_data:
                editing_course.description = course_data['description']
            if 'marks' in course_data:
                editing_course.marks = course_data['marks']
            if 'teachers' in course_data:
                for teacher_id in course_data['teachers']:
                    editing_course.teachers.add(models.User.objects.get(pk=teacher_id))
            if 'teaching_assistants' in course_data:
                for teaching_assistant_id in course_data['teaching_assistants']:
                    editing_course.teaching_assistants.add(models.User.objects.get(pk=teaching_assistant_id))
            if 'students' in course_data:
                for student_id in course_data['students']:
                    editing_course.students.add(models.User.objects.get(pk=student_id))
            if 'school' in course_data:
                editing_course.school = course_data['school']
            if 'start_time' in course_data:
                editing_course.start_time = course_data['start_time']
            if 'end_time' in course_data:
                editing_course.end_time = course_data['end_time']
            editing_course.save()
            return EditCourse(ok=True, course=editing_course)

