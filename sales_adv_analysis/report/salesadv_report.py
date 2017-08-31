# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api


class ReportSalesAdv(models.AbstractModel):
    _name = 'report.sales_adv_analysis.report_salesadv'
    print(' SALE ADV')
    
    # def _get_dataframe(self):
    # 	print('self:',self)
    # 	lines = self.with_context(data['form'].get('used_context'))._get_accounts(accounts, display_account)
    # 	df = pd.DataFrame(lines,columns=['sale','advertising'])
    # 	return df
    	

    # def _compute_current_ratio(self):
    # 	return ' CURRENT RATIO'

    @api.model
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        sales_records = []
        orders = self.env['sale.order'].search([('user_id', '=', docs.company_id.id)])
        if docs.date_from and docs.date_to:
            for order in orders:
                sales_records.append(order);

        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'orders': sales_records,
        }
        return self.env['report'].render('sales_adv_analysis.report_salesadv', docargs)