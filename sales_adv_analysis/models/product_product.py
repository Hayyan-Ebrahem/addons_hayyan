from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class ProductProduct(models.Model):
    _name = 'product.product'
    _inherit = 'product.product'


    adv_cost = fields.Float('Adv Cost', digits=dp.get_precision('Product Price'), store=True, default=0.0)
