from flask import Flask, redirect, url_for, render_template
from urllib2 import Request, urlopen

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
