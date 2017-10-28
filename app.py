from functools import lru_cache
from fnmatch import fnmatch
import json
import random
import os

from flask import Flask, jsonify, render_template

app = Flask(__name__)

one_liners = [
    'Instagram is just Twitter for people who go outside.',
    'Why do dogs always race to the door when the doorbell rings? It’s hardly ever for them.',
    '“Just because you can’t dance doesn’t mean you shouldn’t dance.”   - Alcohol',
    'What are they planting to grow the seedless watermelon?',
    'Sometimes I think war is God’s way of teaching us geography.',
    'Humankind has a perfect record in aviation; we never left one up there.',
    'If truth is beauty, how come no one has their hair done in a library?',
    'Karate: the ancient Japanese art of getting people to buy lots of belts.',
    'Haircuts are great because I did none of the work but get all the credit.',
    '“Dad?” —Zebra looking at a piano',
]


@app.route('/api')
def api():
    return jsonify({'one_liner': random.choice(one_liners)})


@lru_cache()
def assets():
    out = {}
    for filename in os.listdir('static/assets'):
        if fnmatch(filename, 'app.*.css'):
            out['css'] = filename
        if fnmatch(filename, 'app.*.js'):
            out['app_js'] = filename
        if fnmatch(filename, 'manifest.*.js'):
            out['manifest_js'] = filename
        if fnmatch(filename, 'vendor.*.js'):
            out['vendor_js'] = filename
    print('assets run', out)
    return out


@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    if app.debug:
        return render_template('index.html')
    else:
        return render_template('index.html', production_assets=assets())
