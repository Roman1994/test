from scanner import Scanner
from export import Export



def main() :
    URLlist = ['http://whois.arin.net/rest/poc/HALLA27-ARIN',
               'http://whois.arin.net/rest/poc/TDSI-ARIN',
               'http://whois.arin.net/rest/poc/DAVID240-ARIN',
               'http://whois.arin.net/rest/poc/VDLA2-ARIN',
               'http://whois.arin.net/rest/poc/MOORE227-ARIN',
               'http://whois.arin.net/rest/poc/LINDH6-ARIN']
    for url in URLlist :
      scan = Scanner(url)
      export = Export(scan)
    print('Complite')

main()