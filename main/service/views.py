from django.shortcuts import  render, redirect
from .forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User

def logo(request):
    return render(request=request, template_name="logo.html")

def main(request):
    return HttpResponse('done')

def register_request(request):

    if request.method == "POST":
        form = reg_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create_user(username=username,password=password,email=email)
            print(user)

            return redirect("questions")

        else:
            print('aa')
            # return redirect("main")
            # messages.error(request, "Unsuccessful registration. Invalid information.")
    form = reg_form()
    return render (request=request, template_name="main.html", context={"register_form":form})

def questions(request):
    form = quest_form
    if request.method == "POST":
        form = quest_form(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            revenue = form.cleaned_data['revenue']
            fee1 = form.cleaned_data['fee1']
            fee2 = form.cleaned_data['fee2']

            print(request.user,' ',company,' ',revenue,' ',fee1,' ',fee2)

            return redirect("fin")

    return render(request=request, template_name="questions.html", context={"register_form":form})

def fin(request):
    return render(request=request, template_name="fin.html")