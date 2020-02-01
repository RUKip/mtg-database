#!/bin/bash
sudo docker-compose run backend django-admin startproject mtg_database .
sudo chown -R $USER:$USER .
