#!/bin/bash
sudo systemctl daemon-reload
sudo systemctl start dropboxapp.service
sudo systemctl enable dropboxapp.service
sudo systemctl status dropboxapp.service
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx