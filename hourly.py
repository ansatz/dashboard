#WHAT
#get hourly weather forecast
#export to android phone

import urllib2 
import json 
from collections import namedtuple

#[what]
class hourly(object):
	def apiRequest(self): pass
	def getHourly(self): pass
	def android(self): pass

#[how]
#class wunder(hourly):
def api():
		#http://api.wunderground.com/api/c72cc9fdb28f4f9d/hourly/q/IL/Chicago.json
		#try:
		f = urllib2.urlopen('http://api.wunderground.com/api/c72cc9fdb28f4f9d/hourly/astronomy/geolookup/conditions/q/IL/Chicago.json') 
		json_string = f.read() 
		#except:
		#json_string=file.open(json.log,'r')
		parsed_json = json.loads(json_string) 
		b = dict(parsed_json) #copy
		with open('json.log','w') as ff:
			json.dump(parsed_json,ff,sort_keys=True, indent=4)
			#s=str(b)
			#ff.write(s)
	
		ff.closed
		
		location = parsed_json['location']['city'] 
		temp_f = parsed_json['current_observation']['temp_f'] 
			 
		sunup = parsed_json['moon_phase']['sunrise']
		sundown = parsed_json['moon_phase']['sunset']
	
		#Hourly = namedtuple('FCTTIME', 'civil,metric,english')
		#weather = [Hourly(**k) for k in Hourly["weather"]]
		#hourly =  parsed_json['FCTTIME']['civil']
	
		#CVL = [ v for k,v in parsed_json['FCTTIME'].iteritems() if k==['civil'] ]
		#print CVL
		#Civil=[]
		#for v in parsed_json: #.iteritems():
	
		hrl=parsed_json['hourly_forecast']
		#print 'hours', hrl
		#if 'civil' in hrl:
		#	print '{0},{1}'.format(hrl)	
		#print '*array', hrl[0]
		#print '*dict', hrl[0]['FCTTIME']
		#print '*dict22', hrl[0]['FCTTIME']['civil']
		rez = [ ( _dict['FCTTIME']['civil'], _dict['FCTTIME']['weekday_name_abbrev'], _dict['temp'], _dict['condition'] ) \
				for _dict in parsed_json['hourly_forecast'] ]
		#print '*rez', rez, #\n
	
		#hours = [ v for k,v in hrl[0]['FCTTIME'].iteritems() if k==['civil']]
		# or key==['weekday_name_abbrev'] ] 
		#print '*lstcmp',hours
		#hrl2 = hrl['FCTTIME']['civil']
		#civil=[ i["civil"] for i in hrl ]
		#dayz= [ j['weekday_name'] for j in hrl ]
		#print civil, dayz
		#temp_hour = [k for k in parsed_json['temp']]
			 
		print "Current temperature in %s is: %s" % (location, temp_f)
		print "sunrise is at %s:%s. \n sunset is at %s:%s" %(sunup['hour'],sunup['minute'],sundown['hour'],sundown['minute'])
	#	print "%s HOUR %s: %s" %( [ (_dict['weekday_name_abbrev'],_dict['civil'],_dict['condition']) for _dict in rez ])
	#	print "%s HOUR %s: %s" %( [ (i[1],i[0],i[3]) for i in rez ])
		for i in rez:
			print "%s %s: %sC %sF %s" % (i[1],i[0],i[2]['metric'],i[2]['english'],i[3]) 
	#		print "%sC %sF" %(i[2]['metric'],i[2]['english'])
		
		#print "%s HOUR %s: %s \n\t %sC %sF" %(rez['weekday_name_abbrev'],rez['civil'],rez['wx'],rez['temp']['metric'],rez['temp']['english'])
	#	print "\t %sC %sF" %(rez['temp']['metric'],rez['temp']['english'])
		#print "HOURLY WEATHR ", hours 
	#	print "hourly kwargs unpack", weather
		f.close()


#def highlightChanges()
#def sendAndroid

if __name__ == "__main__":
	api()

