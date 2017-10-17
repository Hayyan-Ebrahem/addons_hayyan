
from odoo import api, fields, models


class CustomerSaleWizard(models.TransientModel):

    _name = 'customer.sale.wizard'
    _description = 'Customer Sale Report'

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    @api.multi
    def check_report(self):
        
        print('ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZz')
        return self._print_report({})

    def _print_report(self, data):
        print('|||||||||||||||||||||||||||||||||||||||||||||||||',self)
        return self.env['report'].get_action(self, 'customer_sale_report.report_customersale', data=data)
