from .views import index, contact, about, services, testimonials, consultancy, engineering, oil_and_gas, jenitorial, civil_works, logistics_and_haulvage, real_estates, general_contract

from django.urls import path


app_name = "index"
urlpatterns = [

	path('', index, name='index'),
	path('about/', about, name='about'),
	path('contact/', contact, name='contact'),
	path('services/<str:name>', services, name='services'),
	path('testimonials/', testimonials, name='testimonials'),
	path('services/consultancy/', consultancy, name='consultancy'),
	path('services/engineering/', engineering, name='engineering'),
	path('services/oil-and-gas', oil_and_gas, name='oil_and_gas'),
	path('services/jenitorial/', jenitorial, name='jenitorial'),
	path('services/civil_works/', civil_works, name='civil_works'),
	path('services/logistics-and-haulvage/', logistics_and_haulvage, name='logistics_and_haulvage'),
	path('services/real-estates/', real_estates, name='real_estates'),
	path('services/general-contract/', general_contract, name='general_contract'),



] 