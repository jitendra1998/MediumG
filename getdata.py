

import requests

url = 'https://medium.freecodecamp.org/what-is-a-quantum-computer-explained-with-a-simple-example-b8f602035365'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})

f = open( 'output.txt', 'w+' )
f.write((response.text).encode('utf-8'))
f.close()
