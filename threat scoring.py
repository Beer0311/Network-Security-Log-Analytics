import pandas as pd

def calculate_threat_score(row):
    """
    Custom Threat Scoring Heuristic to prioritize network events.
    Weights are assigned based on Severity Level and Packet Length.
    """
    score = 0
    # Severity weighting
    if row['Severity Level'] == 'High': 
        score += 5
    elif row['Severity Level'] == 'Medium': 
        score += 3
        
    # Packet size penalty (Threshold: 1200 bytes)
    if row['Packet Length'] > 1200: 
        score += 5
        
    return score

# Example usage for the pipeline
if __name__ == "__main__":
    # In a real scenario, this would load from your S3 or local CSV
    print("Threat Scoring Script Initialized.")