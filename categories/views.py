from django.shortcuts import render
from .models import Category, Subcategory, Expenses, Income


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html',
                  {'categories': categories})
