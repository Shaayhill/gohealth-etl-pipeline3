# scripts/ingest_data.py

import pandas as pd
import os

def load_excel_data(file_path):
    try:
        df = pd.read_excel(file_path)
        print(f"✅ Successfully loaded {os.path.basename(file_path)}")
        return df
    except Exception as e:
        print(f"❌ Error loading {file_path}: {e}")
        return None
