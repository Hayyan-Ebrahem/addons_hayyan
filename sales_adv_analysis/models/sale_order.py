from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    advertising = fields.Float(compute='_compute_adv_cost', digits=dp.get_precision('Product Price'), store=True)

    @api.depends('order_line.product_id.adv_cost')
    def _compute_adv_cost(self):
        """
        Compute the total amounts of the SO Adv Cost.
        """
        for order in self:
            advertising = 0.0
            for line in order.order_line:
                advertising += line.product_id.adv_cost
            print(line.order_id,'  ',advertising)

            order.update({
                'advertising': advertising
           
            })



    