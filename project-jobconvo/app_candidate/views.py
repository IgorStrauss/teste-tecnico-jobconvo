from django.shortcuts import render


# Create your views here.
def home_candidate_view(request):
    return render(request, 'home_candidate.html')
