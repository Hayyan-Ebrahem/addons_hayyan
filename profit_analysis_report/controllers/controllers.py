# -*- coding: utf-8 -*-
from odoo import http

# class ProfitAnalysisReport(http.Controller):
#     @http.route('/profit_analysis_report/profit_analysis_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/profit_analysis_report/profit_analysis_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('profit_analysis_report.listing', {
#             'root': '/profit_analysis_report/profit_analysis_report',
#             'objects': http.request.env['profit_analysis_report.profit_analysis_report'].search([]),
#         })

#     @http.route('/profit_analysis_report/profit_analysis_report/objects/<model("profit_analysis_report.profit_analysis_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('profit_analysis_report.object', {
#             'object': obj
#         })