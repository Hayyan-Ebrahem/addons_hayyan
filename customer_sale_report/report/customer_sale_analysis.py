import time
from odoo import api,fields, models


class CustomerSaleReport(models.AbstractModel):
    _name = 'report.customer_sale_report.report_customersale'

    @api.model
    def render_html(self, docids, data=None):
        # if not data.get('form') or not self.env.context.get('active_model') or not self.env.context.get('active_id'):
        #     raise UserError(_("Form content is missing, this report cannot be printed."))
            
        lines =[]
        sale_report = self.env['report']._get_report_from_name('customer_sale_report.report_customersale')
        print(sale_report.model)

        sale_order = self.env['sale.order'].search([])  
        for order in sale_order:
            lines.append(order.partner_id)
        for cus in lines:
            print('-----',cus.name)

        docargs = {
            'doc_ids': self.ids,
            'doc_model': sale_report.model,
            'time': time,
            'get_account_lines': lines,
        }
        return self.env['report'].render('customer_sale_report.report_customersale', docargs)