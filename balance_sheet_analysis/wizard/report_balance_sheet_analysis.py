
from odoo import api, fields, models


class BalanceSheetAnalysisReport(models.TransientModel):

    _name = 'balance.sheet.analysis.report'
    _description = 'Balance Sheet Analysis Report'

    @api.model
    def _get_account_report(self):
        reports = []
        if self._context.get('active_id'):
            menu = self.env['ir.ui.menu'].browse(self._context.get('active_id')).name
            print('-------------- menu:',menu)
            reports = self.env['account.financial.report'].search([('name', 'ilike', menu)])
        return reports and reports[0] or False


    date_from = fields.Datetime(string='Start Date')
    date_to = fields.Datetime(string='End Date')
    account_report_id = fields.Many2one('account.financial.report', string='Account Reports', required=True, default=_get_account_report)

 

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['account_report_id','date_from', 'date_to'])[0]
        #data['form']['used_context'] = dict(used_context, lang=self.env.context.get('lang', 'en_US'))

        return self._print_report(data)

    def _print_report(self, data):
     
        return self.env['report'].get_action(self, 'balance_sheet_analysis.report_sheetanalysis', data=data)
