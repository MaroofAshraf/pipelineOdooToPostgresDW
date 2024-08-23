import pandas as pd
from odoorpc import ODOO

def extract_customers():
    odoo = ODOO('your_odoo_host', port=8069)
    odoo.login('your_db', 'user', 'password')
    customers = odoo.env['res.partner'].search_read([], ['name', 'email', 'phone'])
    customers_df = pd.DataFrame(customers)
    return customers_df
