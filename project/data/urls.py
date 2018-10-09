from django.conf.urls import include, url
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from data import user_views, views
from project import settings

router = DefaultRouter()
router.register('avatars', user_views.UserAvatarViewset, 'avatar')
router.register('files', views.HWFFileViewSet, 'file')
router.register('questions', views.HWFQuestionViewSet, 'question')
router.register('answers', views.HWFAnswerViewSet, 'answer')
router.register('reviews', views.HWFReviewViewSet, 'review')

urlpatterns = [
    url(r'^data/', include(router.urls)),
    url(r'^data/users/$', user_views.user_list),
    url(r'^data/users/(?P<pk>[0-9]+)/$', user_views.user_detail),
    url(r'^login/$', user_views.login),
    url(r'^data/is_repeated/$', user_views.is_repeated),
    url(r'^account/activate/$', user_views.activate),
    url(r'^account/change_password/$', user_views.change_password),
    url(r'^account/forget_password/$', user_views.forget_password),
    url(r'^account/confirm_forgotten/$', user_views.confirm_forgotten),
    url(r'^account/change_directly/$', user_views.directly_change)
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^data/get_qrcode/$',views.get_qrcode),
    url(r'^data/bind_wechat_qrcode/$',views.bind_wechat)
]