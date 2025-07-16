from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'portfolioapp1/index.html')

def resume(request):
    return render(request,'portfolioapp1/resume.html')


