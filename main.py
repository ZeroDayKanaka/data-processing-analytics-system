from utils.loader import load_data
from utils.cleaner import clean_data
from utils.processor import process_data
from utils.analyzer import analyze_data
from utils.report import generate_report

def main():
    file_path = "data/sales.csv"
    output_path = "reports/report.csv"

    df = load_data(file_path)
    df = clean_data(df)
    df = process_data(df)
    
    analysis = analyze_data(df)
    generate_report(analysis, output_path)

if __name__ == "__main__":
    main()
    