# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BalanceAnalysis(models.AbstractModel):
    _name = 'report.balance_sheet_analysis.balance_analysis'
    #_inherit = 'report.account.report_financial'
    print(' BALANCE_SHEET')
    
    def _get_dataframe(self, report):
    	lines = self.with_context(data['form'].get('used_context'))._get_accounts(accounts, display_account)
        print('YESSSSSSSSSSSSSSYESSSSSSSSSSSSSSSSSSSSSSSSYESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
    	df = pd.DataFrame(lines,columns=['name'])
    	return df
    	

    def _compute_current_ratio(self,report):
    	return ' CURRENT RATIO'

    @api.model
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        report_lines = self.with_context(data['form'].get('used_context'))._get_accounts(accounts, display_account)
        df = pd.DataFrame(report_lines)
        print('yessssssssssssssssssssssssssssssssssssssssssssssssssssssss\n\n')
        # print('report_lines ::', report_lines)
        # print('\n\n type(report_lines):',type(report_lines))

        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'get_account_lines': report_lines,
        }
        return self.env['report'].render('balance_sheet_analysis.balance_analysis', docargs)