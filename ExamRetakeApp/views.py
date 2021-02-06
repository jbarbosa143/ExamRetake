from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    print(request.POST)
    resultFromValidator = User.objects.registerValidator(request.POST)
    print("Results from val below")
    print('************************************************************************************************************')
    print(resultFromValidator)
    if len(resultFromValidator) > 0:
        for key, value in resultFromValidator.items():
            messages.error(request, value)
        return redirect('/')
    newuser = User.objects.create(email_address = request.POST['email'],password =request.POST['pw'])
    request.session['loggedinid'] = newuser.id
    return redirect('/success')

def success(request):
    loggedinuser = User.objects.get(id = request.session['loggedinid'])
    userinfo = Quote.objects.all()
    notfavored = Quote.objects.exclude(favoredquote = loggedinuser)
    useruploaded = Quote
    context ={
        'loggedinuser' : loggedinuser,
        'userinfo' : userinfo,
        'likedquotes': Quote.objects.filter(favoredquote=loggedinuser),
        'notfavored' : notfavored
    }
    return render(request,'success.html',context)

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    resultFromValidator = User.objects.loginValidator(request.POST)
    if len(resultFromValidator) > 0:
        for key, value in resultFromValidator.items():
            messages.error(request,value)
        return redirect('/')
    Emaildata =  User.objects.filter(email_address = request.POST['email'])
    request.session['loggedinid'] = Emaildata[0].id
    return redirect('/success')

def info(request,userid):
    loggedinuser = User.objects.get(id = request.session['loggedinid'])
    userquotes = Quote.objects.filter(added_by= userid)
    context = {
    "loggedinuser": loggedinuser,
    "userquotes" : userquotes,
    'user': User.objects.get(id=userid),
    'totalquotescount': len(userquotes)
    }
    return render(request,'info.html',context)

def delete(request,quoteid):
    deletequote = Quote.objects.get(id=quoteid)
    deletequote.delete()
    return redirect('/success')

def like(request,quoteid):
    loggedinuser= User.objects.get(id=request.session['loggedinid'])
    additem = User.objects.get(id=request.session['loggedinid']).favoredaquote.add(Quote.objects.get(id=quoteid))
    return redirect('/success')

def edit(request,quoteid):
    editquote = Quote.objects.get(id=quoteid)
    context = {
        'editquote' : editquote
    }
    return render(request,'edit.html',context)

def unlike(request,quoteid):
    unlike = Quote.objects.get(id=quoteid).favoredquote.remove(User.objects.get(id = request.session['loggedinid']))
    return redirect('/success')

def update(request,quoteid):
    resultFromValidator =Quote.objects.quoteValidator(request.POST)
    if len(resultFromValidator) >0:
        for key,value in resultFromValidator.items():
            messages.error(request,value)
        return redirect(f'/edit/{quoteid}')
    updatequote = Quote.objects.get(id=quoteid)
    updatequote.quote =request.POST['message']
    updatequote.quoter =request.POST['quotedby']
    updatequote.save()
    return redirect('/success')

def create(request):
    resultFromValidator =Quote.objects.quoteValidator(request.POST)
    if len(resultFromValidator) >0:
        for key,value in resultFromValidator.items():
            messages.error(request,value)
        return redirect('/success')
    loggedinuser= User.objects.get(id=request.session['loggedinid'])
    Quote.objects.create(quote=request.POST['message'],quoter=request.POST['quotedby'],added_by=loggedinuser)
    return redirect('/success')