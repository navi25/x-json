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

from django.http import HttpResponseRedirect
from django.shortcuts import render
from xjson.forms import NewDocForm


# Imaginary function to handle an uploaded file.
from xjson.ConvertFormat import handle_uploaded_file

"""
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(form.value)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('convert')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})
"""

class UploadView(TemplateView):
    template_name = 'xjson/index.html'

    def get(self, request):
        form = NewDocForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = NewDocForm(request.POST, request.FILES)


        if form.is_valid():
            name = handle_uploaded_file(request.FILES['file'])
            return render(request, 'xjson/upload.html', {'name' : name})


