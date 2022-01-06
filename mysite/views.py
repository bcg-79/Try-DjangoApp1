from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ExpAccountForm, ExpTransactionsForm
from .models import ExpAccounts, ExpTransactions

@login_required
def home(request):
    form = ExpTransactionsForm(request.POST or None)
    data = {'form': form}

    try:
        active_acc = ExpAccounts.objects.filter(status=1, user_acc=request.user).get()
        last_tx = ExpTransactions.objects.filter(exp_acc=active_acc).order_by('-id')[:10]
    except ExpAccounts.DoesNotExist:
        active_acc = None
        last_tx = None

    # data = {'active_acc': active_acc, 'last_tx': last_tx}
    data['active_acc'] = active_acc
    data['last_tx'] = last_tx

    if form.is_valid():
        add_spend = form.cleaned_data.get('add_spend')
        amount = form.cleaned_data.get('amount')
        p_name = form.cleaned_data.get('person_name')
        cat = form.cleaned_data.get('category')
        extra_note = form.cleaned_data.get('extra_note')

        if add_spend == 0:
            if amount > active_acc.rem_amount:
                messages.add_message(request, messages.WARNING, 'Your Account Balance is LOW.')
                return redirect(reverse('mysite:home'))
            else:
                active_acc.rem_amount = active_acc.rem_amount - amount
                active_acc.save()
        elif add_spend == 1:
            active_acc.rem_amount = active_acc.rem_amount + amount
            active_acc.save()

        new_exp = ExpTransactions(add_spend=add_spend, amount=amount, person_name=p_name, category=cat, extra_note=extra_note, exp_acc=active_acc)
        new_exp.save()


        form = ExpTransactionsForm()
        data['form'] = form
        data['exp_msg'] = f'Transaction Successfull for {amount}'

    
    return render(request, 'mysite/pages/home.html', data)


@login_required
def expaccounts(request):
    form = ExpAccountForm(request.POST or None)
    data = {'form': form}

    # all_acc = ExpAccounts.objects.filter(user_acc=request.user)
    # def_acc = ExpAccounts.objects.filter(status=1, user_acc=request.user).get()
    # paginator = Paginator(all_acc, 10)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # # data = {'page_obj': page_obj, 'def_acc': def_acc}
    # data['page_obj'] = page_obj
    # data['def_acc'] = def_acc
    
    try:
        print("First Try block...")
        all_acc = ExpAccounts.objects.filter(user_acc=request.user)
        paginator = Paginator(all_acc, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except ExpAccounts.DoesNotExist:
        print("First except block")
        


    try:
        print("Second Try block...")
        def_acc = ExpAccounts.objects.filter(status=1, user_acc=request.user).get()
    except ExpAccounts.DoesNotExist:
        print("second Except block...")
        def_acc = None

    

    
    # data = {'page_obj': page_obj, 'def_acc': def_acc}
    data['page_obj'] = page_obj
    data['def_acc'] = def_acc

    if form.is_valid():
        acc_name = form.cleaned_data.get("acc_name")
        acc_type = form.cleaned_data.get("acc_type")
        acc_amt = form.cleaned_data.get("initial_amount")
        
        acc = ExpAccounts(acc_name=acc_name, acc_type= acc_type, initial_amount=acc_amt, rem_amount=acc_amt, user_acc=request.user)
        acc.save()
        form = ExpAccountForm()
        data['form'] = form
        data['s_msg'] = f"{acc_name} Create Successfully."
        
        return redirect(reverse('mysite:expaccounts'))
   

    return render(request, 'mysite/pages/accounts.html', data)

@login_required
def set_default_acc(request):
    
    if request.method == 'POST':
        cur_acc_id = request.POST.get('acc_id')

        old_defalt_acc = ExpAccounts.objects.filter(status=1, user_acc=request.user)
        new_def_acc = ExpAccounts.objects.get(pk=cur_acc_id)

        if old_defalt_acc:
            if len(old_defalt_acc) > 1:
                for x in old_defalt_acc:
                    x.status = 0
                    x.save()
            else:
                old_defalt_acc[0].status = 0
                old_defalt_acc[0].save()

        new_def_acc.status = 1
        new_def_acc.save()

        return redirect(reverse('mysite:expaccounts'))

    return redirect(reverse('mysite:expaccounts'))

@login_required
def all_transactions(request):

    try:
        active_acc = ExpAccounts.objects.filter(status=1, user_acc=request.user).get()
    except ExpAccounts.DoesNotExist:
        active_acc = None

    all_acc = ExpAccounts.objects.filter(user_acc=request.user)
    
    if request.method == 'POST':
       acc_id = request.POST.get('acc_id')
       active_acc.status = 0
       active_acc.save()
       active_acc = ExpAccounts.objects.get(pk=acc_id)
       active_acc.status = 1
       active_acc.save()

    all_tx_data = ExpTransactions.objects.filter(exp_acc=active_acc)
    paginator = Paginator(all_tx_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    no_of_tx = len(ExpTransactions.objects.filter(exp_acc=active_acc))
    spend_tx = len(ExpTransactions.objects.filter(exp_acc=active_acc, add_spend=0))
    add_tx = len(ExpTransactions.objects.filter(exp_acc=active_acc, add_spend=1))

    data = {
        'active_acc': active_acc,
        'all_acc': all_acc,
        'no_of_tx': no_of_tx,
        'spend_tx': spend_tx,
        'add_tx': add_tx,
        'page_obj': page_obj,
        }

    return render(request, 'mysite/pages/all_transactions.html', data)