# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SalesAdvReport(models.AbstractModel):
    _name = 'report.sales_adv_analysis.salesadv_report'
    print(' SALE ADV')
    
    def _get_dataframe(self, report):
    	print('self:',self)
    	lines = self.with_context(data['form'].get('used_context'))._get_accounts(accounts, display_account)
    	df = pd.DataFrame(lines,columns=['sale','advertising'])
    	return df
    	

    def _compute_current_ratio(self,report):
    	return ' CURRENT RATIO'

    @api.model
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        report_lines = self.with_context(data['form'].get('used_context'))._get_accounts(accounts, display_account)
        df = self._get_dataframe(report_lines)
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