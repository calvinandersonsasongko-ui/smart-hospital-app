import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(page_title="Smart Hospital Patient Navigator", page_icon="🏥",
layout="wide")

@st.cache_resource
def load_model():
  with open('hospital_model.pk1', 'rb') as f:
   return pickle.load(f)

bundle = load_model():
model = bundle['model']
scaler = bundle['scaler']
features = bundle['features']
cols_to_scales = bundle['features']
dept_map_inv = bundle['dept_map_inv']
temp_map = bundle['temp_map']
hr_map = bundle['hr_map']
dur_map = bundle['dur_map']
cc_map = bundle['cc_map']
