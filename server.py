'''
You'll be rewriting your Disappearing Ninja assignment to include AJAX. The below steps will help you get started. Next, follow the wireframe below to build a version of Disappearing Ninja with AJAX. Remember, with AJAX, you will only need one view and your page should never be reloaded.

1. Create a new Flask project. Build it with one get route to serve up your index.html. Test to make sure you can run that server and load the html page before continuing.

2. Create a static directory with your JavaScript file inside of it. Now link your JS file to your index.html file. Test it by asking for an alert box on page load. Don't forget to link to the jQuery CDN, too. You'll be using it for AJAX just like before.

3. You'll need some event listeners in order to trigger a request to the server when a user clicks one of the color buttons.

4. When an event occurs (button click), you'll want to send a request to the server. The server should collect information about which Ninja you'd like to display, along with the correct message, and send a JSON response to the client.
'''

# Import Flask to allow us to create our app, and import
# render_template to allow us to render HTML Files.
from flask import Flask, render_template, request, redirect, jsonify
import json

app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.

@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.

def display_index():
    return render_template('index.html')    # Render the template and return it!

@app.route('/ninja', methods=['POST'])         

def display_ninja_home():

    data = json.loads(request.data)
    ninja_color = data.get('color')

    ninja = 'notapril'
    msg = "There's no ninja in that color!"

    if ninja_color == 'blue':
        ninja = 'Leonardo'
    elif ninja_color == 'orange':
        ninja = 'Michelangelo'
    elif ninja_color == 'red':
        ninja = 'Raphael'
    elif ninja_color == 'purple':
        ninja = 'Donatello'

    if ninja != 'notapril':
        msg = 'You chose '+ninja+'!'

    return jsonify(color=ninja_color, ninja=ninja, message=msg)

app.run(debug=True)                       # Run the app in debug mode.