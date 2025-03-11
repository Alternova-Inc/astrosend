#!/bin/bash

# Activate the conda environment
source $(conda info --base)/etc/profile.d/conda.sh
conda activate astrosend

# Run the development server
python manage.py runserver 