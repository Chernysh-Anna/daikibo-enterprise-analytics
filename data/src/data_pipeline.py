import json
import zipfile
import pandas as pd

def process_telemetry(zip_path='data/raw/daikibo-telemetry-data.json'):
    """Unpack nested JSON telemetry data and compute downtime minutes."""
    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open(z.namelist()[0]) as f:
            raw_data = json.load(f)
    df = pd.json_normalize(raw_data)
    df['downtime_minutes'] = df['data.status'].apply(lambda x: 10 if x == 'unhealthy' else 0)
    df.to_csv('data/processed/telemetry_clean.csv', index=False)
    print(f"Processed {len(df):,} telemetry records successfully.")
    return df

def process_equality(input_path='data/raw/Task 5 Equality Table.xlsx'):
    """Apply forensic classification to compensation records."""
    df = pd.read_excel(input_path)
    
    def classify(score):
        if abs(score) <= 10:
            return "Fair"
        elif abs(score) <= 20:
            return "Unfair"
        return "Highly Discriminative"
    
    df['Equality class'] = df['Equality Score'].apply(classify)
    df.to_excel('data/processed/equality_classified.xlsx', index=False)
    print(f"Audited {len(df)} organizational roles.")
    return df

if __name__ == '__main__':
    process_telemetry()
    process_equality()