from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    advertising = fields.Float(compute='_compute_adv_cost', digits=dp.get_precision('Product Price'), store=True)


    def _compute_adv_cost(self):
        """
        Compute the total amounts of the SO Adv Cost.
        """
        for order in self:
            for line in order.order_line:
                # FORWARDPORT UP TO 10.0
                adv_cost = line.adv_cost
            order.update({
                'advertising': order.adv_cost
           
            })