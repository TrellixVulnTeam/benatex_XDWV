from django.shortcuts import render

def index(request):
	return render(request, 'rough.html', {})
def contact(request):
	return render(request, 'contact.html', {})
def about(request):
	return render(request, 'about.html', {})
def services(request,name):
	return render(request, 'services.html', {})
def testimonials(request):
	return render(request, 'testimonials.html', {}) 
def consultancy(request):
	return render(request, 'consultancy.html', {})
def engineering(request):
	return render(request, 'engineering.html', {})
def oil_and_gas(request):
	return render(request, 'oil_and_gas.html', {})
def jenitorial(request):
	return render(request, 'jenitorial.html', {})
def civil_works(request):
	return render(request, 'civil_works.html', {})
def logistics_and_haulvage(request):
	return render(request, 'logistics_and_haulvage.html', {})
def real_estates(request):
	return render(request, 'real_estates.html', {})
def general_contract(request):
	return render(request, 'general_contract.html', {})
