def transform_customers(customers_df):
    # Example transformation: Normalize phone numbers
    customers_df['phone'] = customers_df['phone'].str.replace(r'\D', '')
    return customers_df
