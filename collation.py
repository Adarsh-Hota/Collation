#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
         =====    =====    ||       ||             ====       ==========   ==========     =====    ||\\     ||
        ||       ||   ||   ||       ||           //   \\          ||           ||        ||   ||   || \\    ||
        ||       ||   ||   ||       ||          //     \\         ||           ||        ||   ||   ||  \\   ||
        ||       ||   ||   ||       ||         //=======\\        ||           ||        ||   ||   ||   \\  ||
        ||       ||   ||   ||       ||        //         \\       ||           ||        ||   ||   ||    \\ ||
         =====    =====     =====    =====   //           \\      ||       ==========     =====    ||     \\||


                  ╒ COLLATION════════════════════════════════════╕
                  │Python based script for Information Gathering.│
                  ╘══════════════════════════════════════════════╛
                  Adarsh Hota
"""

import json
import optparse
from sys import argv

from insides import *
from insides import functions

################################  Banner   ################################

os.system('clear')
print(Banner)
print('\r')

################################ Functions ################################

def reverseViaHT(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/reverseiplookup/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")



def geoip(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/geoip/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def pagelinks(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/pagelinks/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")




def dnslookup(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/dnslookup/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def findshareddns(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/findshareddns/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=w, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def heading(heading, website, color, afterWebHead):
    space = " " * 10
    var = str(heading + " '" + website + "'" + str(afterWebHead))
    length = len(var) + 1; 
    print("") # \n
    print("\n\n{color}" + var).format(color=color)
    print("{white}" + "-" * length + "--").format(white=w); 
    print("") # \n

################################  Args  ################################ 

_usage      = w + "collation.py " + w + "<code> " + w + "<website> " + w
parser      = optparse.OptionParser(usage=_usage, conflict_handler="resolve")
general     = optparse.OptionGroup(parser, c + 'Basic Help' + w)
general.add_option( '-h', '--help', action='help', dest='help', help='Shows the help for program.')

reverse_ip  = optparse.OptionGroup(parser, c + "IP Tools" + w)
reverse_ip.add_option( "-1", "--revht",  action='store_true', dest='hackertarget', help="Reverse IP")
reverse_ip.add_option( "-2", "--geo",  action='store_true', dest='geoip', help="Geo IP Lookup")
reverse_ip.add_option( "-3", "--dns",  action='store_true', dest='dnslookup', help="DNS Lookup")
reverse_ip.add_option( "-4", "--sdns",  action='store_true', dest='findshareddns', help="Find Shared DNS")
reverse_ip.add_option( "-5", "--links",  action='store_true', dest='pagelinks', help="Page Links Scrapper")

grouped_scanning = optparse.OptionGroup(parser, c + "Grouped Results" + w)


parser.add_option_group(general)
parser.add_option_group(reverse_ip)
parser.add_option_group(grouped_scanning)

(options, args) = parser.parse_args()
try: website = addHTTP(args[0])
except: pass

try:
    if options.geoip:
        heading(heading="Geo IP Lookup",  color=c, website=website, afterWebHead="")
        geoip(website)

    elif options.hackertarget:
        heading(heading="Reversing IP via HackTarget", color=c, website=website, afterWebHead="")
        reverseViaHT(website)
 

    elif options.pagelinks:
        heading(heading="Extract Links", color=c, website=website, afterWebHead="")
        pagelinks(website)



    elif options.dnslookup:
        heading(heading="DNS Lookup", color=c, website=website, afterWebHead="")
        dnslookup(website)

    elif options.findshareddns:
        heading(heading="Find Shared DNS", color=c, website=website, afterWebHead="")
        findshareddns(website)



    else:
        write(var="~", color=c, data="Usage: " + w + "python " + w + argv[0] + c + " --help")

except KeyboardInterrupt:
    write(var="~", color=r, data="Error: User Interrupted!")

