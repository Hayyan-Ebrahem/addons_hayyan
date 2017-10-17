# -*- coding: utf-8 -*-
import time
from odoo import models, fields, api


class BalanceSheetAnalysisReport(models.AbstractModel):
    _name = 'report.balance_sheet_analysis.report_balanceanalysis'
    _inherit = 'report.account.report_financial'
    print(' BALANCE_SHEET')


    def _compute_current_ratio(self,lines):
        for line in lines:
            print(line.get('balance'),line.get('name'),line.get('account_type'))
    	return lines[0]['balance']


    def _compute_quick_ratio(self,lines):
        return lines['balance']



    def _compute_working_capital(self,lines):
        return lines['balance']


    @api.model
    def render_html(self, docids, data=None):
        if not data.get('form') or not self.env.context.get('active_model') or not self.env.context.get('active_id'):
            raise UserError(_("Form content is missing, this report cannot be printed."))
            
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))        
        print('\n\n')
        print('---------------------------------- data :',data)
      
        lines = super(BalanceSheetAnalysisReport,self).get_account_lines(data.get('form'))
        print ('----------- lines:',lines)

        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'current_ratio': self._compute_current_ratio(lines),
        }
        return self.env['report'].render('balance_sheet_analysis.report_balanceanalysis', docargs)