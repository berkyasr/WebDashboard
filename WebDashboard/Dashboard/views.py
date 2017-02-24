from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.
from wd.app import Application
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

count = 0
loaded = False
try:
    _app
except:
    _app = Application()
    _app.load('mblog')
    _app.load('poll')
    _app.load('moneyrate')
    _app.load('weather')
    _app.load('gallery')
    _app.load('note')
    _app.load('clock')
    _app.load('sticky')

def insertmblog(request):
    global count
    if request.method == 'POST':
        oid = _app.addInstance("mblog", count, 0)
        _app.callMethod(oid,"setWriterName",[request.POST['writer']])
        _app.callMethod(oid,"setTopic",[request.POST['topic']])
        _app.callMethod(oid,"saveEntry",[request.POST['writer'],request.POST['entry']])
        count += 1
        return redirect("/")

    return render(request,'insertmblog.html')
@login_required(login_url='/login')
def mainpage(request):
    global loaded
    global count
    count = _app.id_counter
    return render(request, 'mainpage.html', context={
        'components': [_app.callMethod(key,"execute",[]) for key in _app.instances().keys()],
        'user': request.user.username
    })

def create(request):
    if request.method == 'POST':
        return redirect("/insert" + request.POST['componenttype'])

    return render(request, 'create.html', context={
        'modules': _app.loaded()
    })

def viewmblog(request, id):
    if request.method == 'POST':
        _app.callMethod(id, "saveEntry", [request.POST['writer'], request.POST['entry']])

    return render(request, "mblog.html", context={
        'history':  _app.callMethod(id, "execute", [])
    })

def mbloglist(request):
    x = ''
    for i, j in _app.instances().iteritems():
        if (j[0] == 'mblog'):
            x += '<tr><th><a href = "/' + i + '"> ' + _app.callMethod(i,'getTopic') + '</a> </th><th>' + _app.callMethod(i,'getWriterName')+ '</th></tr>'
    return render(request, "mbloglist.html", context={
        'table' : x
    })

@csrf_exempt
def likedislike(request,id,entry):
    _app.callMethod(id,request.POST['option'],[int(entry)])
    return redirect("/" + id)

def insertpoll(request):
    global count
    if request.method == 'POST':
        id = _app.addInstance("poll", count, 0)
        _app.callMethod(id, "setCreator", [request.POST['creator']])
        _app.callMethod(id, "setName", [request.POST['name']])
        for line in request.POST['entry'].split():
            _app.callMethod(id, "addOption", [line])
        count += 1
        return redirect("/")
    return render(request, "insertpoll.html")

def viewpoll(request,id):
    return render(request, "poll.html", context={
        'history':  _app.callMethod(id, "execute", [])
    })

@csrf_exempt
def votepoll(requet,id,entry):
    _app.callMethod(id,"vote",[entry])
    return redirect("/" + id)

def polllist(request):
    x = ''
    for i, j in _app.instances().iteritems():
        if (j[0] == 'poll'):
            x += '<tr><th><a href = "/' + i + '"> ' + _app.callMethod(i,'getName') + '</a> </th><th>' + _app.callMethod(i,'getCreator')+ '</th></tr>'
    return render(request, "polllist.html", context={
        'table' : x
    })

def insertweather(request):
    global count
    if request.method == 'POST':
        if request.POST['insweather'] == "Auto location":
            _app.addInstance("weather", count, 0)
            count += 1
            return redirect("/")
        if request.POST['location'] == "":
            return render(request, 'insertweather.html')
        oid = _app.addInstance("weather", count, 0)
        _app.callMethod(oid,"setLocation",[request.POST['location']])
        count += 1
        return redirect("/")
    return render(request, 'insertweather.html')
    
def insertgallery(request):
    global count
    if request.method == 'POST':
        id = _app.addInstance("gallery", count, 0)
        _app.callMethod(id, "setName", [request.POST['galleryname']])
        for line in request.POST['photos'].split('\n'):
            _app.callMethod(id, "addPhoto", [line])
        count += 1
        return redirect("/")
    return render(request, "insertgallery.html")

    
