# -*- coding: utf-8 -*-
from odoo import http

# class PricelistClusteringBased(http.Controller):
#     @http.route('/pricelist_clustering_based/pricelist_clustering_based/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pricelist_clustering_based/pricelist_clustering_based/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pricelist_clustering_based.listing', {
#             'root': '/pricelist_clustering_based/pricelist_clustering_based',
#             'objects': http.request.env['pricelist_clustering_based.pricelist_clustering_based'].search([]),
#         })

#     @http.route('/pricelist_clustering_based/pricelist_clustering_based/objects/<model("pricelist_clustering_based.pricelist_clustering_based"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pricelist_clustering_based.object', {
#             'object': obj
#         })