from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.views.generic import TemplateView
from xjson.models import Document
# Create your views here.
#def index(request):
#    return render(request, 'xjson/index.html')

#def convert(request):
#    return render(request, 'xjson/convert.html')

from django.http import HttpResponse
from django.shortcuts import render
from xjson.forms import NewDocForm
from xjson.xmlcsv import get_file_name

# Imaginary function to handle an uploaded file.
from xjson.ConvertFormat import convert_uploaded_file

"""
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(form.value)
        if form.is_valid():
            convert_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('convert')
    else:
        form = DocumentForm()
    return render(request, 'success.html', {'form': form})
"""

import os, tempfile, zipfile
from django.conf import settings
import mimetypes
from wsgiref.util import FileWrapper
from xjson.Constants import *


def send_file(request):

  filename     = download_file_path+'download.csv' # Select your file here.
  download_name = 'converted_to_csv.csv'
  wrapper      = FileWrapper(open(filename))
  content_type = mimetypes.guess_type(filename)[0]
  response     = HttpResponse(wrapper,content_type=content_type)
  response['Content-Length']      = os.path.getsize(filename)
  response['Content-Disposition'] = "attachment; filename=%s"%download_name
  print("send_file view - ", download_name)
  return response

def success(request):
    return render(request, 'xjson/success.html')

def download(request):
    return render(request, 'xjson/success.html')

class UploadView(TemplateView):
    template_name = 'xjson/index.html'

    def get(self, request):
        form = NewDocForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = NewDocForm(request.POST, request.FILES)


        if form.is_valid():
            file = request.FILES['file']
            if file.name.endswith('.json') or file.name.endswith('.xml'):
                filename = get_file_name(file)
                fileurl = convert_uploaded_file(request.FILES['file'])
                if fileurl == DATA_ERROR_CONSTANT:
                    return render(request, 'xjson/error.html', {'error_msg' : DATA_ERROR_CONSTANT})
                else:
                    return render(request, 'xjson/success.html', {'fileurl' : fileurl, 'filename':filename})
            else:
                return render(request, 'xjson/error.html', {'error_msg' : INVALID_FILE_FORMAT})
        else:
            return render(request, 'xjson/error.html', {'error_msg' : INVALID_FILE_FORMAT})


