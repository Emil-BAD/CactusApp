from django.shortcuts import render

def main(request):
    return render(request, 'CactusApp/index.html')

def more(request):
    return render(request, 'CactusApp/more.html')

def facts(request):
    return render(request, 'CactusApp/facts.html')

def photos(request):
    return render(request, 'CactusApp/photos.html')

def author(request):
    return render(request, 'CactusApp/author.html')