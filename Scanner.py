## By Nicolas Alonso
#

import numpy
import nmap3
import csv
import pandas
from ast import literal_eval

# set up

disco = nmap3.Nmap()
dis_host = nmap3.NmapHostDiscovery
# user inputs

print('Local Host Scan:')
print('________________________________')
print('1) SUBNET SCAN:')
print('2) ARP DISCOVERY SCAN')
print('3) PORT SCAN TARGET IP')
whatdo = input('Make a Selection!  (1) or (2) or (3) \n>>>:')

try:    # not my most elegant input checker
    whatdo = int(whatdo)
    #print(type(whatdo)) # check
except:
    whatdo = 0

output = ''
# subnet scan
x = True
while x is True:
    try:
        if whatdo == 1:
            print('Scanning LocalHost...')
            honk = disco.nmap_subnet_scan('localhost')
            #se = pandas.Series(honk)
            #print('Panda:', se)
            print('SUBNET SCAN:\n__________\n', honk)
            output = honk
            x = False
        else:
            pass
        if whatdo == 2:
            print('Scanning LocalHost...')
            arp = dis_host.nmap_arp_discovery('localhost')
            print('ARP DISCOVERY SCAN: \n___________\n', arp)
            output = arp
            x = False
        else:
            pass
        if whatdo == 3:
            print('Target Scan')
            w = True
            while w is True:
                try:
                    target = input('Input target IP: \n>>>:')
                    scan = disco.scan_top_ports(target)
                except:
                    continue

                print('PORT SCAN:\n__________\n', scan)
                output = scan
                w = False
            else:
                w = False
            x = False
        else:
            pass
        if whatdo >=4:
            print('Scanning LocalHost...')
            print('Have Both:')
            honk = disco.nmap_subnet_scan('localhost')
            #se = pandas.Series(honk)
            #print('Panda:', se)
            print('SUBNET SCAN:\n__________\n', honk)
            arp = dis_host.nmap_arp_discovery('localhost')
            print('ARP DISCOVERY SCAN: \n___________\n', arp)
            output = arp, honk
            x = False
        else:
            pass
        if whatdo <=0:
            print('pass')
            x = False

    except:
        x = True



print('\n')
export = input('Export CSV? (1)-yes or (2)-no ? \n>>>:')
try:
    export = int(export)
except:
    export = 2

print(':', export)  # checks
print(type(output))

if export == 1:   # it prints both?
    print('Exporting...')
    with open('ScanData.csv','w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=':', quotechar=',')
        writer.writerows([output])

else:
    print('Goodbuy')


# attempt to format
#numpy
#t = literal_eval(honk)
#result_array = numpy.arrat([[v[j] for j in ['addr','addrtype','hostname','ptr','ports']] for k, v in t.items()])
#print(result_array)
# pandas
#se = pandas.Series(
# honk)
#print('Panda:',se)

