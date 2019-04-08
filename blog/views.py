from django.shortcuts import render

posts = [
    {
        'author': 'giobaski  1',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 14,2019'
    },
    {
        'author': 'giobaski 2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 15,2019'
    }
]


# Create your views here.
def home(request):
    template_name = 'blog/home.html'
    context = {'posts': posts}
    return render(request, template_name, context)

def about(request):
    template_name = 'blog/about.html'
    return render(request, template_name, {'title': 'About'})