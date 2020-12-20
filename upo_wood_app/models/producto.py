from odoo import models, fields, api

class Producto(models.Model):
    _name = 'upo_wood_app.producto'
    _description = 'Clase producto para UPOWOOD'

    name = fields.Char(string="Nombre del producto", required=True)
    fechaFabricacion = fields.Date("Fecha de la fabricacion del producto",required=True)
    precio = fields.Integer("Precio del producto",required=True)
    stock = fields.Integer("Stock del producto",required=True)
    foto = fields.Binary("FotoProducto")
    #Añadir las relaciones entre clases
    venta_ids = fields.Many2many("upo_wood_app.venta",string="Venta asociados al producto") 
    categoria_id = fields.Many2one("upo_wood_app.categoria",string="Categoria asociada al producto")
    material_id = fields.Many2one("upo_wood_app.material",string="Material asociado al producto")
    _sql_constraints = [('producto_name_unique','UNIQUE (name)','Ya existe un producto con ese nombre')]