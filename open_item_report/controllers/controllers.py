# -*- coding: utf-8 -*-
from odoo import http

# class OpenItemReport(http.Controller):
#     @http.route('/open_item_report/open_item_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_item_report/open_item_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_item_report.listing', {
#             'root': '/open_item_report/open_item_report',
#             'objects': http.request.env['open_item_report.open_item_report'].search([]),
#         })

#     @http.route('/open_item_report/open_item_report/objects/<model("open_item_report.open_item_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_item_report.object', {
#             'object': obj
#         })