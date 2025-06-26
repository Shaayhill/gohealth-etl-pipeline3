# scripts/transform_data.py

def transform_and_generate_outputs(patients_df, visits_df, labs_df, icd_df):
    print("🔄 Starting transformations...")

    # Merge visits with patients
    merged_df = visits_df.merge(patients_df, on='patient_id', how='left')

    # Merge labs with visits
    merged_df = merged_df.merge(labs_df, on='visit_id', how='left')

    # Merge ICD reference with visits
    merged_df = merged_df.merge(icd_df, on='icd_code', how='left')

    print(f"✅ Merged data shape: {merged_df.shape}")

    # Export the final dataset
    output_path = "outputs/final_dataset.csv"
    merged_df.to_csv(output_path, index=False)
    print(f"📦 Output saved to {output_path}")
