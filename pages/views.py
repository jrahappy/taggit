from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import PageForm
from .models import Page
from taggit.models import Tag

def index(request):
    pages = Page.objects.all()
    tags = Tag.objects.all()
    context = {
        "pages": pages,
        "tags": tags,
    }
    return render(request, "pages/index.html", context)

def index_filter(request, tag):
    pages = Page.objects.filter(tags__name=tag)
    tags = Tag.objects.all()
    context = {
        "pages": pages,
        "tags": tags,
    }
    return render(request, "pages/index.html", context) 

def page_create(request):
    form = PageForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PageForm()
        return redirect("pages:index")
    context = {
        "form": form
    }
    return render(request, "pages/page_create.html", context)

def page_update(request, pk):
    page = Page.objects.get(pk=pk)
    form = PageForm(request.POST or None, instance=page)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "pages/page_update.html", context)

def page_delete(request, pk):
    page = Page.objects.get(pk=pk)
    page.delete()
    return render(request, "pages/page_delete.html")

def page_detail(request, pk):
    page = Page.objects.get(pk=pk)
    context = {
        "page": page
    }
    return render(request, "pages/page_detail.html", context)   

def page_search(request):
    if request.method == POST:
        if request.POST['search']:
            search = request.POST['search']
            pages = Page.objects.filter(title__icontains=search)
            return render(request, "pages/home.html", {"pages": pages})
    else:
        return render(request, "pages/home.html")

    return render(request, "pages/home.html")

    
def home(request):
    pages = Page.objects.all()
    context = {
        "pages": pages,
    }
    return render(request, "pages/home.html", context)
   


def about(request):
    return render(request, "pages/about.html")