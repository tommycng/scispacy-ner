#!/bin/bash

/usr/bin/docker run -d --restart unless-stopped -p 8445:8445 -t scispacy
