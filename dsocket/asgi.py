# mysite/asgi.py
import os

import django
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter,URLRouter
import mysite.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dsocket.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    "websocket": AuthMiddlewareStack(URLRouter(mysite.routing.websocket_urlpatterns)),
})
