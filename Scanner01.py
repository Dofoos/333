## By Nicolas Alonso
#

import numpy
import nmap3
import csv
import pandas
from ast import literal_eval

# set up

disco = nmap3.Nmap()
dis_host = nmap3.NmapHostDiscovery()

# user inputs
print('________________________________')
print('1) SUBNET SCAN:')
print('2) ARP DISCOVERY SCAN')
whatdo = input('Make a Selection!  (1) or (2) \n>>>:')

try:
    whatdo = int(whatdo)
    print(type(whatdo)) # check
except:
    pass

print('Scanning LocalHost...')
# subnet scan
x = True
while x is True:
    try:
        if whatdo == 1:
            honk = disco.nmap_subnet_scan('localhost')
            se = pandas.Series(honk)
            print('Panda:', se)
            print('SUBNET SCAN:\n__________\n', honk)
            x = False
        else:
            pass
        if whatdo == 2:
            arp = dis_host.nmap_arp_discovery('localhost')
            print('ARP DISCOVERY SCAN: \n___________\n', arp)
            x = False
        if whatdo >= 3:
            print('Have Both:')
            honk = disco.nmap_subnet_scan('localhost')
            se = pandas.Series(honk)
            print('Panda:', se)
            print('SUBNET SCAN:\n__________\n', honk)
            arp = dis_host.nmap_arp_discovery('localhost')
            print('ARP DISCOVERY SCAN: \n___________\n', arp)
            x = False
        if whatdo <= 0:
            print('Have Both:')
            honk = disco.nmap_subnet_scan('localhost')
            se = pandas.Series(honk)
            print('Panda:', se)
            print('SUBNET SCAN:\n__________\n', honk)
            arp = dis_host.nmap_arp_discovery('localhost')
            print('ARP DISCOVERY SCAN: \n___________\n', arp)
            x = False
        else:
            pass
    except:
        x = True

print('\n')
export = print(input('Export CSV? (y) or (n) ? \n>>>:'))
export = str(export)
print(':',export)
if export == 'y' or 'Y':   # it prints both? 
    print('Exporting...')
    # export to csv
if export != 'y' or 'Y':
    print('goodbuy')



#numpy
#t = literal_eval(honk)
#result_array = numpy.arrat([[v[j] for j in ['addr','addrtype','hostname','ptr','ports']] for k, v in t.items()])
#print(result_array)

# pandas
#se = pandas.Series(honk)
#print('Panda:',se)

#writes to cvs attempts to sort
#output
#print('SUBNET SCAN:\n__________\n',honk)
#print('ARP DISCOVERY SCAN: \n___________\n' , arp)