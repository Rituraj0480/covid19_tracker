from django.shortcuts import render
import requests

def index(request):
	url = 'https://covid19.mathdro.id/api'
	url1 = url+'/countries/india'
	r = requests.get(url).json()
	r1 = requests.get(url1).json()
	data = {
		'confirmed': r['confirmed']['value'],
		'recovered': r['recovered']['value'],
		'deaths': r['deaths']['value'],
		'lastUpdate': r['lastUpdate']
	}
	data1 = {
		'confirmed': r1['confirmed']['value'],
		'recovered': r1['recovered']['value'],
		'deaths': r1['deaths']['value'],
		'lastUpdate': r1['lastUpdate']
	}

	return render(request, 'index.html', {'data':data, 'data1':data1})