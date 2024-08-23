def transform_invoices(invoices_df):
    # Example transformation: Convert dates to datetime
    invoices_df['date_invoice'] = pd.to_datetime(invoices_df['date_invoice'])
    return invoices_df
