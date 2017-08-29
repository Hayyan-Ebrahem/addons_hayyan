# -*- coding: utf-8 -*-

from odoo import fields, models


class SalesAdvReport(models.TransientModel):
    _name = 'sale.adv.report'
    _description = 'Sales Advertising Analysis'


    def _print_report(self, data):
        data = self.pre_print_report(data)
        records = self.env[data['model']].browse(data.get('ids', []))
        return self.env['report'].get_action(records, 'account.report_trialbalance', data=data)
