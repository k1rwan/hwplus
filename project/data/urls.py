from rest_framework.routers import DefaultRouter
from data import views
from django.conf.urls import url,include

router=DefaultRouter()
router.register('courses',views.HWFCourseClassViewSet,'course')
router.register('assignments',views.HWFAssignmentViewSet,'assignment')
router.register('files',views.HWFFileViewSet,'file')
router.register('submissions',views.HWFSubmissionViewSet,'submission')
router.register('questions',views.HWFQuestionViewSet,'question')
router.register('answers',views.HWFAnswerViewSet,'answer')
router.register('reviews',views.HWFReviewViewSet,'review')

urlpatterns=[
    url(r'^data/',include(router.urls)),
    url(r'^data/users/$',views.user_list),
    url(r'^data/users/(?P<pk>[0-9]+)/$',views.user_detail),
    url(r'^login/$',views.login),
    url(r'^data/get_all/$',views.get_all)
]