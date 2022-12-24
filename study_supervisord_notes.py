supervisord.py
	self.options.openhttpservers(self)

options.py
	def openhttpservers(self, supervisord):
		self.httpservers = self.make_http_servers(supervisord)

    def make_http_servers(self, supervisord):
        from supervisor.http import make_http_servers
        return make_http_servers(self, supervisord)

http.py
	def make_http_servers(options, supervisord):
		hs = supervisor_af_inet_http_server(host, port,
                                                logger_object=wrapper)

	class supervisor_af_inet_http_server(supervisor_http_server):
		def __init__(self, ip, port, logger_object):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	self.prebind(sock, logger_object)
        	self.bind((ip, port))

	class supervisor_http_server(http_server.http_server):
		def prebind(self, sock, logger_object):
			asyncore.dispatcher.__init__ (self)
        	self.set_socket(sock)

        def postbind(self):
        	self.listen(1024)

medusa.http_server.py
	class http_server (asyncore.dispatcher):

medusa.asyncore_25.py
	class dispatcher:
	    def __init__(self, sock=None, map=None):
	        if map is None:
	            self._map = socket_map
	        else:
	            self._map = map

	        if sock:
	            self.set_socket(sock, map)
	            self.socket.setblocking(0)
	            self.connected = True
		
		def set_socket(self, sock, map=None):
	        self.socket = sock
	        self._fileno = sock.fileno()
	        self.add_channel(map)

	    def add_channel(self, map=None):
	        if map is None:
	            map = self._map
	        map[self._fileno] = self # Initially, self = supervisor_af_inet_http_server

# *****************************************************
# * Notes about XML-RPC                               *
# *****************************************************

1. For server side
Server install a xmlrpc handler object

2. Request and response flow
- Client uses xmlrpc lib to create a ServerProxy object, this object has a underlying HTTP transport object
- Client call a method on server via the proxy object
- Proxy object will marshal the method name and arguments to XML data
- Proxy object passes the XML data to HTTP transport object
- HTTP transport object will make a POST request to the server
- The server will accept the TCP connection and hand control over to a deferring http channel object to handle this connection.
- The deferring http channel object will parse the POST request from the client. It make a http request object from HTTP POST request header.
- The deferring http channel object passes control and the http request object to the corresponding method of xmlrpc handler.
- The xmlrpc handler will collect incomming xml data from the POST request and unmarshal the xml data to Python object.
- Based on xml data, the xmlrpc handler will call the corresponding method from rpcinterface plugin object.
- The xmlrpc handler will marshal the result to xml data and pass this data to the deferring http channel object to respond to client. 
