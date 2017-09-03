# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BalanceSheetAnalysisReport(models.AbstractModel):
    _name = 'report.balance_sheet_analysis.report_sheetanalysis'
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
        print('############### data:',data)
        print('\n\n')
        accounts =  self.env['account.financial.report'].browse([5,6])
        data['form']['account_report_id']=accounts#.update('account_report_id',4)

        print('\n\n')
        print('########### accounts :',accounts)
        #account_res = super(BalanceSheetAnalysisReport,self).get_account_lines(data)
        report_lines = self.get_account_lines(data.get('form'))
        print('report_lines ::', report_lines)
        # print('\n\n type(report_lines):',type(report_lines))

        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'get_account_lines': report_lines,
        }
        return self.env['report'].render('balance_sheet_analysis.report_sheetanalysis', docargs)