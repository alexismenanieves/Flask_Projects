# We'll use Flask
from flask import Flask

# To create an app instance that points to our file using the name
app = Flask(__name__)

# The we use a decorator to indicate in what route we serve
@app.route('/')
def hello_flask():
  return 'Hello Flask!!'

# Then we run the app. We'll get a warning that this is dev server
if __name__ == '__main__':
  app.run()
