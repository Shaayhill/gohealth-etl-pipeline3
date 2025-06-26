# scripts/main.py

import os
from scripts.ingest_data import load_excel_data
from scripts.validate_data import validate_dataframe
from scripts.transform_data import transform_and_generate_outputs

# File paths
data_dir = "data/"
files = {
    "patients": "patients.csv",
    "visits": "visits.csv",
    "lab_results": "lab_results.csv",
    "icd_reference": "icd_reference.csv"
}

def main():
    print("🚀 Starting GoHealth ETL Pipeline...")

    # Load data
    patients_df = load_excel_data(os.path.join(data_dir, files["patients"]))
    visits_df = load_excel_data(os.path.join(data_dir, files["visits"]))
    labs_df = load_excel_data(os.path.join(data_dir, files["lab_results"]))
    icd_df = load_excel_data(os.path.join(data_dir, files["icd_reference"]))

    # Validate data
    validate_dataframe(patients_df, "patients", id_column="patient_id")
    validate_dataframe(visits_df, "visits", id_column="visit_id")
    validate_dataframe(labs_df, "lab_results", id_column="result_id")
    validate_dataframe(icd_df, "icd_reference", id_column="icd_code")

    # Transform and output
    transform_and_generate_outputs(patients_df, visits_df, labs_df, icd_df)

    print("🏁 ETL Pipeline complete!")

if __name__ == "__main__":
    main()
