# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api
import pandas as pd

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
        orders = self.env['sale.order'].search([('state', 'in', ['sale','done'])])
        if docs.date_from and docs.date_to:
            for order in orders:
                res = dict((fn, 0.0) for fn in ['total', 'advertising'])

                order._compute_adv_cost()
                print('   ======== order ',order.amount_total)
                res['total'] = order.amount_total
                res['advertising'] = order.advertising
                sales_records.append(res)

        print('==================== sales_recoreds :',sales_records)
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'orders': pd.DataFrame(sales_records),
        }
        print('==================== orders as DF:',docargs['orders'].describe())
        return self.env['report'].render('sales_adv_analysis.report_salesadv', docargs)