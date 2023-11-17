from flask import Flask, request, render_template, make_response
from weasyprint import HTML
import os

app = Flask(__name__)

def url_function(url):
    try:
        # PDF'ye dönüştürmek istediğiniz URL'yi WeasyPrint ile işleyin
        pdf = HTML(url).write_pdf()
        
        # PDF'yi aynı dizine kaydedin
        pdf_filename = 'weasyprint.pdf'
        with open(pdf_filename, 'wb') as f:
            f.write(pdf)
        
        # Kaydedilen PDF'yi bir HTTP yanıtı olarak gönderin
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'inline; filename={pdf_filename}'
        
        return response
    except Exception as e:
        return f"Error: {e}"

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
