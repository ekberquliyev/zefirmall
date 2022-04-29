from multiprocessing import context
from django.shortcuts import render

from zefir_mall_app.models import about, foodcort, rent,company

# Create your views here.
def index_view(request):
    context = {}
    return render(request,'index.html',context)

def about_detail_view(request):
    context = {}
    text_queryset = about.objects.all()
    context['text_queryset'] = text_queryset
    return render(request,'About.html',context)

def rent_detail_view(request):
    context = {}
    rent_queryset = rent.objects.all()
    context['rent_queryset'] = rent_queryset
    return render(request, 'icare.html', context)

def foodcort_detail_view(request):
    context = {}
    foodcort_queryset = foodcort.objects.all()
    context['foodcort_queryset'] = foodcort_queryset
    return render(request, 'fudkort.html', context)

def company_detail_view(request):
    context = {}
    company_queryset = company.objects.all()
    context['company_queryset'] = company_queryset
    return render(request, 'kampaniyalar.html', context)