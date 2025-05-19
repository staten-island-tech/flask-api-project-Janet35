import http.client

host = 'jooble.org'
key = '<YOUR_API_KEY>'

connection = http.client.HTTPConnection(host)
#request headers
headers = {"Content-type": "application/json"}
#json query
body = '{ "keywords": "it", "location": "Bern"}'
connection.request('POST','/api/' + key, body, headers)
response = connection.getresponse()
print(response.status, response.reason)
print(response.read())

if __name__ == '__main__':
    app.run(debug=True)