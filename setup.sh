#!/usr/bin/env bash

# Update package list and install dependencies
apt-get update
apt-get install -y software-properties-common
add-apt-repository -y ppa:gnome3-team/gnome3
apt-get update
apt-get install -y \
  libpango-1.0-0 \
  libpango1.0-dev \
  libcairo2 \
  libcairo2-dev \
  libgdk-pixbuf2.0-0 \
  libgdk-pixbuf2.0-dev \
  libffi-dev \
  libxml2-dev \
  libxslt1-dev \
  libjpeg-dev \
  zlib1g-dev \
  libpangoft2-1.0-0 \
  libpangocairo-1.0-0

# Ensure Pango is up-to-date
apt-get install --only-upgrade libpango-1.0-0

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt
