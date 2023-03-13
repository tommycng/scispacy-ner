#!/usr/bin/python3
import json
import scispacy
import spacy


#initalise module
nlp = spacy.load("en_ner_bc5cdr_md")

def Entity_Lookup(text):
    doc = nlp(text)

    my_list = list()
    for ent in doc.ents:
        row = {
        "entity": ent.text,
        "start": ent.start_char,
        "end": ent.end_char,
        "label": ent.label_
        }
        my_list.append(row)

    out = {
        "text": text,
        "entries": my_list
    }

    j = json.dumps(out)
    return(j)


#API server
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def health_check():
    return('OK')

@app.route('/parse', methods=['GET', 'POST'])
def parse_message():
    content = request.json
    #print(content['mytext'])
    data = Entity_Lookup(content['text'])
    return(data)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=8445,debug=False)
