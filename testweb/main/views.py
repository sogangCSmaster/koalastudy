from django.http import HttpResponse
from django.shortcuts import render
import time

startTime = time.time()

datas = [
    {
        'author': '코알라',
        'content': '우리는 코알라에서 웹 코딩을 배우고 있습니다.',
        'publishedAt': startTime
    }
]


def main(request):
    if request.method=="POST":
        author = request.POST['author']
        content = request.POST['content']
        currentTime = time.time()

        datas.append({
            'author': author,
            'content': content,
            'publishedAt': currentTime
        })

    return render(request, 'mainfolder/index.html', {'datas': datas})