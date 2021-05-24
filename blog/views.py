from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView,FormView,CreateView
from django.core.paginator import Paginator


class PostHomeView(ListView):
	model=Post
	template_name='blog/home.html'
	context_object_name='posts'
	ordering=['-time_added']
	paginate_by=8

	def get_context_data(self,**kwargs):
		context=super(PostHomeView, self).get_context_data(**kwargs)
		context['User']=User.objects.all()
		return context
#page_obj      current page 
#page_obj   current pge number
#page_obj.object_list      pages in current page
#page_obj.paginator.number     current page t0 numbe

class UserPostView(ListView):
    model = Post
    template_name = 'blog/user_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self,**kwargs):
    	context=super(UserPostView,self).get_context_data(**kwargs)
    	context['User']=User.objects.all()
    	return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-time_added')


class PostDetailView(DetailView):
	model=Post
	context_object_name='posts'

class CreatePostView(LoginRequiredMixin, CreateView):
	model=Post
	fields=['content','HashTag']
	def form_valid(self,form):
		form.instance.author=self.request.user
		form.instance.HashTag='' if not form.instance.HashTag else form.instance.HashTag
		return super(CreatePostView, self).form_valid(form)

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,  DeleteView):
	model=Post
	success_url=reverse_lazy('blog-home')

	def test_func(self):
		data = self.get_object()
		return self.request.user==data.author

class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model=Post
	fields=['content','HashTag']

	def form_valid(self,form):
		form.instance.author=self.request.user
		form.instance.HashTag='' if not form.instance.HashTag else form.instance.HashTag

		return super(UpdatePostView, self).form_valid(form)

	def test_func(self):
		data = self.get_object()
		return self.request.user==data.author

