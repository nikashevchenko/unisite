from django.urls import path
from myunisite import views

urlpatterns = [
    path("", views.main_page_view, name="main_page"),
    path('programs/', views.program_list, name='program_list'),
    path('programs/<int:place_id>/',views.program_detail, name='program_detail'),
    path('deparment/', views.department_list, name='department_list' ),
    path('deparment/<int:department_id>/',views.department_detail, name='department_detail'),

]