sites = [ 'http://www.google.com', 'http://www.facebook.com', 'http://www.twitter.com' ]
for index in range(len(sites)):
	from urllib2 import Request, urlopen, URLError, HTTPError
	req = Request(sites[index])
	try:
		response = urlopen(req)
	except HTTPError as e:
		print 'The server couldn\'t fulfill the request.'
		print 'Error code: ', e.code
	except URLError as e:
		print 'We failed to reach a server.'
		print 'Reason: ', e.reason
	else:
		print 'Everything is fine at ', sites[index]

print '-- Process Complete -- '