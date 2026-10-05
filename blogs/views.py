from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blogs.models import BlogModel, User


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists')
            return render(request, 'register.html')

        if password != conf_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')

        User.objects.create_user(
            username=username,
            full_name=full_name,
            email=email,
            password=password,
        )
        messages.success(request, 'Registration successful')
        return redirect('login_page')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')

        messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_page')


def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        author_name = request.POST.get('author_name', '').strip()
        content = request.POST.get('content', '').strip()
        category = request.POST.get('category')
        blog_image = request.FILES.get('blog_image')

        if not title or not author_name or not content or not category:
            messages.error(request, 'Please fill in all fields')
            return render(request, 'blog-add.html')

        if BlogModel.objects.filter(title=title).exists():
            messages.error(request, 'Blog with this title already exists')
            return render(request, 'blog-add.html')

        BlogModel.objects.create(
            title=title,
            author_name=author_name,
            content=content,
            category=category,
            blog_image=blog_image,
        )
        messages.success(request, 'Blog Added Successfully')
        return redirect('blog_list_page')

    return render(request, 'blog-add.html')


def blog_edit(request, b_id):
    blog = BlogModel.objects.filter(id=b_id).first()
    if blog is None:
        return redirect('blog_list_page')

    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author_name')
        content = request.POST.get('content')
        category = request.POST.get('category')
        blog_image = request.FILES.get('blog_image')

        if not title or not author_name or not content or not category:
            messages.error(request, 'Please fill in all fields')
            return render(request, 'blogedit.html', {'blog': blog})

        if BlogModel.objects.filter(title=title).exclude(id=b_id).exists():
            messages.error(request, 'Blog with this title already exists')
            return render(request, 'blogedit.html', {'blog': blog})

        blog.title = title
        blog.author_name = author_name
        blog.content = content
        blog.category = category
        if blog_image:
            blog.blog_image = blog_image
        blog.save()

        messages.success(request, 'Blog Updated Successfully')
        return redirect('blog_list_page')

    return render(request, 'blogedit.html', {'blog': blog})


def blog_list(request):
    blogs = BlogModel.objects.all()
    return render(request, 'blog-list.html', {'data': blogs})


def delete(request, b_id):
    BlogModel.objects.filter(id=b_id).delete()
    messages.success(request, 'Blog deleted successfully')
    return redirect('blog_list_page')

