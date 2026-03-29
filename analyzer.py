def analyze_data(df):
    total_revenue = df['Total_Sales'].sum()
    avg_order = df['Total_Sales'].mean()

    top_product = df.groupby('Product_Name')['Total_Sales'].sum().idxmax()
    top_category = df.groupby('Category')['Total_Sales'].sum().idxmax()

    print("\n--- ANALYSIS ---")
    print("Total Revenue:", total_revenue)
    print("Average Order Value:", avg_order)
    print("Top Product:", top_product)
    print("Top Category:", top_category)

    return {
        "Total Revenue": total_revenue,
        "Average Order Value": avg_order,
        "Top Product": top_product,
        "Top Category": top_category
    }