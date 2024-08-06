# Ref: https://www.whitelist1.com/2018/04/calculating-http-digest-authentication.html

import hashlib

# from wireshark

# in 401 from server
# Digest realm="validusers@robapi.abb", domain="/", qop="auth", nonce="MGY0Yjc2MGY2Y2QyZjAwNzp2YWxpZHVzZXJzQHJvYmFwaS5hYmI6MTkwMjg5NjRlNGE6MA==", opaque="799d5", algorithm="MD5", stale="FALSE"

# in second GET from client
# Digest username="Default User", realm="validusers@robapi.abb", nonce="MGY0Yjc2MGY2Y2QyZjAwNzp2YWxpZHVzZXJzQHJvYmFwaS5hYmI6MTkwMjg5NjRlNGE6MA==", uri="/rw/rapid/execution", algorithm="MD5", qop=auth, nc=00000001, cnonce="diddLOPR", response="c36e30cdd2961584cd41f6f49f6bcbba", opaque="799d5"

un = 'Default User'
pw = 'robotics'
realm = "validusers@robapi.abb"

h1=hashlib.md5((':'.join([un, realm, pw])).encode('utf-8')).hexdigest()
print("h1: ", h1)

method = 'GET'
uri = '/rw/rapid/execution'

h2=hashlib.md5((':'.join([method, uri])).encode('utf-8')).hexdigest()
print("h2: ", h2)

qop = 'auth'
nonce = 'MGY0Yjc2MGY2Y2QyZjAwNzp2YWxpZHVzZXJzQHJvYmFwaS5hYmI6MTkwMjg5NjRlNGE6MA=='
cnonce = 'diddLOPR'
nc = '00000001'


response=hashlib.md5((':'.join([h1, nonce, nc, cnonce, qop, h2])).encode('utf-8')).hexdigest()

print("resp: ", response)
# Correct response: c36e30cdd2961584cd41f6f49f6bcbba
