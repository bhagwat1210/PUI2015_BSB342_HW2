####PUI2015 3RD ASSIGNMENT
####AUTHOR : BHAGWAT SINGH BISHT


import sys
import urllib2
import json
import csv

if __name__=='__main__':
    url = ('http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2]))
    data = urllib2.urlopen(url)
    jdata = json.loads(data.read())
    jdata1 = jdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    with open(sys.argv[3], 'w') as busdatacsv:
        buswriter = csv.writer(busdatacsv, delimiter = ',')
        buswriter.writerow(("Latitude", "Longtitude", "Stop Name", "Stop Status"))
        for i in range(len(jdata1)):
            busLatitude = jdata1[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
            busLongitude = jdata1[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
            jdata2= jdata1[i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"]
            if jdata1[i]["MonitoredVehicleJourney"]["OnwardCalls"] != 'NA':
                for j in range(len(jdata2)):
                    stopName = jdata2[j]["StopPointName"]
                    busDistance = jdata2[j]["Extensions"]["Distances"]["PresentableDistance"]
                    buswriter.writerow((busLatitude, busLongitude, stopName, busDistance))
            else:
                buswriter.writerow((busLatitude, busLongtitude, "NA", "NA"))