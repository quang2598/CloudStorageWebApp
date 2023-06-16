#!/bin/bash
sudo apt-get update
sudo apt-get install python3-venv
sudo apt install nginx-core
python3 -m venv venv
source venv/bin/activate
pip install -r requiremnent.txt
pip install gunicorn