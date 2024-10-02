from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, Update_BlogForm
from .models import BlogPost
from django.contrib import messages

app_name = 'Blogs'

# Home view
def home(request):
    if request.user.is_authenticated:
        return redirect('Blogs:blogs')
    else:
        return render(request, 'Blogs/index.html')

# Blog creation view
@login_required
def blog_create_view(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads (images)
        if form.is_valid():
            blog_post = form.save(commit=False)  # Create the blog post but don't save it yet
            blog_post.user = request.user  # Assign the current user as the blog post author
            blog_post.save()  # Now save the blog post
            return redirect('Blogs:myblogs')  # Redirect to user's blogs
        else:
            return render(request, 'Blogs/blog_form.html', {'form': form, 'errors': form.errors})
    else:
        form = BlogForm()

    return render(request, 'Blogs/blog_form.html', {'form': form})



# View for user's blogs
@login_required
def user_blog_view(request):
    user_blogs = BlogPost.objects.filter(user=request.user)
    return render(request, 'Blogs/user_blogs.html', {'user_blogs': user_blogs})

# View to show all blogs
def blogs_view(request):
    blogs = BlogPost.objects.all().order_by('-date')
    return render(request, "Blogs/blogs.html", {'blogs': blogs})

# View to show individual blog post
def blog_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'Blogs/blog.html', {'post': post})

@login_required
def user_blog_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'Blogs/user_blog.html', {'post': post})

@login_required
def delete_blog_post(request, id):
    # Fetch the blog post by id and ensure it belongs to the current user
    post = get_object_or_404(BlogPost, id=id, user=request.user)

    if request.method == 'POST':
        post.delete()  # Delete the blog post
        messages.success(request, "Blog post deleted successfully.")
        return redirect('Blogs:myblogs')  # Redirect to the user's blogs page
    
    return render(request, 'Blogs/user_blogs.html')


@login_required
def update_blog_post(request, id):
    post = get_object_or_404(BlogPost, id=id, user=request.user)  # Fetch the blog and ensure the current user is the owner

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)  # Bind the existing post instance to the form
        if form.is_valid():
            form.save()  # Save the updated blog post
            messages.success(request, "Blog post updated successfully.")
            return redirect('Blogs:myblogs')  # Redirect to user's blog list after successful update
        else:
            messages.error(request, "Error updating the blog post.")
    else:
        form = BlogForm(instance=post)  # Prepopulate form with existing data for editing

    return render(request, 'Blogs/blog_form.html', {'form': form, 'is_edit': True, 'post': post})
