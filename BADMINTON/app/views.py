from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def community(request):
    comments = [
        {'text': '一起打球嗎', 'editing': False},
        {'text': '有人要一起上團課嗎', 'editing': False}
    ]
    return render(request, 'community.html', {'comments': comments})

def beginner(request):
    return render(request, 'beginner.html')

def competitive(request):
    return render(request, 'competitive.html')

def onetoone(request):
    return render(request, 'onetoone.html')

def zerodozen(request):
    return render(request, 'zerodozen.html')

def ZZT(request):
    return render(request, 'ZZT.html')

def HWH(request):
    return render(request, 'HWH.html')

def CYZ(request):
    return render(request, 'CYZ.html')

def ZBY(request):
    return render(request, 'ZBY.html')