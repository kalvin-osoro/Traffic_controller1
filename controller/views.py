from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# Create your views here.
def home(request):
    
    return render(request, 'controller/home.html')


def about(request):
<<<<<<< HEAD
     context={
        'posts':Post.objects.all()
    }
     return render(request, 'controller/about.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'controller/about.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','route','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','route','description']

   
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    
    
=======
    return render(request, 'controller/about.html', {'title': 'About'})


>>>>>>> a7d36c52cbf72f2b9d0bfb9ec0b0f8e1d3c33e8f

