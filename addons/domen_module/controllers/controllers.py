# from odoo import http


# class DomenModule(http.Controller):
#     @http.route('/domen_module/domen_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/domen_module/domen_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('domen_module.listing', {
#             'root': '/domen_module/domen_module',
#             'objects': http.request.env['domen_module.domen_module'].search([]),
#         })

#     @http.route('/domen_module/domen_module/objects/<model("domen_module.domen_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('domen_module.object', {
#             'object': obj
#         })

