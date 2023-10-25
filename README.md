# URL Shortener with Flask

This is a simple URL shortener web application built with Flask, a Python web framework. It allows users to enter long URLs and get corresponding shortened URLs. The shortened URLs can then be used to redirect to the original long URLs.

## Getting Started

These instructions will help you set up and run the URL shortener on your local machine for development and testing purposes.

### Prerequisites

- Python 3
- Flask (install it using `pip install flask`)

### Installation

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/Freddy155/url-shortener.git &&
   cd url-shortener-flask
   ```

2. Start the application
   ```shell
    python app.py
    ```

### Usage

1. **Access the URL Shortener**:
   - Open your web browser and visit [http://localhost:5000](http://localhost:5000).

2. **Enter a Long URL**:
   - On the homepage, you'll find an input field.
   - Enter the long URL that you want to shorten.

3. **Generate a Shortened URL**:
   - Click the "Shorten" button.
   - The application will generate a shortened URL for the provided long URL.

4. **Redirect to Original URL**:
   - To access the original long URL, click on the generated shortened URL.
   - You will be redirected to the original webpage.

### How It Works

- The URL shortener uses a Python dictionary as an in-memory key-value store to maintain the associations between long URLs and their corresponding shortened versions.

- Shortened URLs are generated using a simplified SHA-1 hashing algorithm.

### Directory Structure

- **app.py**: This file contains the main Flask application.

- **templates/index.html**: This HTML template is used for the homepage of the URL shortener.

### Acknowledgments

This URL shortener project was created as a part of a python parcticing series **28 days of .py** using Flask. Feel free to customize and enhance it according to your needs. Enjoy using your Flask-based URL shortener! 🚀

