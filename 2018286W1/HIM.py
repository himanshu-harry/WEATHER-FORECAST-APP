import urllib.request
import datetime

date = datetime.date.today()


json='{"cod":"200","message":0.0053,"cnt":40,"list":[{"dt":1536418800,"main":{"temp":302.33,"temp_min":300.745,"temp_max":302.33,"pressure":992.32,"sea_level":1016.91,"grnd_level":992.32,"humidity":87,"temp_kf":1.59},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":76},"wind":{"speed":3.65,"deg":82.5023},"rain":{"3h":0.3525},"sys":{"pod":"n"},"dt_txt":"2018-09-08 15:00:00"},{"dt":1536429600,"main":{"temp":298.53,"temp_min":297.341,"temp_max":298.53,"pressure":993.18,"sea_level":1017.55,"grnd_level":993.18,"humidity":97,"temp_kf":1.19},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10n"}],"clouds":{"all":76},"wind":{"speed":3.06,"deg":88.0066},"rain":{"3h":6.6525},"sys":{"pod":"n"},"dt_txt":"2018-09-08 18:00:00"},{"dt":1536440400,"main":{"temp":298.85,"temp_min":298.051,"temp_max":298.85,"pressure":992.17,"sea_level":1016.56,"grnd_level":992.17,"humidity":96,"temp_kf":0.79},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":44},"wind":{"speed":3.33,"deg":74.0078},"rain":{"3h":0.1325},"sys":{"pod":"n"},"dt_txt":"2018-09-08 21:00:00"},{"dt":1536451200,"main":{"temp":298.23,"temp_min":297.829,"temp_max":298.23,"pressure":991.81,"sea_level":1016.39,"grnd_level":991.81,"humidity":96,"temp_kf":0.4},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":24},"wind":{"speed":3.45,"deg":78.0027},"rain":{"3h":0.0024999999999995},"sys":{"pod":"n"},"dt_txt":"2018-09-09 00:00:00"},{"dt":1536462000,"main":{"temp":299.817,"temp_min":299.817,"temp_max":299.817,"pressure":993.56,"sea_level":1018.05,"grnd_level":993.56,"humidity":96,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02d"}],"clouds":{"all":8},"wind":{"speed":4.66,"deg":99.0011},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-09 03:00:00"},{"dt":1536472800,"main":{"temp":303.053,"temp_min":303.053,"temp_max":303.053,"pressure":993.9,"sea_level":1018.2,"grnd_level":993.9,"humidity":87,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":24},"wind":{"speed":5.65,"deg":106},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-09 06:00:00"},{"dt":1536483600,"main":{"temp":304.124,"temp_min":304.124,"temp_max":304.124,"pressure":992.2,"sea_level":1016.42,"grnd_level":992.2,"humidity":80,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":20},"wind":{"speed":5.86,"deg":112.004},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-09 09:00:00"},{"dt":1536494400,"main":{"temp":303.468,"temp_min":303.468,"temp_max":303.468,"pressure":992.16,"sea_level":1016.49,"grnd_level":992.16,"humidity":77,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":4.57,"deg":107.503},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-09 12:00:00"},{"dt":1536505200,"main":{"temp":300.67,"temp_min":300.67,"temp_max":300.67,"pressure":994.45,"sea_level":1018.84,"grnd_level":994.45,"humidity":84,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":4.12,"deg":99.0033},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-09 15:00:00"},{"dt":1536516000,"main":{"temp":299.645,"temp_min":299.645,"temp_max":299.645,"pressure":995.11,"sea_level":1019.67,"grnd_level":995.11,"humidity":87,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":12},"wind":{"speed":4.05,"deg":112.001},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-09 18:00:00"},{"dt":1536526800,"main":{"temp":298.56,"temp_min":298.56,"temp_max":298.56,"pressure":994.29,"sea_level":1018.84,"grnd_level":994.29,"humidity":89,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02n"}],"clouds":{"all":8},"wind":{"speed":2.96,"deg":131.501},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-09 21:00:00"},{"dt":1536537600,"main":{"temp":297.545,"temp_min":297.545,"temp_max":297.545,"pressure":994.91,"sea_level":1019.48,"grnd_level":994.91,"humidity":94,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":76},"wind":{"speed":1.97,"deg":125.003},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-10 00:00:00"},{"dt":1536548400,"main":{"temp":299.645,"temp_min":299.645,"temp_max":299.645,"pressure":996.46,"sea_level":1020.92,"grnd_level":996.46,"humidity":92,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":56},"wind":{"speed":2.3,"deg":90.0016},"rain":{"3h":0.010000000000002},"sys":{"pod":"d"},"dt_txt":"2018-09-10 03:00:00"},{"dt":1536559200,"main":{"temp":303.299,"temp_min":303.299,"temp_max":303.299,"pressure":996.52,"sea_level":1021,"grnd_level":996.52,"humidity":85,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":4.06,"deg":94.5057},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-10 06:00:00"},{"dt":1536570000,"main":{"temp":305.239,"temp_min":305.239,"temp_max":305.239,"pressure":994.45,"sea_level":1018.71,"grnd_level":994.45,"humidity":75,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02d"}],"clouds":{"all":8},"wind":{"speed":4.57,"deg":101.503},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-10 09:00:00"},{"dt":1536580800,"main":{"temp":304.32,"temp_min":304.32,"temp_max":304.32,"pressure":993.68,"sea_level":1017.93,"grnd_level":993.68,"humidity":70,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":56},"wind":{"speed":4.01,"deg":100.504},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-10 12:00:00"},{"dt":1536591600,"main":{"temp":302.023,"temp_min":302.023,"temp_max":302.023,"pressure":994.87,"sea_level":1019.47,"grnd_level":994.87,"humidity":74,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":36},"wind":{"speed":3.61,"deg":102.005},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-10 15:00:00"},{"dt":1536602400,"main":{"temp":300.509,"temp_min":300.509,"temp_max":300.509,"pressure":995.42,"sea_level":1020,"grnd_level":995.42,"humidity":82,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":48},"wind":{"speed":2.91,"deg":124.005},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-10 18:00:00"},{"dt":1536613200,"main":{"temp":299.425,"temp_min":299.425,"temp_max":299.425,"pressure":994.45,"sea_level":1019.02,"grnd_level":994.45,"humidity":87,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":80},"wind":{"speed":2.16,"deg":118.505},"rain":{"3h":0.004999999999999},"sys":{"pod":"n"},"dt_txt":"2018-09-10 21:00:00"},{"dt":1536624000,"main":{"temp":297.955,"temp_min":297.955,"temp_max":297.955,"pressure":994.49,"sea_level":1018.95,"grnd_level":994.49,"humidity":99,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":1.95,"deg":97.5033},"rain":{"3h":2.28},"sys":{"pod":"n"},"dt_txt":"2018-09-11 00:00:00"},{"dt":1536634800,"main":{"temp":297.85,"temp_min":297.85,"temp_max":297.85,"pressure":995.68,"sea_level":1020.08,"grnd_level":995.68,"humidity":100,"temp_kf":0},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":1.66,"deg":99.0032},"rain":{"3h":8.8},"sys":{"pod":"d"},"dt_txt":"2018-09-11 03:00:00"},{"dt":1536645600,"main":{"temp":299.965,"temp_min":299.965,"temp_max":299.965,"pressure":995.71,"sea_level":1020.08,"grnd_level":995.71,"humidity":100,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":88},"wind":{"speed":1.46,"deg":80.5005},"rain":{"3h":2.28},"sys":{"pod":"d"},"dt_txt":"2018-09-11 06:00:00"},{"dt":1536656400,"main":{"temp":302.519,"temp_min":302.519,"temp_max":302.519,"pressure":993.18,"sea_level":1017.53,"grnd_level":993.18,"humidity":93,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":64},"wind":{"speed":1.96,"deg":75.5015},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-11 09:00:00"},{"dt":1536667200,"main":{"temp":302.739,"temp_min":302.739,"temp_max":302.739,"pressure":992.06,"sea_level":1016.44,"grnd_level":992.06,"humidity":85,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":24},"wind":{"speed":2.12,"deg":88.0018},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-11 12:00:00"},{"dt":1536678000,"main":{"temp":299.41,"temp_min":299.41,"temp_max":299.41,"pressure":993.38,"sea_level":1017.72,"grnd_level":993.38,"humidity":92,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":12},"wind":{"speed":1.51,"deg":87.5032},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-11 15:00:00"},{"dt":1536688800,"main":{"temp":297.564,"temp_min":297.564,"temp_max":297.564,"pressure":993.4,"sea_level":1017.82,"grnd_level":993.4,"humidity":93,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":12},"wind":{"speed":1.25,"deg":74.5001},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-11 18:00:00"},{"dt":1536699600,"main":{"temp":296.802,"temp_min":296.802,"temp_max":296.802,"pressure":992.03,"sea_level":1016.5,"grnd_level":992.03,"humidity":94,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.26,"deg":79.5036},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-11 21:00:00"},{"dt":1536710400,"main":{"temp":296.173,"temp_min":296.173,"temp_max":296.173,"pressure":991.85,"sea_level":1016.34,"grnd_level":991.85,"humidity":94,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.31,"deg":121.003},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-12 00:00:00"},{"dt":1536721200,"main":{"temp":300.686,"temp_min":300.686,"temp_max":300.686,"pressure":993.18,"sea_level":1017.61,"grnd_level":993.18,"humidity":97,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":24},"wind":{"speed":1.91,"deg":165.5},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-12 03:00:00"},{"dt":1536732000,"main":{"temp":303.788,"temp_min":303.788,"temp_max":303.788,"pressure":993.08,"sea_level":1017.43,"grnd_level":993.08,"humidity":90,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":32},"wind":{"speed":1.76,"deg":221},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-12 06:00:00"},{"dt":1536742800,"main":{"temp":302.426,"temp_min":302.426,"temp_max":302.426,"pressure":991.03,"sea_level":1015.22,"grnd_level":991.03,"humidity":95,"temp_kf":0},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":{"all":36},"wind":{"speed":1.56,"deg":316.502},"rain":{"3h":3.46},"sys":{"pod":"d"},"dt_txt":"2018-09-12 09:00:00"},{"dt":1536753600,"main":{"temp":302.478,"temp_min":302.478,"temp_max":302.478,"pressure":990.21,"sea_level":1014.56,"grnd_level":990.21,"humidity":88,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":36},"wind":{"speed":1.61,"deg":44.0002},"rain":{"3h":1.63},"sys":{"pod":"d"},"dt_txt":"2018-09-12 12:00:00"},{"dt":1536764400,"main":{"temp":299.715,"temp_min":299.715,"temp_max":299.715,"pressure":991.13,"sea_level":1015.64,"grnd_level":991.13,"humidity":93,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":44},"wind":{"speed":1.32,"deg":126.004},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-12 15:00:00"},{"dt":1536775200,"main":{"temp":298.71,"temp_min":298.71,"temp_max":298.71,"pressure":991.51,"sea_level":1016.01,"grnd_level":991.51,"humidity":93,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":76},"wind":{"speed":1.76,"deg":188.508},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-12 18:00:00"},{"dt":1536786000,"main":{"temp":296.057,"temp_min":296.057,"temp_max":296.057,"pressure":990.74,"sea_level":1015.32,"grnd_level":990.74,"humidity":94,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":32},"wind":{"speed":1.51,"deg":218.501},"rain":{"3h":2.65},"sys":{"pod":"n"},"dt_txt":"2018-09-12 21:00:00"},{"dt":1536796800,"main":{"temp":295.779,"temp_min":295.779,"temp_max":295.779,"pressure":990.66,"sea_level":1015.31,"grnd_level":990.66,"humidity":93,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":24},"wind":{"speed":1.17,"deg":227.501},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-13 00:00:00"},{"dt":1536807600,"main":{"temp":299.024,"temp_min":299.024,"temp_max":299.024,"pressure":992.09,"sea_level":1016.58,"grnd_level":992.09,"humidity":95,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":12},"wind":{"speed":1.62,"deg":38},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-13 03:00:00"},{"dt":1536818400,"main":{"temp":303.546,"temp_min":303.546,"temp_max":303.546,"pressure":992.52,"sea_level":1016.87,"grnd_level":992.52,"humidity":90,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.12,"deg":315.508},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-13 06:00:00"},{"dt":1536829200,"main":{"temp":305.937,"temp_min":305.937,"temp_max":305.937,"pressure":990.5,"sea_level":1014.7,"grnd_level":990.5,"humidity":80,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.22,"deg":285.001},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-13 09:00:00"},{"dt":1536840000,"main":{"temp":302.799,"temp_min":302.799,"temp_max":302.799,"pressure":989.94,"sea_level":1014.06,"grnd_level":989.94,"humidity":88,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":0},"wind":{"speed":1.52,"deg":256},"rain":{"3h":0.77},"sys":{"pod":"d"},"dt_txt":"2018-09-13 12:00:00"}],"city":{"id":1273294,"name":"Delhi","coord":{"lat":28.6517,"lon":77.2219},"country":"IN","population":10927986}}'

