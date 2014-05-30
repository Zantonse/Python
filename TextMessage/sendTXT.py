import urllib
import urllib2
number = 9014831164
message = "Your Turn"
carrier = 'AT&T'
prov = ''
url2 = 'http://www.txt2day.com/lookup.php'
url = 'http://www.onlinetextmessage.com/send.php'
if 'Verizon' in carrier:
    prov = '203'
if 'AT&T' in carrier:
    prov = '41'
print prov
if prov == 0:
    print "Failed To Identify Provider\n"
    exit
values = {'number' : number,
          'from' : 'craigv@ami.com',
          'remember' : 'n',
          'subject' : 'Welcome',
          'carrier' : prov,
          'quicktext' : '',
          'message' : message,
          's' : 'Send Message'}
data = urllib.urlencode(values)  ##text sender
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read() 
print "sent"