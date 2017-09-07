from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class Product(models.Model):
    _name = 'product.product'
    _inherit = 'product.product'

    advertising = fields.Float(compute='_compute_adv_cost', digits=dp.get_precision('Product Adv Price'), store=True)

    @api.depends('order_line.product_id.adv_cost')
    def _compute_adv_cost(self):
        """
        Compute the total amounts of the SO Adv Cost.
        """
        for order in self:
            advertising = 0.0
            print('---------- self.cost :',self.cost)
            if self.cost != 0:
                for line in order.order_line:
                    advertising += line.product_id.adv_cost

            order.update({
                'advertising': advertising
           
            })




    