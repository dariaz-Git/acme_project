from django.shortcuts import get_object_or_404  # redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(LoginRequiredMixin, CreateView):
    model = Birthday
    form_class = BirthdayForm

    def form_valid(self, form):
        """Сохряняет имя автора в БД"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class BirthdayUpdateView(LoginRequiredMixin, UpdateView):
    model = Birthday
    form_class = BirthdayForm

    def dispatch(self, request, *args, **kwargs):
        """Проверяет право пользователя на редактирование записи"""
        instance = get_object_or_404(
            Birthday, pk=kwargs['pk'], author=request.user
        )
        if instance.author != request.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class BirthdayDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляет запись из БД"""
    model = Birthday

    def dispatch(self, request, *args, **kwargs):
        """Проверяет право пользователя на удаление записи"""
        instanse = get_object_or_404(
            Birthday, pk=kwargs['pk'], author=request.user
        )
        if instanse.author != request.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["birthday_countdown"] = calculate_birthday_countdown(
            self.object.birthday)
        return context
