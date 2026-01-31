# instantiate an SKLearnModel object that combines your S3-stored model artifacts with the inference logic defined in the provided entry_point.py file

import os
import joblib

def model_fn(model_dir):
    """Load model for inference"""
    # TODO: Load the model file named 'trained_model.joblib'
    model = joblib.load(os.path.join(model_dir, 'trained_model.joblib'))
    return model