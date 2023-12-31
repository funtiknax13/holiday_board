from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from board.forms import MessageForm
from board.models import Message


class MessageListView(ListView):
    model = Message

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_public=True).order_by('?')[:5]
        return queryset


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('board:messages')

    def form_valid(self, form):
        if form.is_valid():
            new_message = form.save()
            new_message.save()

        return super().form_valid(form)
