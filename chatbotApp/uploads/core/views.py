from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import ImageUploadModel
from uploads.core.forms import ImageUploadForm



def home(request):
    #documents = Document.objects.all()
    return render(request, 'core/home.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
 

    if request.method == 'POST':
    

        form= ImageUploadForm(request.POST, request.FILES) 

        if form.is_valid():
            form.save()
            return redirect('model_form_upload')
    else:
        form = ImageUploadForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })


    
 
