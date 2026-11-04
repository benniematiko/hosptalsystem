from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.permissions import role_required


@login_required
def dashboard(request):
    return render(request, "core/dashboard.html")


# @role_required("doctor")
# def test_doctor(request):
#     return HttpResponse("Doctor page OK")


# @role_required("admin")
# def test_admin(request):
#     return HttpResponse("Admin page OK")