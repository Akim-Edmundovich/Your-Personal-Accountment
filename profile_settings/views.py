from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from transactions.models import Transaction, Category, Subcategory
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin  # Проверка прав доступа


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})


@login_required
def settings(request):
    return render(request, 'settings.html')


class ManageCategoryList(ListView):
    model = Category
    template_name = 'categories/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class OwnerMixin:
    """Можно использовать в представлениях, которые взаимодействуют
        с любой моделью, содержащей owner"""

    def get_queryset(self):
        """Извлечение курсов, созданных текущим пользователем."""
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OwnerCategoryMixin(OwnerMixin,
                         LoginRequiredMixin,
                         PermissionRequiredMixin):
    model = Category
    fields = ['name', 'type']
    success_url = reverse_lazy('manage_category_list')


class OwnerCategoryEditMixin(OwnerCategoryMixin, OwnerEditMixin):
    template_name = 'categories/form.html'


class CategoryCreateView(OwnerCategoryEditMixin, CreateView):
    """Создает объект Category"""
    permission_required = 'categories.add_category'


class CategoryUpdateView(OwnerCategoryEditMixin, UpdateView):
    """Редактирует объект Category"""
    permission_required = 'categories.change_category'


class CategoryDeleteView(OwnerCategoryEditMixin, DeleteView):
    """Удаляет объект Category"""
    template_name = 'categories/delete.html'
    permission_required = 'categories.delete_categories'
