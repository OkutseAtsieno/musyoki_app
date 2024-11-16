from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import clientform
from django.contrib.auth.models import User
from .models import user_profile
from django.contrib import messages


# Create your views here.

@login_required()
def index(request):
    email = request.user.email
    dat = User.objects.get(email=email)

    try:
        prof = user_profile.objects.get(email=email)
        prof = prof.image
    except user_profile.DoesNotExist:
        prof =''
    return render(request, 'index.html', {'dat': dat, 'prof':prof})


def Clientsection(request):
    return render(request, 'Clientsection.html')


def client_list(request):  # display all the client lists
    return render(request, 'clientlist.html')


def case(request):
    return render(request, 'case.html')


def client_form(request):  # deal with insert and update operations
    if request.method == "POST":
        form = clientform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
        else:

            return render(request, 'clientform.html', {'form': form})
    else:

        form = clientform()
        return render(request, 'clientform.html', {'form': form})


def client_delete(request):  # deals with the delete operations
    return


pass


@login_required()
def userprofile(request):
    email = request.user.email
    dat = User.objects.get(email=email)

    try:
        fname = user_profile.objects.get(email=email)
        fname = fname.fname
    except user_profile.DoesNotExist:
        fname = ''
    try:
        lname = user_profile.objects.get(email=email)
        lname = lname.lname
    except user_profile.DoesNotExist:
        lname = ''
    try:
        company = user_profile.objects.get(email=email)
        company = company.company
    except user_profile.DoesNotExist:
        company = ''
    try:
        job = user_profile.objects.get(email=email)
        job = job.job
    except user_profile.DoesNotExist:
        job = ''
    try:
        county = user_profile.objects.get(email=email)
        county = county.county
    except user_profile.DoesNotExist:
        county = ''
    try:
        address = user_profile.objects.get(email=email)
        address = address.address
    except user_profile.DoesNotExist:
        address = ''
    try:
        phone = user_profile.objects.get(email=email)
        phone = phone.phone
    except user_profile.DoesNotExist:
        phone = ''
    try:
        email = user_profile.objects.get(email=email)
        email = email.email
    except user_profile.DoesNotExist:
        email = ''
    try:
        profile = user_profile.objects.get(email=email)
        profile = profile.image
    except user_profile.DoesNotExist:
        profile = ''

    return render(request, 'userprofile.html',
                  {'dat': dat, 'fname': fname, 'lname': lname, 'company': company, 'job': job, 'county': county,
                   'address': address, 'phone': phone, 'email': email, 'profile': profile})


def clientforms(request):
    return render(request, 'clientforms.html')


def userprofileinsert(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        company = request.POST.get('company')
        job = request.POST.get('job')
        county = request.POST.get('county')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        image = request.FILES['image']

        userprofiles = user_profile(fname=fname, lname=lname, company=company, job=job, county=county, address=address,
                                    phone=phone, email=email, image=image)
        userprofiles.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('userprofile')
    return redirect('userprofile')
