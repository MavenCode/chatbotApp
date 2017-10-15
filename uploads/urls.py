from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls


from uploads.core import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^sample/questions/$', views.sample_questions, name='samples'),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
    url(r'^', include('send_email.urls')), #credit: https://wsvincent.com/django-contact-form/
    
] 					

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
