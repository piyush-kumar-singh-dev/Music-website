from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Album
from django.views import generic
from django.contrib.auth import authenticate,login,logout
from .myform import Register,Loginpage
# Create your views here.

def home(request):
     #return HttpResponse("<h1> it is home page of music website</h1>")
     #return render(request,'markup/home.html')
     a=Album.objects.all()
     #ht=''
     #for i in a:
     #     ht+='<h1>'+i.name+'</h1></br>'
     #return HttpResponse(ht)
     return render(request,'markup/home.html',{'data':a})

class Home(generic.ListView):
     template_name = 'markup/home.html'
     context_object_name = 'data' #default name is object
     def get_queryset(self):#it is used to prepare context data object
          return Album.objects.all()

def songpage(request,pk):
     #try:
     #     a=Album.objects.get(id=pk)
     #except:
     #     raise Http404("queried album doesnot exists")
     a=get_object_or_404(Album,id=pk)
     #ht=''
     #for s in a.song_set.all():
     #    ht+='<h1>'+s.name+'</h1></br>'
     #return HttpResponse(ht)
     return render(request,'markup/song.html',{'album':a})

class Songdetail(generic.DetailView):
     template_name = 'markup/song.html'
     context_object_name = 'album'
     model = Album

'''def signup(request):
     form=Register(None or request.POST)
     if form.is_valid():
          a=form.save(commit=False)
          p=form.cleaned_data.get("password")
          a.set_password(p)
          a.save()
          return HttpResponse("<h1>go to login page</h1>")
     return render(request,"markup/signup.html",{'form':form})

def signin(request):
     form=Loginpage(None or request.POST)
     if form.is_valid():
          u=form.cleaned_data.get('username')
          p=form.cleaned_data.get("password")
          user=authenticate(username=u,password=p)
          if user:
               login(request,user)
               return HttpResponse("logged in succesfully"+request.user.username)
     return render(request,'markup/signup.html',{'form':form}) '''

class Signup(generic.View):
     def get(self,request):
          form=Register(None)
          return render(request, "markup/signup.html", {'form': form})
     def post(self,request):
          form = Register(request.POST)
          if form.is_valid():
               a = form.save(commit=False)
               p = form.cleaned_data.get("password")
               a.set_password(p)
               a.save()
               return HttpResponse("<h1>go to login page</h1>")
          return render(request, "markup/signup.html", {'form': form})

class Signin(generic.View):
     def get(self,request):
          form=Loginpage(None)
          return render(request, 'markup/signup.html', {'form': form})
     def post(self,request):
          form = Loginpage(request.POST)
          if form.is_valid():
               u = form.cleaned_data.get('username')
               p = form.cleaned_data.get("password")
               user = authenticate(username=u, password=p)
               if user:
                    login(request, user)
                    return HttpResponse("logged in succesfully" + request.user.username)
          return render(request, 'markup/signup.html', {'form': form})