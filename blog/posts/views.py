from django.shortcuts import render, get_object_or_404,redirect
from posts.models import Post, Category, Comment
from django.contrib.auth.decorators import login_required
from posts.forms import PostCreationForm, CommentForm
from django.db.models import Q, Count, Avg, Sum
from django.contrib.auth.decorators import login_required
from posts.forms import PostCreationForm
from django.db.models import Q,Count
# Create your views here.

def post_list_view(request):
    try:
        query = request.GET.get('query','')
        category_id = request.GET.get('category_id','')
        status = request.GET.get('status','')
        
        posts = Post.objects.select_related('category','author')
        
        if query:
          posts = posts.filter(
              Q(title__icontains=query) |
              Q(content__icontains=query) |
              Q(author__username__icontains=query)
    )#search
          
        if category_id :
            posts = posts.filter(category_id=category_id)
        if status:
            posts = posts.filter(status = status )

        post_summary_list = []

        for post in posts:
            post_summary_list.append(
                {
                    "id": post.id,
                    "title": post.title,
                    "content": post.content[:100],
                    "category": post.category,
                    "created_at":post.created_at
                }
            )
            
        my_total = None
        my_categories = None
        if request.user.is_authenticated:
            my_total = Post.objects.filter(author=request.user).aggregate(
                total_posts=Count('id')
            )
        #   per author koita post korse total post eikhane ache 

        my_categories = Category.objects.annotate(
            post_count = Count('posts'))

        # all single category te koita post ache oita dekhabe 
        


        return render(
            request=request,
            template_name='post_list.html',
            context={
                'post_summary':post_summary_list,
                'categories':Category.objects.all(),
                'status_choices':Post.STATUS_CHOICES,
                'query':query,
                'selected_category':category_id,
                'selected_status':status,
                'my_total':my_total,
                "my_categories":my_categories,
                "result_count":len(post_summary_list)
            }
        )
    except Exception as e:
         return render(
            request=request,
            template_name='error.html',
            context={'error':e}
        )


def post_detail_view(request,pk):
    try:
        post = Post.objects.get(id=pk)
        parent_comments = post.comments.filter(parent__isnull=True).select_related('parent')

        form = CommentForm()
        if request.method == "POST" and request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                parent_id = request.POST.get('parent_id')
                if parent_id:
                    comment.parent = Comment.objects.get(id=parent_id)
                comment.save()
                return redirect('post_detail',pk=post.id)
        return render(
            request=request,
            template_name='post_detail.html',
            context={
                'post':post,
                'parent_comments':parent_comments,
                'form':form
            }
        )
    except Exception as e:
         return render(
            request=request,
            template_name='error.html',
            context={'error':e}
        )


@login_required
def post_create_view(request):
    try:
        form = PostCreationForm()

        if request.method == "POST":
            form = PostCreationForm(request.POST)
            category_id = request.POST.get('category')
            category = Category.objects.get(id=category_id)

            if form.is_valid():
                post = Post(
                    title=request.POST.get('title'),
                    content=request.POST.get('content'),
                    category=category,
                    author=request.user
                )
                post.save()
                return redirect('post_list')

        return render(
            request=request,
            template_name='post_creation.html',
            context={'form': form}
        )

    except Exception as e:
        return render(
            request=request,
            template_name='error.html',
            context={'error': e}
        )


# @login_required
# def post_create_view(request):

#     if request.method == "POST":
#         form = PostCreationForm(request.POST)

#         if form.is_valid():
#             category_id = request.POST.get('category')
#             category = Category.objects.get(id=category_id)

#             post = Post(
#                 title=form.cleaned_data['title'],
#                 content=form.cleaned_data['content'],
#                 category=category,
#                 author=request.user
#             )

#             post.save()

#             return redirect('home')

#     else:
#         form = PostCreationForm()

#     return render(
#         request,
#         'post_creation.html',
#         {'form': form}
#     )