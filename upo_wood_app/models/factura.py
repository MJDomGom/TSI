from odoo import models, fields, api

class Factura(models.Model):
    _name = 'upo_wood_app.factura'
    _description = 'Clase factura para UPOWOOD'

    name = fields.Integer("Numero de factura", required=True)
    fecha = fields.Date('Fecha de la factura',required=True, autodate = True)
    #Añadir las relaciones entre clases
    venta_id = fields.Many2one("upo_wood_app.venta",string="Venta asociada a la factura")    
    _sql_constraints = [('factura_name_unique','UNIQUE (name)','El número de la factura debe ser único')]