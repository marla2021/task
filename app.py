import json

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    with open('entities.json') as f:
        entities = json.load(f)
        return render_template("main-all-items.html", entities=entities)


@app.route('/paging')
def paging():
    return render_template("main.html")


@app.route('/search')
def search():
    model = request.args.get('model')
    with open('entities.json') as f:
        entities = json.load(f)
        response = []
        if not model:
            response = entities
        else:
            for word in model.split():
                for e in entities:
                    if word in e["model"]:
                        response.append(e)
        return render_template("search_ause.html", entities=response)


@app.route('/card/<int:eid>')
def card(eid: int):

    with open('entities.json') as f:
        entities = json.load(f)
        for en in entities:
            if en["id"] == eid:
                return render_template("card_full.html", entity=ent)

@app.route('/short_card/<int:eid>')
def short_card(eid: int):

    with open('entities.json') as f:
        entities = json.load(f)
        for ent in entities:
            if ent["id"] == eid:
                return render_template("short_card.html", entity=ent)

if __name__ == '__main__':
    app.run(debug=True)
