## Development hints and tips

### Generating new django secret key
`from django.core.management.utils import get_random_secret_key`
`get_random_secret_key()`

### Running shell with env variables
1. Windows
    - Set Env variables by below command
    `set MODE=dev & set SECRET_KEY='something' & set DB_NAME=db_name & set DB_USER=user & set DB_PASSWORD=correct_password`
    - Now you can run `python manage.py shell`