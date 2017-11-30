import time
from odoo import api,fields, models


class CustomerSaleReport(models.AbstractModel):
    _name = 'report.customer_sale_report.report_customersale'



    name = fields.Char('Order Reference', readonly=True)
    date = fields.Datetime('Date Order', readonly=True)
    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    product_uom = fields.Many2one('product.uom', 'Unit of Measure', readonly=True)
    product_uom_qty = fields.Float('# of Qty', readonly=True)
    qty_delivered = fields.Float('Qty Delivered', readonly=True)
    qty_to_invoice = fields.Float('Qty To Invoice', readonly=True)
    qty_invoiced = fields.Float('Qty Invoiced', readonly=True)
    partner_id = fields.Many2one('res.partner', 'Partner', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', readonly=True)
    user_id = fields.Many2one('res.users', 'Salesperson', readonly=True)
    unit_price = fields.Float('Total', readonly=True)
    price_subtotal = fields.Float('Untaxed Total', readonly=True)
    product_tmpl_id = fields.Many2one('product.template', 'Product Template', readonly=True)
    categ_id = fields.Many2one('product.category', 'Product Category', readonly=True)
    nbr = fields.Integer('# of Quantity', readonly=True)
    pricelist_id = fields.Many2one('product.pricelist', 'Pricelist', readonly=True)
    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', readonly=True)
    team_id = fields.Many2one('crm.team', 'Sales Team', readonly=True, oldname='section_id')
    country_id = fields.Many2one('res.country', 'Partner Country', readonly=True)
    commercial_partner_id = fields.Many2one('res.partner', 'Commercial Entity', readonly=True)

    # @api.model
    # def render_html(self, docids, data=None):
    #     # if not data.get('form') or not self.env.context.get('active_model') or not self.env.context.get('active_id'):
    #     #     raise UserError(_("Form content is missing, this report cannot be printed."))
            
    #     lines =[]
    #     sale_report = self.env['report']._get_report_from_name('customer_sale_report.report_customersale')
    #     print(sale_report.model)

    #     sale_order = self.env['sale.order'].search([])  
    #     for order in sale_order:
    #         lines.append(order.partner_id)
    #     for cus in lines:
    #         print('-----',cus.name)

    #     docargs = {
    #         'doc_ids': self.ids,
    #         'doc_model': sale_report.model,
    #         'time': time,
    #         'get_account_lines': lines,
    #     }
    #     return self.env['report'].render('customer_sale_report.report_customersale', docargs)