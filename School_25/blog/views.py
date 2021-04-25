from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

# Create your views here.
def ShowAllPost(request):
    all_post = Post.objects.all().order_by('id')
    paginator = Paginator(all_post,4,orphans=2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/showPost.html', {'posts':page_obj})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 2

    # def get_context_data(self, *args, **kwargs):
    #     try:
    #         return super(PostListView, self).get_context_data(*args, **kwargs)
    #     except:
    #         self.kwargs['page'] = 1
    #         return super(PostListView, self).get_context_data(*args, **kwargs)
            

    def paginate_queryset(self, queryset, page_size):
        try:
            return super(PostListView, self).paginate_queryset(queryset, page_size)
        except:
            self.kwargs['page'] = 1
            return super(PostListView, self).paginate_queryset(queryset, page_size)

class PostDetalView(DetailView):
    model = Post
    template_name = "blog/post.html"