from django.shortcuts import render
import requests
from django.http import JsonResponse

def index(request):
	url = 'https://covid19.mathdro.id/api'
	url1 = url+'/countries/india'
	r = requests.get(url).json()
	r1 = requests.get(url1).json()
	data = {
		'confirmed': r['confirmed']['value'],
		'recovered': r['recovered']['value'],
		'deaths': r['deaths']['value'],
		'lastUpdate': r['lastUpdate'].split('T')[0]
	}
	data1 = {
		'confirmed': r1['confirmed']['value'],
		'recovered': r1['recovered']['value'],
		'deaths': r1['deaths']['value'],
		'lastUpdate': r1['lastUpdate'].split('T')[0]
	}

	return render(request, 'index.html', {'data':data, 'data1':data1})


def search(request):
	return render(request, 'search.html')

def ajax_search(request):
	if request.is_ajax and request.method == "GET":
		country = request.GET.get("country")
		url = 'https://covid19.mathdro.id/api/countries/' + str(country)
		r = requests.get(url).json()
		data = {
			'confirmed': r['confirmed']['value'],
			'recovered': r['recovered']['value'],
			'deaths': r['deaths']['value'],
			'lastUpdate': r['lastUpdate'].split('T')[0]
		}

		return JsonResponse({"data":data})


def about(request):
	return render(request, 'about.html')