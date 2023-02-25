from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "products": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23, 567, 7676, 5465767]
    }
    return render(request, 'home/index.html', context=context)
