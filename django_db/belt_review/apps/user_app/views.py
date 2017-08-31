# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, reverse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'user_app/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success('successfully registered!')
     
    return HttpResponseRedirect(request, reverse('user_app_name:index'))

def login(request, user_id):
    user = User.objects.get(id=user_id)
    return redirect('/user_page')

def user_page(request, user_id):
    context={
        'unique_book_reviews':user.reviews.all()
    }
    return render(request, 'user_app/user_page.html', context)

def logout(request):
    request.session.clear()

    return redirect('/')