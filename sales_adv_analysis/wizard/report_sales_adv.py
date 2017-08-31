
from odoo import fields, models


class SalesAdvReport(models.TransientModel):
    _name = 'salesadv.report'
    _description = 'rfrfrferfref'

    salesadv_id = fields.Many2one('res.users', required=True)
    date_from = fields.Datetime(string='Start Date')
    date_to = fields.Datetime(string='End Date')

    def _print_report(self, data):
        data = self.pre_print_report(data)
        records = self.env[data['model']].browse(data.get('ids', []))
        return self.env['report'].get_action(records, 'sales_adv_analysis.report_salesadv', data=data)
