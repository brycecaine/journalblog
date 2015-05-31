#!/bin/bash

pelican -s conf_ancestor.py
ghp-import output/ancestorjournals
git push git@github.com:ancestorjournals/ancestorjournals.github.io.git gh-pages:master