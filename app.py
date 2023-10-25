from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

# Initialize the URL shortener dictionary
url_dict = {}

import hashlib

def shorten_url(url):
    sha1_hash = hashlib.sha1(url.encode()).hexdigest()
    # Take the first 8 characters of the hash as the short URL
    short_url = sha1_hash[:8]
    return short_url

def add_url(long_url):
    short_url = shorten_url(long_url)
    url_dict[short_url] = long_url
    return f'http://localhost:5000/{short_url}'  # Adjust the URL format

def get_original_url(short_url):
    return url_dict.get(short_url, None)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_url = add_url(long_url)
    return f'Shortened URL: {short_url}'  

@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = get_original_url(short_url)
    if original_url:
        # Modify the redirection to use localhost and port 5000
        return redirect(url_for('original', short_url=short_url))
    else:
        return "Short URL not found."

@app.route('/original/<short_url>')
def original(short_url):
    original_url = get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return "Original URL not found."

if __name__ == '__main__':
    app.run(debug=True)
