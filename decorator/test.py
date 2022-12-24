from fakeflask import FakeFlask

app = FakeFlask('Test Decorator App')

@app.route('/', methods=['GET', 'POST'])
def index():
	return 'Welcome to Home Page'

@app.route('/users', methods=['POST'])
def create():
	return 'An user was created'

app.run()