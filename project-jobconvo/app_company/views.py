from django.shortcuts import render


# Create your views here.
def home_company_view(request):
    return render(request, 'home_company.html')
