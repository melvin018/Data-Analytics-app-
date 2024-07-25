import pandas as pd

def load_data():
    try:
        data = pd.read_csv(r'C:\Users\Owner\Desktop\DataAnalysis\Data-Analytics-app-\Book1.csv')
        print(f"Data loaded successfully from {r'C:\Users\Owner\Desktop\DataAnalysis\Data-Analytics-app-\Book1.csv'}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None