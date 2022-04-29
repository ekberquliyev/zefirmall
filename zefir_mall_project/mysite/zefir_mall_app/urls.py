from django.urls import path

from .views import index_view,about_detail_view,rent_detail_view,foodcort_detail_view,company_detail_view

urlpatterns = [
    path('', index_view, name='index_page'),
    path("about/", about_detail_view, name='about' ),
    path("rent/", rent_detail_view, name='rent' ),
    path("foodcort/", foodcort_detail_view, name='foodcort' ),
    path("company/", company_detail_view, name='company' ),

]
