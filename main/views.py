from django.shortcuts import render , redirect ,get_object_or_404
from . forms import CreateUserForm , AddPostForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from .models import PostModel
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})



@login_required()
def home(request):
    all_posts = PostModel.objects.all()
    data = {'posts':all_posts,'title':'All posts'}
    return render(request,'index.html',data)

@login_required()
def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid:
            w = form.save(commit=False)
            w.user = request.user
            w.save()
            return redirect('home')
    form = AddPostForm()
    data = {'form':form,'title':'Add post'}
    return render(request,'addpost.html',data)

@login_required()
def userposts(request):
    posts = PostModel.objects.filter(user=request.user)
    data = {'posts':posts,'title':'My posts'}
    return render(request,'index.html',data)
    
@login_required()
def edit(request,id):
    object = get_object_or_404(PostModel,pk = id,user=request.user)
    if request.method == 'POST':
        form = AddPostForm(request.POST,instance=object)
        if form.is_valid:
            form.save()
            return redirect('home')
    form = AddPostForm(instance=object)
    data = {'form':form,'title':'Edit post'}
    return render(request,'addpost.html',data)


class Detail_View(LoginRequiredMixin,DetailView):
    model = PostModel
    template_name = 'detail_view.html'
    context_object_name = 'post'
    
    
@login_required()
def delete(request,pk):
    object = get_object_or_404(PostModel,pk = pk,user=request.user)
    if request.method == 'POST':
        object.delete()
        return redirect('home')
    return render(request,'delete.html')
