# -*- coding: utf-8 -*-
from odoo import http

# class PurchaseAnalysisReport(http.Controller):
#     @http.route('/purchase_analysis_report/purchase_analysis_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_analysis_report/purchase_analysis_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_analysis_report.listing', {
#             'root': '/purchase_analysis_report/purchase_analysis_report',
#             'objects': http.request.env['purchase_analysis_report.purchase_analysis_report'].search([]),
#         })

#     @http.route('/purchase_analysis_report/purchase_analysis_report/objects/<model("purchase_analysis_report.purchase_analysis_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_analysis_report.object', {
#             'object': obj
#         })