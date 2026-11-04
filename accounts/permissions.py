from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from core.services import log_action


def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.role in roles:
                return view_func(request, *args, **kwargs)
            log_action(
                request.user,
                "ACCESS_DENIED",
                details=request.path,
                request=request,
            )
            raise PermissionDenied

        return login_required(wrapper)

    return decorator