def get_app_settings():
    import os

    mode = os.environ.get('MODE', 'dev')

    if mode == 'dev':
        from .dev import AppSettings

    elif mode == 'staging':
        from .staging import AppSettings

    elif mode == 'prod':
        from .prod import AppSettings

    else:
        raise Exception("Invalid configurations, please set proper app run mode")

    return AppSettings()
