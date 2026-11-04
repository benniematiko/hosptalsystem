from .models import AuditLog


def get_client_ip(request):
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def log_action(user, action, instance=None, details="", request=None):
    return AuditLog.objects.create(
        user=user if user and user.is_authenticated else None,
        action=action,
        model_name=instance.__class__.__name__ if instance else "",
        object_id=str(instance.pk) if instance else "",
        details=details,
        ip_address=get_client_ip(request) if request else None,
    )