#!/usr/bin/env python3
"""
Download and save the California Housing dataset as CSV.
This script downloads the original dataset from StatLib and applies
sklearn's transformations to produce a CSV identical to
fetch_california_housing(as_frame=True).frame
"""
import os
import tempfile
import zipfile
from pathlib import Path
from urllib.request import urlretrieve

import numpy as np
import pandas as pd


def download_california_housing_csv(output_dir="data"):
    """
    Download California Housing dataset from StatLib and save as CSV.
    
    Parameters
    ----------
    output_dir : str, default="data"
        Directory where the CSV file will be saved.
    """
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Download from StatLib
        zip_path = tmpdir / "houses.zip"
        urlretrieve("https://lib.stat.cmu.edu/datasets/houses.zip", zip_path)
        
        # Extract the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdir)
        
        # Read and parse the data file
        data_file = tmpdir / "cadata.txt"
        with open(data_file, 'r', encoding='latin-1') as f:
            lines = f.readlines()
            # Extract the last 20640 lines (actual data)
            data_lines = lines[-20640:]
        
        # Parse the data
        data = []
        for line in data_lines:
            values = [float(x) for x in line.strip().split()]
            data.append(values)
        
        data_array = np.array(data)
        
        # StatLib column order: median_house_value, median_income, housing_median_age,
        #                       total_rooms, total_bedrooms, population, households,
        #                       latitude, longitude
        median_house_value = data_array[:, 0]
        median_income = data_array[:, 1]
        housing_median_age = data_array[:, 2]
        total_rooms = data_array[:, 3]
        total_bedrooms = data_array[:, 4]
        population = data_array[:, 5]
        households = data_array[:, 6]
        latitude = data_array[:, 7]
        longitude = data_array[:, 8]
        
        # Apply sklearn's transformations
        ave_rooms = total_rooms / households
        ave_bedrms = total_bedrooms / households
        ave_occup = population / households
        target = median_house_value / 100000.0
        
        # Create DataFrame with sklearn's column names and order
        df = pd.DataFrame({
            'MedInc': median_income,
            'HouseAge': housing_median_age,
            'AveRooms': ave_rooms,
            'AveBedrms': ave_bedrms,
            'Population': population,
            'AveOccup': ave_occup,
            'Latitude': latitude,
            'Longitude': longitude,
            'MedHouseVal': target
        })
        
        # Save to CSV
        csv_path = output_path / "california_housing.csv"
        df.to_csv(csv_path, index=False)


if __name__ == "__main__":
    download_california_housing_csv()

