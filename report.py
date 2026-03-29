import pandas as pd

def generate_report(analysis, output_path):
    report_df = pd.DataFrame(list(analysis.items()), columns=['Metric', 'Value'])
    report_df.to_csv(output_path, index=False)

    print("\nReport Generated Successfully!\n")