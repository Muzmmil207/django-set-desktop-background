import ctypes

import requests
from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

P = settings.BACKGROUND_PICTURE

def find_Wallpapers(request):
    '''This view searches and fetches data from Pixabay API and displays it to the user'''

    q = request.GET.get('q', '') # get search query

    URL = f'https://pixabay.com/api/?key=28649987-1dbe522815c3603c4504c8384&image_type=photo&q=HD&q={q}&per_page=200'
    response = requests.get(URL).json()
    data = response['hits']

    p = Paginator(data, 16)
    page = request.GET.get('page')
    pictures = p.get_page(page)

    return render(request, 'index.html', {'pictures': pictures})


def set_new_background(request):
    '''This view sets a new background on the desktop'''
    
    if request.method == 'POST':
        url = request.POST.get('url')
        r = requests.get(url, timeout=0.5)
        if r.status_code == 200:
            with open(f'{P}/picture.jpg', 'wb') as f:
                f.write(r.content)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{P}/picture.jpg' , 0)
    
    return JsonResponse('done', safe=False)
