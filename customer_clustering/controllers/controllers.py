# -*- coding: utf-8 -*-
from odoo import http

# class CustomerClustering(http.Controller):
#     @http.route('/customer_clustering/customer_clustering/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_clustering/customer_clustering/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_clustering.listing', {
#             'root': '/customer_clustering/customer_clustering',
#             'objects': http.request.env['customer_clustering.customer_clustering'].search([]),
#         })

#     @http.route('/customer_clustering/customer_clustering/objects/<model("customer_clustering.customer_clustering"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_clustering.object', {
#             'object': obj
#         })