from .navigation import MENUS


def sidebar_menu(request):
    """Gives every template a `menu_items` list for the logged-in user's role."""
    user = request.user
    if not user.is_authenticated:
        return {}
    return {"menu_items": MENUS.get(user.role, [])}