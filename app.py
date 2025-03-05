from flask import Flask, render_template, request
import requests
import urllib.parse
import os
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        encoded_question = urllib.parse.quote(question)
        gemini_url = "https://gemini.google.com/prompt?utm_source=lmgtfy&utm_medium=notowned&utm_campaign=lmfao"
        headers = {
            "X-Omnibox-Gemini": encoded_question
        }
        try:
            response = requests.get(gemini_url, headers=headers)
            response.raise_for_status()

            # Parse the HTML response with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the input field (you'll need to inspect the Gemini HTML to get the correct selector)
            # This is just an EXAMPLE; you need the ACTUAL selector.  Inspect the Gemini page!
            input_field = soup.find('textarea')  # Or 'input', or whatever the correct tag is.
            #  Could also be: input_field = soup.find('input', {'name': 'q'}) or similar

            if input_field:
                # Set the value of the input field
                input_field.string = question # Use the *unencoded* question here.
            else:
                 print("Input field not found in Gemini HTML!") #Debug to check

            # Return the *modified* HTML
            return str(soup), response.status_code, response.headers.items()

        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}", 500

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))