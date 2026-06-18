from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.utils import timezone
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.all()

    # --- Filters ---
    category_filter = request.GET.get('category')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    search_query = request.GET.get('search')

    if category_filter:
        expenses = expenses.filter(category=category_filter)
    if date_from:
        expenses = expenses.filter(date__gte=date_from)
    if date_to:
        expenses = expenses.filter(date__lte=date_to)
    if search_query:
        expenses = expenses.filter(title__icontains=search_query)

    # --- Current Month Summary Logic ---
    today = timezone.now().date()
    current_year = today.year
    current_month = today.month

    monthly_expenses = Expense.objects.filter(date__year=current_year, date__month=current_month)
    total_spent = monthly_expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    category_breakdown = (
        monthly_expenses.values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    context = {
        'expenses': expenses,
        'categories': Expense.CATEGORY_CHOICES,
        'total_spent': total_spent,
        'category_breakdown': category_breakdown,
        'current_month_name': today.strftime('%B %Y'),
    }
    return render(request, 'expenses/expense_list.html', context)

def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form, 'title': 'Add Expense'})

def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form': form, 'title': 'Edit Expense'})

def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})