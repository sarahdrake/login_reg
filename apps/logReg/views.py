from django.shortcuts import render, redirect, HttpResponse
from .models import User
# Create your views here.
def index(request):
    # print User.objects.log('bob@bob.com','Thisbetterwork1')
    # User.objects.log(email='bob@bob.com', password='helloworld')
    context = {
        'users': User.objects.all(),
        'test': User.objects.filter(email='bob@bob.com', pw_hash='$2b$12$rRw2kVxPLqfZgx17TUvkJ.3kBZCyhDNfQ4kNvAQHZOI8.nc29YpXK'),

    }
    # print len(User.objects.filter(email='bob@bob.com', pw_hash='$2b$12$rRw2kVxPLqfZgx17TUvkJ.3kBZCyhDNfQ4kNvAQHZOI8.nc29YpXK'))
    return render(request, 'logReg/index.html', context)
def process(request):
    if request.method == 'POST':
        user_check = User.objects.reg(request.POST['first'], request.POST['last'], request.POST['email'], request.POST['password'], request.POST['confirm'])
        if user_check == False:
            return redirect('/')
        else:
            return redirect('/success')
def log_in(request):
    if User.objects.log(request.POST['elog'], request.POST['plog']) == False:
        print "it was false"
        return redirect('/')
    else:
        print "it was else"
        if 'id' not in request.session:
            print "why is session not being made?"
            request.session['id'] = User.objects.log(request.POST['elog'], request.POST['plog'])
            print "it might have worked"
            print request.session['id']

    return redirect('/success')

def success(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'logReg/success.html', context)

def log_off(request):
    del request.session['id']
    return redirect('/')
