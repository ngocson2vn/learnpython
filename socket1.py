import socket

def log(message):
    print "[INFO] %s" % message

hostname = socket.gethostname()
log("hostname: %s" % hostname)
try:
    ip = socket.gethostbyname(hostname)
    log("ip: %s" % ip)
except socket.error:
    raise ValueError(
        'Could not determine IP address for hostname %s, '
        'please try setting an explicit IP address in the "port" '
        'setting of your [inet_http_server] section.  For example, '
        'instead of "port = 9001", try "port = 127.0.0.1:9001."'
        % hostname)
try:
    server_name = socket.gethostbyaddr(ip)
    log(str(server_name))
except socket.error:
    log('Cannot do reverse lookup')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
status = [sock.__class__.__module__+"."+sock.__class__.__name__]
print ' '.join(status)
print "%s" % sock.__repr__()
print ""
print dir(sock)
