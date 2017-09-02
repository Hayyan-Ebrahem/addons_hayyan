
from odoo import api, fields, models


class BalanceSheetAnalysisReport(models.TransientModel):

    _name = 'balance.sheet.analysis.report'
    _description = 'Balance Sheet Analysis Report'

    date_from = fields.Datetime(string='Start Date')
    date_to = fields.Datetime(string='End Date')

 

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['date_from', 'date_to'])[0]
        return self._print_report(data)

    def _print_report(self, data):
    	data['form'].update(self.read(['date_from', 'date_to'])[0])
        print('+++++++++++_______-----------',data,' self :',self)
     
        return self.env['report'].get_action(self, 'balance_sheet_analysis.report_sheetanalysis', data=data)
