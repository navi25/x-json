from django.conf.urls import url

from . import views

app_name = 'xjson'

urlpatterns = [
    #url(r'^$', views.index, name='home'),
    url(r'^$', views.UploadView.as_view(), name='index'),

]
