#!/bin/bash

cd frontend
npm install
npm run build

cd ../backend
pip install -r requirements.txt

gunicorn --bind=0.0.0.0 --timeout 600 app:app
