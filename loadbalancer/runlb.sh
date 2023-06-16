#!/bin/bash
sudo systemctl daemon-reload
sudo systemctl start lb.service
sudo systemctl enable lb.service
sudo systemctl status lb.service
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx