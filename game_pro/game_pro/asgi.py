"""
ASGI config for game_pro project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from home.consumers import GameRoom
from django.urls import path
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_pro.settings')

application = get_asgi_application()

ws_pattern = [
    path('ws/game/<room_code>', GameRoom)
]

application = ProtocolTypeRouter(
    {
        'websocket' : AuthMiddlewareStack(URLRouter([

        ]))
    }
)
