# -*- coding: utf-8 -*-
from odoo import http

# class BalanceSheetAnalysis(http.Controller):
#     @http.route('/balance_sheet_analysis/balance_sheet_analysis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/balance_sheet_analysis/balance_sheet_analysis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('balance_sheet_analysis.listing', {
#             'root': '/balance_sheet_analysis/balance_sheet_analysis',
#             'objects': http.request.env['balance_sheet_analysis.balance_sheet_analysis'].search([]),
#         })

#     @http.route('/balance_sheet_analysis/balance_sheet_analysis/objects/<model("balance_sheet_analysis.balance_sheet_analysis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('balance_sheet_analysis.object', {
#             'object': obj
#         })