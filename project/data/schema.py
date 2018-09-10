# -*- coding: utf-8 -*-
import graphene
from django import http
from graphene_django.types import DjangoObjectType

from data import models, serializers
from data.safe_gql_view import BetterGraphQLView
from data.user_views import token

from data import encrypt

# GraphQL Schema

# hidden fields
user_exclude_fields = ('password', 'is_staff', 'is_superuser', 'first_name', 'last_name')


# graphql types
class UserAvatarType(DjangoObjectType):
    class Meta:
        model = models.UserAvatar


class UserType(DjangoObjectType):
    class Meta:
        model = models.User
        exclude_fields = user_exclude_fields


class TeacherType(DjangoObjectType):
    class Meta:
        model = models.User
        exclude_fields = user_exclude_fields


class TeachingAssistantType(DjangoObjectType):
    class Meta:
        model = models.User
        exclude_fields = user_exclude_fields


class StudentType(DjangoObjectType):
    class Meta:
        model = models.User
        exclude_fields = user_exclude_fields


class CourseType(DjangoObjectType):
    class Meta:
        model = models.HWFCourseClass


class AssignmentType(DjangoObjectType):
    class Meta:
        model = models.HWFAssignment


# arguments of creating a user
class UserCreationInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    name = graphene.String(required=True)
    gender = graphene.String(required=True)
    usertype = graphene.String(required=True)
    password = graphene.String(required=True)
    bupt_id = graphene.String(required=False)
    class_number = graphene.String(required=False)
    email = graphene.String(required=True)
    phone = graphene.String(required=True)


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


# arguments of editing a user
class UserEditionInput(graphene.InputObjectType):
    id = graphene.Int(required=True)
    username = graphene.String(required=False)
    class_number = graphene.String(required=False)
    phone = graphene.String(required=False)


# editing a user
class EditUser(graphene.Mutation):

    class Arguments:
        user_data = UserEditionInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    def mutate(self, info, user_data):
        try:
            realuser = token.confirm_validate_token(info.context.META['HTTP_TOKEN'])
            realuser = models.User.objects.get(username=realuser)
            editing_user = models.User.objects.get(pk=user_data['id'])
        except:
            try:
                realuser = models.User.objects.get(wechat=encrypt.getHash(info.context.META['HTTP_TOKEN']))
                editing_user = models.User.objects.get(pk=user_data['id'])
            except:
                return http.HttpResponseForbidden('{"error":"forbidden"}', content_type="application/json")
        if editing_user.username == realuser.username:
            if 'username' in user_data:
                editing_user.username = user_data['username']
            if 'class_number' in user_data:
                editing_user.class_number = user_data['class_number']
            if 'phone' in user_data:
                editing_user.phone = user_data['phone']
            editing_user.save()
            ok = True
            return EditUser(user=editing_user, ok=ok)
        else:
            return http.HttpResponseForbidden('{"error":"forbidden"}', content_type="application/json")


# arguments of creating a course
class CourseCreationInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String(required=True)
    marks = graphene.Float(required=True)
    teachers = graphene.List(of_type=graphene.Int, required=False)
    teaching_assistants = graphene.List(of_type=graphene.Int, required=False)
    students = graphene.List(of_type=graphene.Int, required=False)
    school = graphene.String(required=False)
    start_time = graphene.DateTime(required=True)
    end_time = graphene.DateTime(required=True)


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
                return http.HttpResponseForbidden('{"error":"forbidden"}', content_type="application/json")
        
        if realuser.usertype.lower() == 'teacher':
            serial = serializers.HWFCourseClassSerializer(data=course_data)
            if serial.is_valid():
                new_course = serial.save()
                new_course.teachers.add(realuser)
            return CreateCourse(ok=True, course=new_course)
        else:
            return http.HttpResponseForbidden('{"error":"you are not a teacher"}', content_type="application/json")
        

# arguments of editing a course
class CourseEditionInput(graphene.InputObjectType):
    id = graphene.Int(required=True)
    name = graphene.String(required=False)
    description = graphene.String(required=False)
    marks = graphene.Float(required=False)
    teachers = graphene.List(of_type=graphene.Int, required=False)
    teaching_assistants = graphene.List(of_type=graphene.Int, required=False)
    students = graphene.List(of_type=graphene.Int, required=False)
    school = graphene.String(required=False)
    start_time = graphene.DateTime(required=False)
    end_time = graphene.DateTime(required=False)


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
                return http.HttpResponseForbidden('{"error":"forbidden"}', content_type="application/json")

        if realuser.usertype.lower() == 'teacher':

            if len(editing_course.teachers.filter(pk=realuser.id)) == 0:
                return http.HttpResponseForbidden('{"error":"forbidden"}', content_type="application/json")
            
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

        elif realuser.usertype.lower() == 'assistant':

            if len(editing_course.teaching_assistants.filter(pk=realuser.id)) == 0:
                return http.HttpResponseForbidden('{"error":"forbidden"}', content_type="application/json")

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

        elif realuser.usertype.lower() == 'student':
            try:
                realuser = models.User.objects.get(wechat=encrypt.getHash(info.context.META['HTTP_TOKEN']))
            except:
                return http.HttpResponseForbidden('{"error":"forbidden"}', content_type="application/json")
            if 'students' in course_data:
                for student_id in course_data['students']:
                    if student_id == realuser.pk:
                        editing_course.students.add(models.User.objects.get(pk=student_id))
                    else:
                        return http.HttpResponseForbidden('{"error":"forbidden"}', content_type="application/json")
            editing_course.save()
            return EditCourse(ok=True, course=editing_course)


