from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),


    # path("test-doctor/", views.test_doctor),
    # path("test-admin/", views.test_admin),
]