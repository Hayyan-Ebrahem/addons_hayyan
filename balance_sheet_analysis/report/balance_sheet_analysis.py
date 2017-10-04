# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api


class BalanceSheetAnalysisReport(models.AbstractModel):
    _name = 'balance_sheet_analysis.report_sheet_analysis'
    _inherit = 'report.account.report_financial'
    print(' BALANCE_SHEET')


    def _compute_report_sheetnalysis(self,report):
    	return ' CURRENT RATIO'

    @api.model
    def render_html(self, docids, data=None):
        if not data.get('form') or not self.env.context.get('active_model') or not self.env.context.get('active_id'):
            raise UserError(_("Form content is missing, this report cannot be printed."))
            
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))        
        print('\n\n')
        print('---------------------------------- data :',data)
      
        account_res = self.get_account_lines(data.get('form'))


        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'get_account_lines': account_res,
        }
        return self.env['report'].render('balance_sheet_analysis.report_sheet_analysis', docargs)