def viewgallery(request,id):
    return render(request, "gallery.html", context={
        'history':  _app.callMethod(id, "execute", [])
    })
def insertsticky(request):
    global count
    if request.method=='POST':
        id = _app.addInstance("sticky", count, 0)
        _app.callMethod(id, "setName", [request.POST['stickyname']])
        for line in request.POST['notes'].split('\n'):
            print line
            _app.callMethod(id, "addNote", [line])
        count += 1
        return redirect("/")
    return render(request, "insertsticky.html")
        
def viewsticky(request,id):
    return render(request,"sticky.html", context={
        'name' : _app.callMethod(id,"getName",[]),
        'notes': _app.callMethod(id,"getNotes",[])
    })

def viewclock(request):
    return render(request, "clock.html")

def insertclock(request):
    global count
    if request.method == 'POST':
        id = _app.addInstance("clock", count,0)
        count += 1
        return redirect("/")
    return render(request,"insertclock.html")
@csrf_exempt
def gallerymove(request,id):
    _app.callMethod(id,request.POST['option'],[])
    return redirect("/" + id)

def moneys(request):
    if request.method == 'POST':
        id = _app.addInstance("moneyrate", count, 0)
        _app.callMethod(id, "setBase", [request.POST['basename']])
        count += 1
    x = _app.callMethod("moneyrate1","execute",[])
    print x
    print "asdasda"
    return render(request, "moneys.html", context={
        'table' : x
    })

def insertmoneyrate(request):
    global count
    if request.method == 'POST':
        id = _app.addInstance("moneyrate", count, 0)
        _app.callMethod(id, "setBase", [request.POST['basename']])
        count += 1
        # return redirect("/")
    return render(request, "insertmoneyrate.html")

def saveorload(request):
    global count
    if request.method == 'POST':
        if request.POST['designaction'] == "Save":
            _app.saveDesign(request.user.username)
        else: # request.POST.['designaction'] == "Load"
            _app.loadDesign(request.POST['loadname'])
            count = len(_app.instances()) + 1
        return redirect("/")

    return render(request, 'saveorload.html', context={
        'designs': _app.loadableDesigns()
    })

def insertnote(request):
    global count
    if request.method == 'POST':
        id = _app.addInstance("note", count, 0)
        _app.callMethod(id, "setName", [request.POST['name']])
        for line in request.POST['entry'].split('\n'):
            _app.callMethod(id, "addElement", [line])
        count += 1
        return redirect("/")
    return render(request, "insertnote.html")

@csrf_exempt
def deleteelement(request,id,element):
    _app.callMethod(id,"deleteElement",[int(element)])
    return redirect("/" + id)

def viewnote(request,id):
    return render(request, "note.html", context={
        'history':  _app.callMethod(id, "execute", [])
    })

def notelist(request):
    x = ''
    for i, j in _app.instances().iteritems():
        if (j[0] == 'note'):
            x += '<tr><th><a href = "/' + i + '"> ' + _app.callMethod(i, 'getName') + '</a></th></tr>'
    return render(request, "notelist.html", context={
        'table': x
    })
    
def loginpage(request):
    if request.method == 'POST':
        if request.POST.get("login")=="1":
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                _app.loadDesign(request.POST['username'])

            return redirect("/")

        if request.POST.get("register")=="1":
            print request.POST['username']
            if not (User.objects.filter(username=request.POST['username'])):
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                user.save()
                login(request,user)
                _app.loadDesign("Fresh")
                _app.saveDesign(request.POST['username'])
                return redirect("/")
            return redirect("/")

    return render(request, "login_register.html")

def logout_view(request):
    logout(request)
    return redirect("/login")

def save(request):
    _app.saveDesign(request.user.username)
    return redirect("/")
