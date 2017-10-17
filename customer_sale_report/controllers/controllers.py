# -*- coding: utf-8 -*-
from odoo import http

# class CustomerSaleReport(http.Controller):
#     @http.route('/customer_sale_report/customer_sale_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_sale_report/customer_sale_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_sale_report.listing', {
#             'root': '/customer_sale_report/customer_sale_report',
#             'objects': http.request.env['customer_sale_report.customer_sale_report'].search([]),
#         })

#     @http.route('/customer_sale_report/customer_sale_report/objects/<model("customer_sale_report.customer_sale_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_sale_report.object', {
#             'object': obj
#         })