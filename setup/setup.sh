#!/bin/sh
# This script will be run when the environment is initialized.
# Add any setup logic here.

echo "Setting up environment..."

# Execute extra setup steps
bash .setup/setup_steps.sh

# Start server to show plots in preview window
cd .setup
nohup python -m http.server 3000 --bind 0.0.0.0 > /dev/null 2>&1 &

# Create a temporary file to mark that setup has successfully completed
touch /tmp/.setup_finished

# Notify the user
echo "Setup complete!"