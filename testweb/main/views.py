from django.http import HttpResponse
from django.shortcuts import render

datas = [
    {
        'author': '코알라',
        'content': '우리는 코알라에서 웹 코딩을 배우고 있습니다.',
        'publishedAt': '2019-07-01'
    }
]


def main(request):
    if request.method=="POST":
        author = request.POST['author']
        content = request.POST['content']
        datas.append({
            'author': author,
            'content': content,
            'publishedAt': '2019-07-02'
        })
    return render(request, 'mainfolder/index.html', {'datas': datas})