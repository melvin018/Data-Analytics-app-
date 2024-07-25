import pandas as pd

def run_analysis():
    # Load data
    data = pd.read_csv(r'C:\Users\Owner\Desktop\DataAnalysis\Data-Analytics-app-\Book1.csv')
    
    # Perform analysis (e.g., calculate mean)
    mean_value = data['value'].mean()

    return {'mean': mean_value}
