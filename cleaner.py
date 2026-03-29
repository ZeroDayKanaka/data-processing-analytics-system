def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    df['Date'] = df['Date'].astype(str)
    df['Price'] = df['Price'].astype(float)
    df['Quantity'] = df['Quantity'].astype(int)

    print("\nData Cleaned Successfully!\n")
    return df