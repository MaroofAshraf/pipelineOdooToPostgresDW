from sqlalchemy import create_engine

def load_customers(customers_df):
    engine = create_engine('postgresql://user:password@localhost:5432/odoo_db')
    customers_df.to_sql('res_partner', engine, if_exists='replace', index=False)
