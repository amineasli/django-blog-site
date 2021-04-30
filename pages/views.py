from django.shortcuts import render

def about_page(request):
    
    return render(request, 'pages/about_page.html')
