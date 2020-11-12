from django.views.generic import ListView, DetailView
from .models import Blog
# Create your views here.

class IndexView(ListView):
    model = Blog
    queryset = Blog.objects.filter(status='published').all(). \
        order_by('-published_at')
    template_name = 'blog/list_view.html'
    context_object_name = 'index_post_list'


class DetailedView(DetailView):
    model = Blog
    template_name = 'blog/detail_view.html'
    context_object_name = 'blog_object'