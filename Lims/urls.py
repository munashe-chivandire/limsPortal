from django.urls import path
from Lims import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index' ),
    path('login', views.login, name='login' ),
    path('topics', views.topics, name='topics' ),
    path('knowledge_center', views.knowledge_center, name='knowledge_center' ),
    path('CONPI_certificate', views.CONPI_certificate, name='CONPI_certificate' ),
    path('enquiries_faq', views.enquiries_faq, name='enquiries_faq' ),
    path('CONPI_Application_Form', views.CONPI_Application_Form, name='CONPI_Application_Form' ),
    path('get_conpi/', views.get_conpi, name='get_conpi' ),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)