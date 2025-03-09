import pickle
import pandas as pd
from src.utils import load_pkl_object, load_json

# Load global path
PATH_MODEL_BINNING = "./artifact/model/binning/model.pkl"
PATH_MODEL_CLASSIFIER = "./artifact/model/classifier/logistic_regression/model.pkl"
PATH_METADATA_CLASSIFIER = "artifact/model/classifier/logistic_regression/model_metadata.json"

MODEL_BINNING = load_pkl_object(PATH_MODEL_BINNING)
MODEL_CLASSIFIER = load_pkl_object(PATH_MODEL_CLASSIFIER)
METADATA_CLASSIFIER = load_json(PATH_METADATA_CLASSIFIER)
CUT_OFF_THRESHOLD = METADATA_CLASSIFIER["cut_off_threshold"]

MODEL_FEATURE = list(MODEL_BINNING.variable_names)

def inference(X_test:pd.DataFrame):
    global MODEL_BINNING, MODEL_CLASSIFIER, CUT_OFF_THRESHOLD

    X_test_binned = MODEL_BINNING.transform(X_test)
    y_prob = MODEL_CLASSIFIER.predict_proba(X_test_binned)[:,1]
    y_pred = (y_prob >= CUT_OFF_THRESHOLD).astype(int)
    return y_pred