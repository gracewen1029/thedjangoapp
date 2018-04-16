from django.shortcuts import render

# Credef home_page(request):

def home_page(request):
	return render(request, 'blog/home_page.html')
