#!/bin/bash

cd /usercode/FILESYSTEM

# Check if setup is complete
if [ ! -f "/tmp/.setup_finished" ]; then
    echo "The setup is not finished yet. Try again in a few seconds." >&2
    exit 1
fi

# Set matplotlib to use the Agg backend (non-interactive, no GUI windows)
export MPLBACKEND=Agg

# Run the Python script and capture the plot:
# 1. exec(open('main.py').read()) - Execute the original script without modification
# 2. import matplotlib.pyplot as plt - Import pyplot to access the created plots
# 3. plt.savefig('.setup/plot.png') - Save any existing plots to the specified file
python -c "exec(open('main.py').read()); import matplotlib.pyplot as plt; plt.savefig('.setup/plot.png')"