#to get weather forecast which is going to be stored in json variable ,specific location and apikey are to be taken as input during testing, which will provide weather_response
#After that, this program take values of specific date and time we are interested in from a1test.py and result as according to further defined functions



def weather_response(location, API_key):

	
	report=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key)
	json=str(report.read())
	
	return json
	 

 
def has_error(location,json): 
	s=json.rfind("\"name\"")
	h=json.find(":",s)
	p=json.find(",",h)

	name=json[h+2:p-1]

	if name==location:
		return False
	else:
		return True
 

#for gettting temperature the logic used is to first find date and time then find  'temp' and then find ':'and then find ',' and take value from ':'+1 to ','
def get_temperature (json, n, t):
	 
	tday=str(date +datetime.timedelta(days=n))
	d=(tday+" "+t)
	him=json.find(d)

	tp=json.rfind("\"temp\"",0,him)

	cp=json.find(":",tp)

	comp=json.find(",",tp)

	p=json[cp+1:comp]

	return	float(p)
# we use same logic for finding humidity, wind, pressure , sealevel:

def get_humidity(json, n ,t):
	
	tday=str(date +datetime.timedelta(days=n))
	d=(tday+" "+t)
	him=json.find(d) 
	

	hp=json.rfind("\"humidity\"",0,him)
	cp2=json.find(":",hp)
	comp2=json.find(",",hp)
	h=json[cp2+1:comp2]

	
	return	float(h) 

def get_pressure(json, n ,t):
	
	tday=str(date +datetime.timedelta(days=n))
	d=(tday+" "+t)
	him=json.find(d)
	

	pop=json.rfind("\"pressure\"",0,him)
	cp3=json.find(":",pop)
	comp3=json.find(",",pop)
	pp=json[cp3+1:comp3]
	
	return	float(pp)

def get_wind(json, n ,t):
	 
	tday=str(date +datetime.timedelta(days=n))
	d=(tday+" "+t)
	him=json.find(d)
	

	wop=json.rfind("\"speed\"",0,him)
	cp4=json.find(":",wop)
	comp4=json.find(",",wop)
	w=json[cp4+1:comp4]
	
	return	float(w)

def get_sealevel(json, n ,t):
	
	tday=str(date +datetime.timedelta(days=n))
	d=(tday+" "+t)
	him=json.find(d)


	sop=json.rfind("\"sea_level\"",0,him)
	cp5=json.find(":",sop)
	comp5=json.find(",",sop)
	sp=json[cp5+1:comp5]
	
	return	float(sp)

