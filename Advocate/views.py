from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import clientform
from django.contrib.auth.models import User


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

def personalinfo(request):
    return render(request, 'personalinfo.html')


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
    email = User.objects.get(email=email)
    return render(request, 'userprofile.html', {'email': email})


def clientforms(request):
    return render(request, 'clientforms.html')

def Caseinfo(request):
    return render(request, 'Caseinfo.html')
