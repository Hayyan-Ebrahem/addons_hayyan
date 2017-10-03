# -*- coding: utf-8 -*-
from odoo import http

# class SaleOrderProcessReport(http.Controller):
#     @http.route('/sale_order_process_report/sale_order_process_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_process_report/sale_order_process_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_process_report.listing', {
#             'root': '/sale_order_process_report/sale_order_process_report',
#             'objects': http.request.env['sale_order_process_report.sale_order_process_report'].search([]),
#         })

#     @http.route('/sale_order_process_report/sale_order_process_report/objects/<model("sale_order_process_report.sale_order_process_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_process_report.object', {
#             'object': obj
#         })