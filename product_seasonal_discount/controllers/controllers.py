# -*- coding: utf-8 -*-
from odoo import http

# class ProductSeasonalDiscount(http.Controller):
#     @http.route('/product_seasonal_discount/product_seasonal_discount/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_seasonal_discount/product_seasonal_discount/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_seasonal_discount.listing', {
#             'root': '/product_seasonal_discount/product_seasonal_discount',
#             'objects': http.request.env['product_seasonal_discount.product_seasonal_discount'].search([]),
#         })

#     @http.route('/product_seasonal_discount/product_seasonal_discount/objects/<model("product_seasonal_discount.product_seasonal_discount"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_seasonal_discount.object', {
#             'object': obj
#         })