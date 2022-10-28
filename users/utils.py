def get_allowed_user_actions(user):
    return [
        {'title': 'My visits manager', 'path': '/', 'icon': 'tour'},
        {'title': 'Add new trip', 'path': '/trips/new', 'icon': 'add'},
        {'title': 'Shared trips', 'path': '/trips/shared', 'icon': 'share'},
        {'title': 'Trip requests', 'path': '/trips/requests', 'icon': 'flight'},
    ]
