# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    adv_cost = fields.Many2one('product.product', 'Advertising', readonly=True)

    def _select(self):
        return super(SaleReport, self)._select() + ", p.adv_cost as adv_cost"

    def _group_by(self):
        return super(SaleReport, self)._group_by() + ", p.adv_cost"
