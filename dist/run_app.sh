#!/bin/bash
./manage &  # This starts the Django server in the background
sleep 3     # Wait for 3 seconds to make sure the server starts
open http://127.0.0.1:8000/  # This opens the web browser

