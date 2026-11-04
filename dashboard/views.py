from django.shortcuts import render

# Create your views here.


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect



from .permissions import role_required

# role value (from User.Role)  ->  URL name of that role's dashboard
ROLE_DASHBOARDS = {
    "receptionist": "dashboard:receptionist",
    "doctor": "dashboard:doctor",
    "lab_tech": "dashboard:lab_tech",
    "pharmacist": "dashboard:pharmacist",
    "cashier": "dashboard:cashier",
    "manager": "dashboard:manager",
    "admin": "dashboard:admin",
}


@login_required
def dashboard_home(request):
    url_name = ROLE_DASHBOARDS.get(request.user.role)
    if url_name is None:
        return HttpResponseForbidden("Your account has no valid role. Contact the administrator.")
    return redirect(url_name)



def _render(request, title):
    return render(request, "dashboard/role_dashboard.html", {"title": title})


@role_required("receptionist")
def receptionist_dashboard(request):
    return _render(request, "Receptionist Dashboard")


@role_required("doctor")
def doctor_dashboard(request):
    return _render(request, "Doctor Dashboard")


@role_required("lab_tech")
def lab_tech_dashboard(request):
    return _render(request, "Laboratory Dashboard")


@role_required("pharmacist")
def pharmacist_dashboard(request):
    return _render(request, "Pharmacy Dashboard")


@role_required("cashier")
def cashier_dashboard(request):
    return _render(request, "Cashier Dashboard")


@role_required("manager")
def manager_dashboard(request):
    return _render(request, "Manager Dashboard")


@role_required("admin")
def admin_dashboard(request):
    return _render(request, "Administrator Dashboard")