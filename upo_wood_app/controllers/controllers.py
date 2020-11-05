# -*- coding: utf-8 -*-
# from odoo import http


# class UpoWoodApp(http.Controller):
#     @http.route('/upo_wood_app/upo_wood_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upo_wood_app/upo_wood_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upo_wood_app.listing', {
#             'root': '/upo_wood_app/upo_wood_app',
#             'objects': http.request.env['upo_wood_app.upo_wood_app'].search([]),
#         })

#     @http.route('/upo_wood_app/upo_wood_app/objects/<model("upo_wood_app.upo_wood_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upo_wood_app.object', {
#             'object': obj
#         })
