#!/bin/bash

pip install -r requirements.txt

export FLASK_APP=webapp.py
export FLASK_DEBUG=1

flask run -h 0.0.0.0