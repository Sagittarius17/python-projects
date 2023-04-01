from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['url']
    # shortener = CustomShortener(prefix='me')
    # short_url = shortener.shorten(url)
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    return render_template('index.html', short_url=short_url)

# class CustomShortener(pyshorteners.Shortener):
#     def __init__(self, prefix=None, **kwargs):
#         self.prefix = prefix
#         super().__init__(**kwargs)

#     def shorten(self, url):
#         short_url = super().shorten(url)
#         if self.prefix:
#             short_url = self.prefix + short_url
#         return short_url

if __name__ == '__main__':
    app.run(debug=True)

