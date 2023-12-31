from django.urls import path

from board.apps import BoardConfig
from board.views import MessageListView, MessageCreateView

app_name = BoardConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name="messages"),
    path('create', MessageCreateView.as_view(), name="create"),
]