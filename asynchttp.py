#!/usr/bin/env python
# -*- Mode: Python; tab-width: 4 -*-

import asyncore
import socket
import string

class http_client(asyncore.dispatcher):

    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.path = path
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, 80))
        self.buffer = "GET %s HTTP/1.1\nHost: %s\r\n\r\n" % (self.path, host)

    def handle_connect(self):
        pass

    def handle_read(self):
        data = self.recv(8192)
        print data

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

if __name__ == '__main__':
    import sys
    import urlparse

    for url in sys.argv[1:]:
        parts = urlparse.urlparse(url)
        if parts[0] != 'http':
            raise ValueError, "HTTP URL's only, please"
        else:
            host = parts[1]
            path = parts[2]
            print "host = %s" % host
            print "path = %s" % path
            http_client(host, path)

    asyncore.loop()
