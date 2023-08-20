from django.shortcuts import render, redirect
from django.contrib import messages


from website.forms import ContactForm, CantactModelForm
from website.models import Contact
# Create your views here.


def home(request):
    return render(request, 'website/home.html')


def contact(request):
    if request.method == 'GET':
        form = CantactModelForm()
        return render(request, 'website/contact.html', {'form': form})
    if request.method == 'POST':
        form = CantactModelForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Contact.objects.create(name=cd['name'], email=cd['email'], subject=cd['subject'], message=cd['message'])
            messages.success(request, 'your contact info stored successfully, we call you soon', 'success')
            return redirect('website:contact')
        return render(request, 'website/contact.html', {'form': form})


def about(request):
    return render(request, 'website/about.html')