from django import forms
from django.core.files.images import get_image_dimensions
from uploads.core.models import ImageUploadModel



class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ('image',)
    FILE_EXT_WHITELIST = ['jpg','jpeg']


    def clean_image(self): # method name must be same name as the field
       picture = self.cleaned_data.get("image")
       

       if not picture:
           raise forms.ValidationError("No image!")
       else:
           w, h = get_image_dimensions(picture)
           if w != 400:
               raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 400px wide" % w)
           if h != 300:
               raise forms.ValidationError("The image is %i pixel high. It's supposed to be 300px long" % h)
       
           if len(picture.name.split('.')) == 1:
              raise forms.ValidationError("File type is not supported.")
           if picture.name.split('.')[-1] in self.FILE_EXT_WHITELIST:
               return picture
           else:
             raise forms.ValidationError("Only '.jpg' and '.jpeg' files are allowed.")
       return picture




