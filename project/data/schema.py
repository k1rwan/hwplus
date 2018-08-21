import graphene
from graphene_django.types import DjangoObjectType
from data import models

class UserAvatarType(DjangoObjectType):
    class Meta:
        model = models.UserAvatar


class UserType(DjangoObjectType):
    class Meta:
        model = models.User


class TeacherType(DjangoObjectType):
    class Meta:
        model = models.User


class TeachingAssistantType(DjangoObjectType):
    class Meta:
        model = models.User


class StudentType(DjangoObjectType):
    class Meta:
        model = models.User


class CourseType(DjangoObjectType):
    class Meta:
        model = models.HWFCourseClass


class Query(object):

    all_users = graphene.List(UserType)
    get_users_by_ids = graphene.List(UserType, ids=graphene.List(of_type=graphene.Int))

    all_courses = graphene.List(CourseType)
    get_course_by_id = graphene.Field(CourseType, id=graphene.Int())
    search_courses_by_keywords = graphene.List(CourseType, keywords=graphene.String())
    search_courses_by_name = graphene.List(CourseType, name=graphene.String())
    search_courses_by_teacher_name = graphene.List(CourseType, teacher_name=graphene.String())

    def resolve_all_users(self, info, **kwargs):
        return models.User.objects.all()
        
    def resolve_get_users_by_ids(self, info, **kwargs):
        result = models.models.Q(pk=None)
        for item in kwargs['ids']:
            result = result | models.models.Q(pk=item)
        return models.User.objects.filter(result)

    def resolve_all_courses(self, info, **kwargs):
        return models.HWFCourseClass.objects.all()

    def resolve_get_course_by_id(self, info, **kwargs):
        return models.HWFCourseClass.objects.get(pk=kwargs['id'])

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