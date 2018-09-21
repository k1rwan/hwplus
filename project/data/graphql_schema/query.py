import graphene
from data.graphql_schema.types import *

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

    all_assignments = graphene.List(AssignmentType)
    get_assignments_by_ids = graphene.List(AssignmentType, ids=graphene.List(of_type=graphene.Int))
    get_assignments_by_courses = graphene.List(AssignmentType, courses=graphene.List(of_type=graphene.Int))
    get_assignments_by_deadline = graphene.List(AssignmentType, deadline=graphene.DateTime())
    search_assignments_by_name = graphene.List(AssignmentType, name=graphene.String())
    search_asssignments_by_keywords = graphene.List(AssignmentType, keywords=graphene.String())
    

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

    # specific query of assignments
    def resolve_all_assignments(self, info, **kwargs):
        return models.HWFAssignment.objects.all()

    def resolve_get_assignments_by_ids(self, info, **kwargs):
        result = models.models.Q(pk=None)
        for item in kwargs['ids']:
            result = result | models.models.Q(pk=item)
        return models.HWFAssignment.objects.filter(result)

    def resolve_get_assignments_by_courses(self, info, **kwargs):
        result = models.models.Q(course_class_id=None)
        for item in kwargs['courses']:
            result = result | models.models.Q(course_class_id=item)
        return models.HWFAssignment.objects.filter(result)

    def resolve_get_assignments_by_deadline(self, info, **kwargs):
        result = models.models.Q(pk=None)
        for item in models.HWFAssignment.objects.all():
            if item.deadline < kwargs['deadline']:
                result = result | models.models.Q(pk=item.pk)
        return models.HWFAssignment.objects.filter(result)

    def resolve_search_assignments_by_name(self, info, **kwargs):
        result = models.models.Q(pk=None)
        for item in models.HWFAssignment.objects.all():
            if kwargs['name'] in item.name:
                result = result | models.models.Q(pk=item.pk)
        return models.HWFAssignment.objects.filter(result)

    def resolve_search_assignments_by_keywords(self, info, **kwargs):
        result = models.models.Q(pk=None)
        for item in models.HWFAssignment.objects.all():
            if kwargs['keywords'] in item.name or kwargs['keywords'] in item.description:
                result = result | models.models.Q(pk=item.pk)
            elif kwargs['keywords'] in item.course_class.name or kwargs['keywords'] in item.course_class.description:
                result = result | models.models.Q(pk=item.pk)
            else:
                course_teachers = item.course_class.teachers.all()
                for teacher in course_teachers:
                    if kwargs['keywords'] in teacher.name:
                        result = result | models.models.Q(pk=item.pk)
                        break