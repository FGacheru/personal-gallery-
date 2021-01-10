from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Location,Category

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my Gallery')

def home(request):
    '''
    Method to return all images, locations, categories
    '''
    images = Image.objects.all()
    location = Location.objects.all()
    categories = Category.get_all_categories()
    context = {
        "images":images,
        "location":location,
        "categories": categories,
    }
    
    return render(request, 'all-images/home.html', context)

def search_results(request):
    '''
    Method to search by location or category
    '''
    if 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Picture.search_by_category(search_term)
       
        message = f"{search_term}"
        return render(request, 'photo/search.html', {"message":message, "images":searched_images})
    elif 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Picture.search_by_location(search_term)
        message = f"{search_term}"    

        return render(request, 'all-images/search.html', {"message":message, "images":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html', {"message":message})

def view_image(request,image_id):
    '''
    Method to get image by id
    '''
    try:
        image = Image.objects.get(id =  image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-images/view.html", {"image":image})

def category(request, id):
    '''
    Method to search by images or category
    '''
    # categories = Category.get_all_categories()
    images = Image.objects.filter(category__id=id)
    context = {
        "categories":categories,
        "images":images
    }
    return render(request, 'all-images/home.html', context)
