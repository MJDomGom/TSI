from odoo import models, fields, api
class Venta(models.Model):
    _name = 'upo_wood_app.venta'
    _description = 'Clase venta para UPOWOOD'

    name = fields.Integer("Numero de venta", required=True)
    IVA = fields.Integer("IVA asociado a la venta")
    fechaVenta = fields.Date("Fecha de la venta",required=True, autodate = True)
    total = fields.Integer("Cantidad total de la venta",required=True)
    #Añadir las relaciones entre clases
    producto_ids = fields.Many2many("upo_wood_app.producto",string="Productos asociados a la venta")
    persona_ids = fields.Many2many("upo_wood_app.persona",string="Personas asociados a la venta")
    #Relaciones one to one
    devolucion_id = fields.Many2one("upo_wood_app.devolucion",string="Devolucion asociada a la venta")
    envio_id = fields.Many2one("upo_wood_app.envio",string="Envio asociado a la venta")
    factura_id = fields.Many2one("upo_wood_app.factura",string="Factura asociado a la venta")
    _sql_constraints = [('venta_name_unique','UNIQUE (name)','El número de la venta debe ser único')]

    #Funcion para que el IVA no sea un numero negativo
    @api.constrains('IVA')
    def _check_IVA(self):
        if self.IVA < 0:
            raise models.ValidationError('El IVA debe ser un numero positivo, no puede ser un numero negativo')

