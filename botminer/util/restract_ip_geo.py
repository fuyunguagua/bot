import re
import os
import requests

#file
def identify_ip_geolocaltion_from_file(file):
    with open(file, 'rb') as f:
        ips = [line.strip(os.linesep) for line in f]
    return identify_ip_geolocaltion(ips)
#
def identify_ip_geolocaltion(ips):
    ips_info = []
    ips_missed = []
    for ip in ips:
        try:
            response = query_from_internet(ip)
        except Exception:
            ips_missed.append(ip)
            continue
        result = restract_ip_geolocation(response)
        ips_info.append(result[0])
    return ips_info,ips_missed


def query_from_internet(ip):
    data = {}
    data['query'] = ip
    data['submit'] = 'IP+Lookup'
    headers = {'authority':'www.iplocation.net',
                'method':'POST',
                'path':'/',
                'scheme':'https',
                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding':'gzip, deflate, br',
                'accept-language':'zh-CN,zh;q=0.8,en;q=0.6',
                'cache-control':'max-age=0',
                'content-length':'30',
                'content-type':'application/x-www-form-urlencoded',
                'cookie':'visid_incap_877543=QI58HI4ASNyLlM4h1MmysTJDtVkAAAAAQUIPAAAAAAAtXdc6I1NdLSMxuLeAz1VV; incap_ses_636_877543=W7TOeASP1hFvF/7c8obTCDNDtVkAAAAAQYb5Mahhiq1ohhGyZhKcFg==; freewheel-detected-bandwidth=0; GED_PLAYLIST_ACTIVITY=W3sidSI6IlBFL1QiLCJ0c2wiOjE1MDUwNTIxNTgsIm52IjowLCJ1cHQiOjE1MDUwNTIxNTIsImx0IjoxNTA1MDUyMTUyfV0.; _gat=1; incap_ses_549_877543=PZjFV23komHufuxsHnGeBzZJtVkAAAAA/uUosdJeF6AwuH4LJes2fw==; _ga=GA1.2.967065210.1505051451; _gid=GA1.2.659834846.1505051458; OX_plg=pm',
                'origin':'https://www.iplocation.net',
                'referer':'https://www.iplocation.net/',
                'upgrade-insecure-requests':'1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}


    response = requests.post('https://www.iplocation.net/', data=data, headers=headers, timeout= 10)
    return response

def restract_ip_geolocation(response):
    re_pre = '<td>(\d*\.\d*\.\d*\.\d*)</td><td>(.*?)<img.*?<td>(.*?)</td><td>(.*?)</td></tr>'
    result = re.findall(re_pre, response.text, re.S)
    return result
