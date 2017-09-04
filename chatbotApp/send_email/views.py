# -*- coding: utf-8 -*-
# send_email/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm



def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['taiwo.adetiloye@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            #return redirect('success')
            form = ContactForm()
            messages.success(request, 'Success! Email sent.')
    return render(request, "email.html", {'form': form})


# def success(request):
# 	return render(request, 'success.html')
    #return HttpResponse('Success! Thank you for your message.')
