# -*- coding: utf-8 -*-
from odoo import http

# class IncomeStatement(http.Controller):
#     @http.route('/income_statement/income_statement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/income_statement/income_statement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('income_statement.listing', {
#             'root': '/income_statement/income_statement',
#             'objects': http.request.env['income_statement.income_statement'].search([]),
#         })

#     @http.route('/income_statement/income_statement/objects/<model("income_statement.income_statement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('income_statement.object', {
#             'object': obj
#         })