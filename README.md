# 🏥 GoHealth EMR Data Engineering Pipeline

Built by **Shaayla Hill**, this project is an end-to-end data engineering solution for ingesting, validating, transforming, and outputting real-world Electronic Medical Records (EMR) data for GoHealth Urgent Care.

---

## Project Overview

This pipeline simulates a healthcare analytics environment using raw data files provided in `.csv` format. The goal is to prepare the data for downstream use in reporting, insights, and predictive models.

### Source Data

The following datasets are ingested and processed:
- `patients.csv`: Master list of patients
- `visits.csv`: Patient visits linked to providers
- `lab_results.csv`: Lab results tied to each visit
- `icd_reference.csv`: Diagnosis codes and descriptions

---

## Key Features

✅ Built using **Python** and **pandas**  
✅ Modular ETL scripts (`ingest`, `validate`, `transform`)  
✅ Null check, duplicate check, and join validation  
✅ Clean final output in `outputs/final_dataset.csv`  
✅ Clean folder structure, schema docs, and best practices

---

##  Folder Structure

gohealth-etl-pipeline/
│
├── data/ # Raw .csv files (excluded from GitHub)
├── outputs/ # Cleaned, merged final dataset
├── scripts/ # Python scripts for each ETL phase
│ ├── ingest_data.py
│ ├── validate_data.py
│ ├── transform_data.py
│ └── main.py
├── docs/ # Schema and design documentation
│ ├── design_decisions.md
│ ├── schema_layout.txt
│ └── schema.png
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md

yaml
Copy
Edit

---

##  How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Shaayhill/gohealth-etl-pipeline3.git
cd gohealth-etl-pipeline3
2. Create and activate a virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add the .csv files to the data/ folder
Required files:

patients.csv

visits.csv

lab_results.csv

icd_reference.csv

5. Run the pipeline
bash
Copy
Edit
python scripts/main.py
The final dataset will be saved in:

bash
Copy
Edit
outputs/final_dataset.csv
 Schema Diagram

Or view it as text: docs/schema_layout.txt

 Design Overview
Documentation of technical decisions is available in:
docs/design_decisions.md

Highlights include:

Data validation logic

Why certain joins were used

HIPAA considerations (simulated data only)

Suggested enhancements (e.g., Slowly Changing Dimensions, CI/CD)

🧰 Tools Used
Python 3

pandas

openpyxl

Git & GitHub

VS Code

 Potential Extensions
Add database storage (e.g., PostgreSQL, Snowflake)

Load into a data warehouse (ETL → ELT)

Visualize insights with Tableau or Power BI

Build CI pipeline with GitHub Actions

Add Great Expectations for robust validation

 Live Demo (GitHub Pages)
Visit the interactive project showcase:
🔗 https://shaayhill.github.io/gohealth-etl-pipeline3
