from nurse_app import app

@app.route('/')
@app.route("/login")
def index():
	return "Please Login"
	
	