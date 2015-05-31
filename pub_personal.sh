#!/bin/bash

pelican -s conf_personal.py
ghp-import output/personaljournal
git push git@github.com:brycecaine/brycecaine.github.io.git gh-pages:master