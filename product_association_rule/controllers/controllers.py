# -*- coding: utf-8 -*-
from odoo import http

# class ProductAssociationRule(http.Controller):
#     @http.route('/product_association_rule/product_association_rule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_association_rule/product_association_rule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_association_rule.listing', {
#             'root': '/product_association_rule/product_association_rule',
#             'objects': http.request.env['product_association_rule.product_association_rule'].search([]),
#         })

#     @http.route('/product_association_rule/product_association_rule/objects/<model("product_association_rule.product_association_rule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_association_rule.object', {
#             'object': obj
#         })