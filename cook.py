import urllib2
import urllib
from cookielib import CookieJar

cj = CookieJar()

opener = urllib2.build_opener(
        urllib2.HTTPCookieProcessor(cj),
        urllib2.HTTPSHandler(debuglevel=1)
        )

formdata = {
    "user" : "turbofish",
    "password" : "gheyv17",
    "remember" : "true",
    "maintain_session " : "true",
    "action" : "Login",
    "rym_ajax_req" : 1,
    "request_token" : ""
}

data_encoded = urllib.urlencode(formdata)

opener.addheaders = [
        ("referer", "https://rateyourmusic.com/account/login"),
        ("user-agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"),
        ("path", "/httprequest"),
        ("scheme", "https"),
        ("accept", "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01"),
        ("accept-encoding", "gzip,deflate,sdch"),
        ("accept-language", "sv-SE,sv;q=0.8,en-US;q=0.6,en;q=0.4"),
        ("cookie", "username=turbofish; is_logged_in=0"),
        ("origin","https://rateyourmusic.com"),
        ("x-requested-with", "XMLHttpRequest")
]

try:
    response = opener.open("https://rateyourmusic.com/httprequest",data_encoded)
    content = response.read()
except urllib2.HTTPError, e:
    print e

