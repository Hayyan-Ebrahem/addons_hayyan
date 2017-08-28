from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    adv_cost = fields.Float('Adv Cost', digits=dp.get_precision('Product Price'), store=True, default=2.0)


# class ProductProduct(models.Model):
#     _inherit = 'product.product'

#     advertising_cost = fields.Float('Adv Cost', digits=dp.get_precision('Product Price'), store=True, default=2.0)
