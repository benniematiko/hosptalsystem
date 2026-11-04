def _item(label, url_name=None):
    return {"label": label, "url_name": url_name}


MENUS = {
    "receptionist": [
        _item("Dashboard", "dashboard:receptionist"),
        _item("Patients"),
        _item("Appointments"),
        _item("Queue"),
        _item("Referrals"),
        _item("Admissions"),
    ],
    "doctor": [
        _item("Dashboard", "dashboard:doctor"),
        _item("My Patients"),
        _item("Consultations"),
        _item("Prescriptions"),
        _item("Lab Requests"),
        _item("Follow-ups"),
    ],
    "lab_tech": [
        _item("Dashboard", "dashboard:lab_tech"),
        _item("Test Requests"),
        _item("Samples"),
        _item("Results"),
        _item("Equipment"),
    ],
    "pharmacist": [
        _item("Dashboard", "dashboard:pharmacist"),
        _item("Prescriptions"),
        _item("Inventory"),
        _item("Stock Adjustments"),
        _item("Suppliers"),
        _item("Pharmacy Sales"),
    ],
    "cashier": [
        _item("Dashboard", "dashboard:cashier"),
        _item("Invoices"),
        _item("Payments"),
    ],
    "manager": [
        _item("Dashboard", "dashboard:manager"),
        _item("Reports"),
        _item("Staff"),
        _item("Departments"),
        _item("Patient Statistics"),
    ],
    "admin": [
        _item("Dashboard", "dashboard:admin"),
        _item("Users"),
        _item("Roles & Permissions"),
        _item("Audit Logs"),
        _item("Configuration"),
    ],
}