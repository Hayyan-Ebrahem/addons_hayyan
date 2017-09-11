# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api
import pandas as pd

class ReportSalesAdv(models.AbstractModel):
    _name = 'report.sales_adv_analysis.report_salesadv'
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    def _get_dataframe(self):
    	print('self:',self)
        self.model = self.env.context.get('active_model')
        sales_records = []
        orders = self.env['sale.order'].search([('state', 'in', ['sale','done'])])
        for order in orders:
            res = dict((fn, 0.0) for fn in ['total', 'advertising'])
            order._compute_adv_cost()
            print('   ======== order ',order.amount_total)
            res['total'] = order.amount_total
            res['advertising'] = order.advertising
            sales_records.append(res)
        df = pd.DataFrame(sales_records)

        return df

    # def _compute_current_ratio(self):
    # 	return ' CURRENT RATIO'

    @api.model
    def render_html(self, docids, data=None):
        if not data.get('form') or not self.env.context.get('active_model'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        account_res = self._get_dataframe()
        print('============ ::',account_res)
      
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'orders': account_res,
        }
        return self.env['report'].render('sales_adv_analysis.report_salesadv', docargs)