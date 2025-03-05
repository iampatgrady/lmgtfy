from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        encoded_question = urllib.parse.quote(question)
        gemini_url = "https://gemini.google.com/prompt?utm_source=chrome_omnibox&utm_medium=owned&utm_campaign=gemini_shortcut"
        headers = {
            "X-Omnibox-Gemini": encoded_question
        }
        # We're not actually *sending* the request with headers. We just construct the URL
        # with the X-Omnibox-Gemini value *as if* it was a header.  This is how we achieve
        # the redirect with the "header" as a URL parameter.
        redirect_url = f"{gemini_url}&X-Omnibox-Gemini={encoded_question}"
        return redirect(redirect_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))