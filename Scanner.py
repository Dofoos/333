## By Nicolas Alonso
#
import numpy
import nmap3
import csv
import pandas
from ast import literal_eval

disco = nmap3.Nmap()
dis_host = nmap3.NmapHostDiscovery()
arp = dis_host.nmap_arp_discovery('localhost')
honk = disco.nmap_subnet_scan('localhost')

#writes to cvs attempts to sort

# pandas

#numpy
t = literal_eval(honk)
result_array = numpy.arrat([[v[j] for j in ['addr','addrtype','hostname','ptr','ports']] for k, v in t.items()])
print(result_array)
# sort dict ?
keys = honk.keys()
values = honk.values()
print('keys:', str(keys))
priny('values:', str(values))
se = pandas.Series(honk)
print(se)
print('SUBNET SCAN:\n__________\n',honk)
print('ARP DISCOVERY SCAN: \n___________\n' , arp)