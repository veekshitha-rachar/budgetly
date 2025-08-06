from django.shortcuts import render
from .models import Income, Expense
from django.db.models import Sum

def dashboard_view(request):
    total_income = Income.objects.aggregate(total=Sum('amount'))['total'] or 0
    total_expense = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expense

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'dashboard.html', context)
