from flask import Flask, request, render_template
import webbrowser
import pdfkit
import os

app = Flask(__name__)

def url_function(url):
    webbrowser.get('firefox').open_new(url)
    try:
        pdfkit.from_url(url, 'url.pdf')
    except Exception as e:
        print(e)
    return url

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        url = request.form['url']

        result = url_function(url)
        
    return render_template('index.html', result=result)
        
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)