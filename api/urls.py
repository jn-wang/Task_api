
from django.urls import path,include,re_path
from api.views import account
from api.views import task
urlpatterns = [
    # re_path(r'^course/$', course.CourseView.as_view()),
    # re_path(r'^micro/$', course.MicroView.as_view()),
    # re_path(r'^course/$', course.CourseView.as_view({'get':'list'})),
    #
    # re_path(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get':'retrieve'})), b
    re_path(r'^auth/$', account.AuthView.as_view()),
    re_path(r'^RegisteredView/$', account.RegisteredView.as_view()),
    re_path(r'^TaskView/$', task.TaskView.as_view({'get':'list'})),
    re_path(r'^TaskView/(?P<pk>\d+)/$', task.TaskView.as_view({'get': 'retrieve'})),
]
