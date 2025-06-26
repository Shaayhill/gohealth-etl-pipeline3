# scripts/validate_data.py

def validate_dataframe(df, df_name, id_column=None):
    print(f"\n📋 Validating {df_name}...")

    # Check for nulls
    null_counts = df.isnull().sum()
    print("🔍 Null values per column:\n", null_counts)

    # Check for duplicates in ID column
    if id_column and id_column in df.columns:
        duplicates = df[df.duplicated(subset=[id_column])]
        print(f"🔁 Duplicates in {id_column}: {len(duplicates)}")
    else:
        print("⚠️ No ID column provided for duplicate check.")

    print("✅ Validation complete.\n")
