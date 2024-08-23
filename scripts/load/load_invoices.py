from sqlalchemy import create_engine

def load_invoices(invoices_df):
    engine = create_engine('postgresql://user:password@localhost:5432/odoo_db')
    invoices_df.to_sql('account_invoice', engine, if_exists='replace', index=False)
