from website import create_app
from flask import request

app = create_app()

@app.route('/')
def index():
    username = request.cookies.get('username')

if __name__ == '__main__': 
    app.run(debug=True)