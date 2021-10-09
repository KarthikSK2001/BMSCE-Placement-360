from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment,Postint,CategoryInt,Commentint
from .forms import PostForm, EditForm, CommentForm,PostIntForm,EditIntForm,CommentIntForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
#def home(request):
#	return render(request, 'home.html', {})

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	
	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def LikeIntView(request, pk):
	postint = get_object_or_404(Postint, id=request.POST.get('postint_id'))
	liked = False
	if postint.likes_int.filter(id=request.user.id).exists():
		postint.likes_int.remove(request.user)
		liked = False
	else:
		postint.likes_int.add(request.user)
		liked = True
	
	return HttpResponseRedirect(reverse('article_int-detail', args=[str(pk)]))

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	cats = Category.objects.all()
	ordering = ['-post_date']
	#ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class HomeView(ListView):
	model = Postint
	template_name = 'home.html'
	cats_int = CategoryInt.objects.all()
	ordering = ['-post_date']
	#ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		cat_menu = CategoryInt.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryIntListView(request):
	cat_menu_list_int = CategoryInt.objects.all()
	return render(request, 'category_list_int.html', {'cat_menu_list_int':cat_menu_list_int})

def CategoryView(request, cats):
	category_posts = Post.objects.filter(year_of_hiring=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats':cats.replace('-', ' ').title(), 'category_posts':category_posts})

def CategoryIntView(request, cats_int):
	category_posts_int = Postint.objects.filter(year_of_hiring=cats_int.replace('-', ' '))
	return render(request, 'categories_int.html', {'cats_int':cats_int.replace('-', ' ').title(), 'category_posts_int':category_posts_int})


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()	
		
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class ArticleDetailIntView(DetailView):
	model = Postint
	template_name = 'article_details_int.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = CategoryInt.objects.all()
		context = super(ArticleDetailIntView, self).get_context_data(*args, **kwargs)
		
		stuff = get_object_or_404(Postint, id=self.kwargs['pk'])
		total_likes_int = stuff.total_likes_int()	
		
		liked = False
		if stuff.likes_int.filter(id=self.request.user.id).exists():
			liked = True

		context["cat_menu"] = cat_menu
		context["total_likes_int"] = total_likes_int
		context["liked"] = liked
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'

class AddIntPostView(CreateView):
	model = Postint
	form_class = PostIntForm
	template_name = 'add_post_int.html'

def Contact(request):
	return render(request, 'contact.html')

def Resources(request):
	return render(request, 'resources.html')

def Links(request):
	return render(request, 'links.html')

def Pdfs(request):
	return render(request, 'pdfs.html')

def Aptitude(request):
	return render(request, 'aptitude.html')

def WebDev(request):
	return render(request, 'webdevroadmap.html')

def AppDev(request):
	return render(request, 'appdevroadmap.html')

def CyberSecurity(request):
	return render(request, 'cybersecurityroadmap.html')

def DataScience(request):
	return render(request, 'datascience.html')

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)
 
	success_url = reverse_lazy('home')

class AddCommentIntView(CreateView):
	model = Commentint
	form_class = CommentIntForm
	template_name = 'add_comment_int.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.postint_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'
	#fields = ('title', 'body')

class AddCategoryIntView(CreateView):
	model = CategoryInt
	#form_class = PostForm
	template_name = 'add_category_int.html'
	fields = '__all__'
	#fields = ('title', 'body')
	
class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title', 'title_tag', 'body']

class UpdatePostIntView(UpdateView):
	model = Postint
	form_class = EditIntForm
	template_name = 'update_post_int.html'
	#fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

class DeletePostIntView(DeleteView):
	model = Postint
	template_name = 'delete_post_int.html'
	success_url = reverse_lazy('home')