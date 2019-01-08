from django.conf.urls import url

from account.views import SignUp, login_view,login_user, logout_view, dashboard_view


app_name = "account"

urlpatterns = [
    url(r'^register/$', SignUp.as_view(), name="signup"),
    url(r'^login/$', login_view, name="login"),
    url(r'^login_user/$', login_user, name="login_user"),
    url(r'^logout/$', logout_view, name="logout_view"),
    url(r'^dashboard/(?P<username>[\w.@+-]+)/$', dashboard_view, name="dashboard_view"),
]