from odoo import models, fields, api

class Envio(models.Model):
    _name = 'upo_wood_app.envio'
    _description = 'Clase envio para UPOWOOD'

    name = fields.Integer("Numero de envio", required=True)
    direccion = fields.Text("Direccion del envio",required=True)
    cp = fields.Integer('Codigo postal',required=True)
    fechaEnvio = fields.Date('Fecha de envio',required=True, autodate = True)
    fechaLlegada = fields.Date('Fecha de llegada prevista',required=True)
    #Añadir las relaciones entre clases
    venta_id = fields.Many2one("upo_wood_app.venta",string="Venta relacionada con el envio")
    albaran_id = fields.Many2one("upo_wood_app.albaran",string="Albaran relacionado con el envio")
    _sql_constraints = [('envio_name_unique','UNIQUE (name)','El número del envío debe ser único')]