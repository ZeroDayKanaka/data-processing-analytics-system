def process_data(df):
    df['Total_Sales'] = df['Price'] * df['Quantity']
    return df