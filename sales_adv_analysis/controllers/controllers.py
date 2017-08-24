# -*- coding: utf-8 -*-
from odoo import http

# class SalesAdvAnalysis(http.Controller):
#     @http.route('/sales_adv_analysis/sales_adv_analysis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_adv_analysis/sales_adv_analysis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_adv_analysis.listing', {
#             'root': '/sales_adv_analysis/sales_adv_analysis',
#             'objects': http.request.env['sales_adv_analysis.sales_adv_analysis'].search([]),
#         })

#     @http.route('/sales_adv_analysis/sales_adv_analysis/objects/<model("sales_adv_analysis.sales_adv_analysis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_adv_analysis.object', {
#             'object': obj
#         })