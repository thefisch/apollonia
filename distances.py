from sys import argv
import urllib
import json

def main():
    script, filein, fileout = argv
    
    baseurl = 'http://maps.googleapis.com/maps/api/distancematrix/json?'
    
    coords = open(filein).readlines()
    coords_distance_time = open(fileout, 'w')
    
    for origin in coords:
        for destination in coords:
            disttime = json.load(urllib.urlopen(baseurl + 'origins=' + 
                       origin[:-1] + '&destinations=' + destination[:-1] + 
                       '&sensor=false'))

            status = disttime['rows'][0]['elements'][0]['status']
            
            if status == 'ZERO_RESULTS':
                distance = time = 'No Route'
            elif status == 'OK':
                distance = disttime['rows'][0]['elements'][0]['distance']['value']
                time = disttime['rows'][0]['elements'][0]['duration']['value']
            else: print 'strange'

            coords_distance_time.write('{},{},{},{}\n'.format(
            origin[:-1], destination[:-1], distance, time))

            print '{},{},{},{}'.format(
                  origin[:-1], destination[:-1], distance, time)
            
if __name__ == '__main__':
    main()