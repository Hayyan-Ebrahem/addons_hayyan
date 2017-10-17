# -*- coding: utf-8 -*-
from odoo import http

# class LostSaleOrderReport(http.Controller):
#     @http.route('/lost_sale_order_report/lost_sale_order_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lost_sale_order_report/lost_sale_order_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lost_sale_order_report.listing', {
#             'root': '/lost_sale_order_report/lost_sale_order_report',
#             'objects': http.request.env['lost_sale_order_report.lost_sale_order_report'].search([]),
#         })

#     @http.route('/lost_sale_order_report/lost_sale_order_report/objects/<model("lost_sale_order_report.lost_sale_order_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lost_sale_order_report.object', {
#             'object': obj
#         })