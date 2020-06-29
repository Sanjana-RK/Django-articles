from . import views
from django.urls import path,include,re_path

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/$', views.signup_view, name="signup"),
    re_path('^login/$',views.login_view,name="login"),
    re_path('^logout/$',views.logout_view,name="logout"),
]
