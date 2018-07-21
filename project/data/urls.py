from rest_framework.routers import DefaultRouter
from data import views
from data import user_views
from data import course_class_views
from django.conf.urls import url,include

router=DefaultRouter()
# router.register('courses',course_class_views.HWFCourseClassViewSet,'course')
router.register('assignments',views.HWFAssignmentViewSet,'assignment')
router.register('files',views.HWFFileViewSet,'file')
router.register('submissions',views.HWFSubmissionViewSet,'submission')
router.register('questions',views.HWFQuestionViewSet,'question')
router.register('answers',views.HWFAnswerViewSet,'answer')
router.register('reviews',views.HWFReviewViewSet,'review')

urlpatterns=[
    url(r'^data/',include(router.urls)),
    url(r'^data/users/$',user_views.user_list),
    url(r'^data/users/(?P<pk>[0-9]+)/$',user_views.user_detail),
    url(r'^login/$',user_views.login),
    url(r'^data/is_repeated/$',user_views.is_repeated),
    url(r'^account/activate/$',user_views.activate),
    url(r'^account/change_password/$',user_views.change_password),
    url(r'^account/forget_password/$',user_views.forget_password),
    url(r'^account/confirm_forgotten/$',user_views.confirm_forgotten),
    url(r'^account/change_directly/$',user_views.directly_change)
]

urlpatterns+=[
    url(r'^data/courses/$',course_class_views.HWFCourseClassListView.as_view()),
    url(r'^data/courses/(?P<pk>[0-9]+)/$',course_class_views.HWFCourseClassDetailView.as_view()),
    url(r'^data/user_with_course/student/$',course_class_views.UserWithCourseListViewForStudent.as_view()),
    url(r'^data/user_with_course/student/(?P<pk>[0-9]+)/$',course_class_views.UserWithCourseDetailViewForStudent.as_view()),
    url(r'^data/user_with_course/teacher/$',course_class_views.UserWithCourseListViewForTeacher.as_view()),
    url(r'^data/user_with_course/teacher/(?P<pk>[0-9]+)/$',course_class_views.UserWithCourseDetailViewForTeacher.as_view()),
    url(r'^data/user_with_course/assistant/$',course_class_views.UserWithCourseListViewForAssistant.as_view()),
    url(r'^data/user_with_course/assistant/(?P<pk>[0-9]+)/$',course_class_views.UserWithCourseDetailViewForAssistant.as_view()),
]