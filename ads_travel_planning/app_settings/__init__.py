def get_app_settings():
    from environs import Env
    env = Env()
    env.read_env()

    mode = env.str('MODE', 'dev')

    if mode == 'dev':
        from .dev import AppSettings

    elif mode == 'staging':
        from .staging import AppSettings

    elif mode == 'prod':
        from .prod import AppSettings

    else:
        raise Exception("Invalid configurations, please set proper app run mode")

    return AppSettings(env)