# arguments of creating an Assignment
class AssignmentCreationInput(graphene.InputObjectType):
    course_class_id = graphene.Int(required=True)
    name = graphene.String(required=True)
    description = graphene.String(required=True)
    deadline = graphene.DateTime(required=True)
    addfile = graphene.String(required=True)

# query
class Query(object):

    all_users = graphene.List(UserType)
    get_users_by_ids = graphene.List(UserType, ids=graphene.List(of_type=graphene.Int))
    get_users_by_usertype = graphene.List(UserType, usertype=graphene.String())
    get_users_by_usernames = graphene.List(UserType, usernames=graphene.List(of_type=graphene.String))

    all_courses = graphene.List(CourseType)
    get_courses_by_ids = graphene.List(CourseType, ids=graphene.List(of_type=graphene.Int))
    search_courses_by_keywords = graphene.List(CourseType, keywords=graphene.String())
    search_courses_by_name = graphene.List(CourseType, name=graphene.String())
    search_courses_by_teacher_name = graphene.List(CourseType, teacher_name=graphene.String())
    all_teachers = graphene.List(TeacherType)
    all_students = graphene.List(StudentType)
    all_teaching_assistants = graphene.List(TeachingAssistantType)

    # query for users
    def resolve_all_users(self, info, **kwargs):
        return models.User.objects.all()
        
    def resolve_get_users_by_ids(self, info, **kwargs):
        result = models.models.Q(pk=None)
        for item in kwargs['ids']:
            result = result | models.models.Q(pk=item)
        return models.User.objects.filter(result)

    def resolve_get_users_by_usertype(self, info, **kwargs):
        return models.User.objects.filter(usertype=kwargs['usertype'])

    def resolve_get_users_by_usernames(self, info, **kwargs):
        result = models.models.Q(username=None)
        for item in kwargs['usernames']:
            result = result | models.models.Q(username=item)
        return models.User.objects.filter(result)

    # specific query of courses
    def resolve_all_courses(self, info, **kwargs):
        return models.HWFCourseClass.objects.all()

    def resolve_get_courses_by_ids(self, info, **kwargs):
        result = models.models.Q(pk=None)
        for item in kwargs['ids']:
            result = result | models.models.Q(pk=item)
        return models.HWFCourseClass.objects.filter(result)

    # fuzzy query of coruses
    def resolve_search_courses_by_keywords(self, info, **kwargs):
        result = models.models.Q(pk=None)
        for item in models.HWFCourseClass.objects.all():
            if kwargs['keywords'] in item.name:
                result = result | models.models.Q(pk=item.pk)
            if kwargs['keywords'] in item.description:
                result = result | models.models.Q(pk=item.pk)
            for teacher in item.teachers.all():
                if kwargs['keywords'] in teacher.name:
                    result = result | models.models.Q(pk=item.pk)
        return models.HWFCourseClass.objects.filter(result)

    def resolve_search_courses_by_name(self, info, **kwargs):
        result = models.models.Q(pk=None)
        for item in models.HWFCourseClass.objects.all():
            if kwargs['name'] in item.name:
                result = result | models.models.Q(pk=item.pk)
        return models.HWFCourseClass.objects.filter(result)

    def resolve_search_courses_by_teacher_name(self, info, **kwargs):
        result = models.models.Q(pk=None)
        for item in models.HWFCourseClass.objects.all():
            for teacher in item.teachers.all():
                if kwargs['teacher_name'] in teacher.name:
                    result = result | models.models.Q(pk=item.pk)
        return models.HWFCourseClass.objects.filter(result)

    # get related of course
    def resolve_all_teachers(self, info, **kwargs):
        return models.HWFCourseClass.objects.select_related('teachers').all()

    def resolve_all_students(self, info, **kwargs):
        return models.HWFCourseClass.objects.select_related('students').all()
    
    def resolve_all_teaching_assistants(self, info, **kwargs):
        return models.HWFCourseClass.objects.select_related('teaching_assistants').all()
