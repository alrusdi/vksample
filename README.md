# vksample
Sample of how to use vk.com friends API via vk module in conjunction with django and social-auth-app-django

1. Clone/download this repository
2. Create new venv python3 -m venv env
3. Activate it source ./env/bin/activate
4. Install requirements pip install -r requirements.txt
5. Init db python manage.py migrate

Fill appropriate data into variables in core/settings.py:

SOCIAL_AUTH_VK_OAUTH2_KEY = '' <-- Here should be your App ID

SOCIAL_AUTH_VK_OAUTH2_SECRET = '' <-- Here should be a Secret Key

For development add domain of your vk app to /etc/hosts as localhost

Start your project python manage.py runserver

And go to http://<your-url>:8000
