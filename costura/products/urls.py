from django.urls import path
from . import views

app_name="products"

urlpatterns= [
    path(route='',                          view=views.product_list,    name='list'),
    #path(route='add/', view=views.ProductCreateView.as_view(),name='add'),
    path(route='categories/',               view=views.category_list,   name='category_list'),
    path(route='categories/<slug:slug>',    view=views.product_category,name='product_by_category'),
    path(route='search/',                   view=views.product_search,  name='search_results'),
    path(route='<slug:slug>/',              view=views.product_detail,  name='detail'),
    #path(route='<slug:slug>/update/',view=views.ProductUpdateView.as_view(),name='update'),
]