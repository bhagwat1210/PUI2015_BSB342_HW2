####PUI2015 3RD ASSIGNMENT
####AUTHOR : BHAGWAT SINGH BISHT

import sys
import urllib2
import json

if __name__=='__main__':    
    url = ('http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' \
           % (sys.argv[1], sys.argv[2]))
    data = urllib2.urlopen(url)
    jdata = json.loads(data.read())
    jdata1 = jdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    BusLine = sys.argv[2]
    print 'BusLine is  : %s' % (BusLine)
    BusCoordinate = []
    for i in jdata1:
            BusCoordinate.append(i["MonitoredVehicleJourney"]["VehicleLocation"])
    Bus = len(BusCoordinate)
    print 'Number of Buses : %i' % Bus
    for j in range(Bus):
        print 'Bus %d is at latitude %f and longitude %f' % (j, BusCoordinate[j]["Latitude"], BusCoordinate[j]["Longitude"])
