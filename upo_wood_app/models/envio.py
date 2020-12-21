from odoo import models, fields, api

class Envio(models.Model):
    _name = 'upo_wood_app.envio'
    _description = 'Clase envio para UPOWOOD'

    name = fields.Integer("Numero de envio", required=True)
    direccion = fields.Text("Direccion del envio",required=True)
    cp = fields.Integer('Codigo postal',required=True)
    fechaEnvio = fields.Date('Fecha de envio',required=True, autodate = True)
    fechaLlegada = fields.Date('Fecha de llegada prevista',required=True)
    state = fields.Selection([('preparando','Preparando'),('enviado','Enviado'),('reparto','En reparto'),('entregado','Entregado'),('cancelado','Cancelado')],'Estado',default='preparando')
    #Añadir las relaciones entre clases
    venta_id = fields.Many2one("upo_wood_app.venta",string="Venta relacionada con el envio")
    albaran_id = fields.Many2one("upo_wood_app.albaran",string="Albaran relacionado con el envio")
    _sql_constraints = [('envio_name_unique','UNIQUE (name)','El número del envío debe ser único')]

    def btn_submit_to_preparando(self):
        self.write({'state':'preparando'})
    
    def btn_submit_to_enviado(self):
        self.write({'state':'enviado'})
    
    def btn_submit_to_reparto(self):
        self.write({'state':'reparto'})

    def btn_submit_to_entregado(self):
        self.write({'state':'entregado'})

    def btn_submit_to_cancelado(self):
        self.write({'state':'cancelado'}) 
    