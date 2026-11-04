from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard_home, name="home"),

    # role dashboards 
    path("receptionist/", views.receptionist_dashboard, name="receptionist"),
    path("doctor/", views.doctor_dashboard, name="doctor"),
    path("lab-tech/", views.lab_tech_dashboard, name="lab_tech"),
    path("pharmacist/", views.pharmacist_dashboard, name="pharmacist"),
    path("cashier/", views.cashier_dashboard, name="cashier"),
    path("manager/", views.manager_dashboard, name="manager"),
    path("admin/", views.admin_dashboard, name="admin"),
]