from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from django.http import HttpResponse
from .forms import TicketForm, CreateUserForm, CreateTickeForm
from .models import *
from .filters import TicketFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user= form.save()

            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user
            )
            messages.success(request, "Account was created for " + username)
            return redirect('login')
    context={'form':form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')
    
    return render(request, 'accounts/login.html')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    
    tickets = Ticket.objects.all()

    customers = Customer.objects.all()

    resolved = tickets.filter(status='Resolved').count()
    pending = tickets.filter(status='Pending').count()
    inprogress = tickets.filter(status='InProgess').count()
    open = tickets.filter(status='Open').count()
    myFilter = TicketFilter(request.GET, queryset=tickets)
    tickets = myFilter.qs
    
    total_customers = customers.count()
    total_tickets = tickets.count()

    context ={'tickets': tickets, 'customers': customers,'total_customers': total_customers,
     'total_tickets':total_tickets,'resolved': resolved, 'pending' : pending, 'inprogress': inprogress
      ,'open': open, 'myFilter':myFilter}
    
    return render(request, 'accounts/dashboard.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    tickets = request.user.customer.ticket_set.all()
    resolved = tickets.filter(status='Resolved').count()
    pending = tickets.filter(status='Pending').count()
    inprogress = tickets.filter(status='InProgess').count()
    open = tickets.filter(status='Open').count()
    total_tickets = tickets.count()
    customer=request.user.customer
    context={'tickets':tickets,'total_tickets':total_tickets,'resolved': resolved, 'pending' : pending, 'inprogress': inprogress
      ,'open': open,'customer': customer}
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tickets(request):
    tickets = Ticket.objects.all()
    context ={'tickets':tickets}
    return render(request, 'accounts/tickets.html',context)
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    tickets = customer.ticket_set.all()
    ticket_count = tickets.count()
    context = {'customer':customer, 'tickets': tickets, 'ticket_count':ticket_count}
    return render(request, 'accounts/customers.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def createTicket(request,pk):
    customer = Customer.objects.get(id=pk)
    form = CreateTickeForm(initial={'customer':customer})
    if request.method == 'POST':
        
        form = CreateTickeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    
    return render(request, 'accounts/ticket_form.html', context)

@login_required(login_url='login')
def updateTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)
    if request.method == 'POST':
        
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'accounts/ticket_form.html', context)

@login_required(login_url='login')
def deleteTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == "POST":
        ticket.delete()
        return redirect('/')
    context={'item': ticket}
    return render(request, 'accounts/delete.html', context)