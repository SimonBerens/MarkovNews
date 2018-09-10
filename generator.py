import os

from web_scrape import get_text
from markov_chain import MarkovChain
from constants import *
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def news():
    if not os.path.exists(HEADLINE_JSON):
        f = open(HEADLINE_JSON, "w")
        headline_matrix = MarkovChain()
        [headline_matrix.append_to_matrix(text) for k, source in HEADLINE_SOURCES.items() for text in get_text(source)]
        f.write(headline_matrix.to_json())
    else:
        f = open(HEADLINE_JSON, "r")
        headline_matrix = MarkovChain(json_str=f.read())
    f.close()

    if not os.path.exists(SUMMARY_JSON):
        f = open(SUMMARY_JSON, "w")
        summary_matrix = MarkovChain()
        [summary_matrix.append_to_matrix(text) for k, source in SUMMARY_SOURCES.items() for text in get_text(source)]
        f.write(summary_matrix.to_json())
    else:
        f = open(SUMMARY_JSON, "r")
        summary_matrix = MarkovChain(json_str=f.read())
    f.close()

    return render_template("index.html", headline=headline_matrix.generate_chain(),
                           summary=summary_matrix.generate_chain())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/static/<path:path>')
def styles(path):
    return send_from_directory('js', path)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
