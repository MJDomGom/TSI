from odoo import models, fields, api


class Devolucion(models.Model):
    _name = 'upo_wood_app.devolucion'
    _description = 'Clase devolucion para UPOWOOD'

    name = fields.Integer("Numero de devolucion", required=True)
    motivo = fields.Text(
        'Descripcion del motivo de la devolucion', required=True)
    isAprobado = fields.Boolean("Devolucion aprobada o denegada")
    fechaDevolucion = fields.Date(
        'Fecha de la devolucion', required=True, autodate=True)
    state = fields.Selection([('aprobado', 'Aprobado'), ('denegado', 'Denegado'), (
        'pendiente', 'Pendiente')], 'Estado', default='pendiente')
    # Añadir las relaciones entre clases
    venta_id = fields.Many2one(
        "upo_wood_app.venta", string="Venta relacionada con la devolucion")
    _sql_constraints = [('devolucion_name_unique', 'UNIQUE (name)',
                         'El número de la devolución debe ser único')]

    # Funcion para los workflows, si cambia el atributo isAprobado, el atributo state cambiara acorde a lo que ponga isAprobado
    @api.constrains('isAprobado')
    def btn_submit_to_isAprobado(self):
        if self.isAprobado == True:
            self.write({'state': 'aprobado'})
        else:
            self.write({'state': 'denegado'})

    # Funcion para que la descripcion del motivo no sobrepase 100 caracteres
    @api.constrains('motivo')
    def _check_len_content(self):
        if len(self.motivo) > 100:
            raise models.ValidationError(
                'Solo se permite explicaciones de un tamaño menor de 100 caracteres')
