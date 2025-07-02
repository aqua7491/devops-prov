#!/bin/bash

chmod +x app.py

tar -cvpf app1-01.tar.gz app.py

mv app1-01.tar.gz rpmbuild/SOURCES/app1-01.tar.gz
