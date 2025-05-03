from flask import Flask, send_file, request, render_template
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the text from the form
        data = request.form.get('data')
        
        # Create QR code
        img = qrcode.make(data)
        
        # Save it to a bytes buffer
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        buffer.seek(0)
        
        return send_file(buffer, mimetype='image/png')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
