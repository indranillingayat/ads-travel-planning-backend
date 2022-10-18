def get_allowed_user_actions(user):
    return [
        {'title': 'My visits manager', 'path': '/', 'icon': 'tour'},
        {'title': 'Add new trip', 'path': '/trip/new', 'icon': 'add'},
        {'title': 'Shared trips', 'path': '/trip/shared', 'icon': 'share'},
        {'title': 'Trip requests', 'path': '/trip/requests', 'icon': 'flight'},
    ]
