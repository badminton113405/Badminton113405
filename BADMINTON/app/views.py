from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def community(request):
    comments = [
        {'text': '一起打球嗎', 'editing': False},
        {'text': '有人要一起上團課嗎', 'editing': False}
    ]
    return render(request, 'community.html', {'comments': comments})