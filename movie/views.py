from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView

"""from rest_framework import viewsets,status,Response,APIView"""
from .models import Post
from .serializer import PostSerializer

#from django.http import HttpResponse

"""
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all
    serializer_class = PostSerializer
"""
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'movie/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'movie/home.html'
    context_object_name = 'posts'
    ordering = ['-release_date']

class PostDetailView(DetailView):
    model = Post 

class PostCreateView(CreateView):
    model = Post 
    fields = ['title', 'rating', 'release_date']

    def form_valid(self, form):
        form.instance.rating = "PG"
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post 
    fields = ['title', 'rating','release_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post 
    success_url = '/'

def about(request):
    return render(request, 'movie/about.html')

# Create your views here.
