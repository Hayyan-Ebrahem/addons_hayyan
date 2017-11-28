# -*- coding: utf-8 -*-
from odoo import http

# class CustomerPricelistReport(http.Controller):
#     @http.route('/customer_pricelist_report/customer_pricelist_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_pricelist_report/customer_pricelist_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_pricelist_report.listing', {
#             'root': '/customer_pricelist_report/customer_pricelist_report',
#             'objects': http.request.env['customer_pricelist_report.customer_pricelist_report'].search([]),
#         })

#     @http.route('/customer_pricelist_report/customer_pricelist_report/objects/<model("customer_pricelist_report.customer_pricelist_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_pricelist_report.object', {
#             'object': obj
#         })