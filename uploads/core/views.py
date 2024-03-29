from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import ImageUploadModel
from uploads.core.forms import ImageUploadForm
from django.contrib import messages



def home(request):
    #documents = Document.objects.all()
    return render(request, 'core/home.html')


def sample_questions(request):
    #documents = Document.objects.all()
    return render(request, 'core/sample_questions.html')


def model_form_upload(request):
 

    if request.method == 'POST':
    

        form= ImageUploadForm(request.POST, request.FILES) 

        if form.is_valid():
            form.save()
            messages.success(request, 'Uploaded successfully!')
            #return redirect('model_form_upload')
    else:
        form = ImageUploadForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    }
    )


    
 
