
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

 

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['date_from', 'date_to'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        print('+++++++++++_______----------- data :',data)
     
        return self.env['report'].get_action(self, 'balance_sheet_analysis.report_sheetanalysis', data=data)
