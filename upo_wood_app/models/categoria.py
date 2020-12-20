from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'upo_wood_app.categoria'
    _description = 'Clase categoria para UPOWOOD'

    name = fields.Char(string="Nombre de la categoria",required=True)
    descripcion = fields.Text("Descripcion de la categoria en cuestion")
    #Añadir las relaciones entre clases
    producto_id = fields.One2many("upo_wood_app.producto","categoria_id","Producto relacionado con la categoria")
    _sql_constraints = [('categoria_name_unique','UNIQUE (name)','Ya existe una categoría con ese nombre')]