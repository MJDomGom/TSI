from odoo import models, fields, api

class Devolucion(models.Model):
    _name = 'upo_wood_app.devolucion'
    _description = 'Clase devolucion para UPOWOOD'

    name = fields.Integer("Numero de devolucion", required=True)
    motivo = fields.Text('Descripcion del motivo de la devolucion',required=True)
    isAprobado = fields.Boolean("Devolucion aprobada o denegada")
    fechaDevolucion = fields.Date('Fecha de la devolucion',required=True, autodate = True)
    #Añadir las relaciones entre clases
    venta_id = fields.Many2one("upo_wood_app.venta",string="Venta relacionada con la devolucion")
    _sql_constraints = [('devolucion_name_unique','UNIQUE (name)','El número de la devolución debe ser único')]