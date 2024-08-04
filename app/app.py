from flask import Flask
import socket

app = Flask(__name__)

# Define the port number
port = 5000

# HTML template for the response with CSS
def generate_response(title, message):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                color: #333;
            }}
            .container {{
                width: 80%;
                margin: 20px auto;
                padding: 20px;
                background: #fff;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #007BFF;
            }}
            p {{
                font-size: 18px;
                line-height: 1.6;
            }}
            .bold {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{title}</h1>
            <p>{message}</p>
        </div>
    </body>
    </html>
    """

@app.route('/')
def home():
    hostname = socket.gethostname()
    return generate_response(
        'Home Page',
        f'Hello! Showing Home Page <span class="bold">{hostname}</span>!'
    )

@app.route('/frontend')
def frontend():
    hostname = socket.gethostname()
    return generate_response(
        'Frontend Page',
        f'Frontend Response from Port <span class="bold">{port}</span> from <span class="bold">{hostname}</span>!'
    )

@app.route('/backend')
def backend():
    hostname = socket.gethostname()
    return generate_response(
        'Backend Page',
        f'Backend Response from Port <span class="bold">{port}</span> from <span class="bold">{hostname}</span>!'
    )

@app.route('/admin')
def admin():
    return generate_response(
        'Admin Page',
        'Hello, this is the admin page!'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
