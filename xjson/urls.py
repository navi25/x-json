from django.conf.urls import url
from xjson.Constants import download_filePath

from . import views

app_name = 'xjson'


urlpatterns = [
    #url(r'^$', views.index, name='home'),
    url(r'^$', views.UploadView.as_view(), name='index'),
    url(r'^documents$', views.success, name='success'),
    url(r'^documents/download.csv$',views.send_file, name='download'),

]
