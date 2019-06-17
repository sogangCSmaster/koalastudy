from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    if request.GET.get('username'):
        username = request.GET.get('username')
        tempText = "안녕하세요. " + request.GET.get('username') + "님!"

        study = "코알라"

        return render(request, 'mainfolder/index.html',{'username': username, 'study': study})

    return render(request, 'mainfolder/index.html', {})