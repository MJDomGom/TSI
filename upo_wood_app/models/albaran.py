from odoo import models, fields, api


class Albaran(models.Model):
    _name = 'upo_wood_app.albaran'
    _description = 'Clase albaran para UPOWOOD'

    # Atributo creado para que odoo ponga Albaran / numero , pero este atributo no esta en el uml
    name = fields.Integer("Numero de albaras", required=True)
    isEntregado = fields.Boolean(
        "Se ha realizado el envio correctamente?", required=True)
    fechaLlegada = fields.Date('Fecha de llegada prevista', required=True)
    descripcion = fields.Text(
        "Descripcion de la llegada y, en caso de problemas, motivo de no haber realizado la entrega")
    # Añadir las relaciones entre clases
    envio_id = fields.Many2one(
        "upo_wood_app.venta", string="Envio relacionado con el albaran")
    _sql_constraints = [('albaran_name_unique', 'UNIQUE (name)',
                         'El número del albarán debe ser único')]

    # Funcion para que la descripcion no sobrepase 100 caracteres
    @api.constrains('descripcion')
    def _check_len_content(self):
        if len(self.descripcion) > 100:
            raise models.ValidationError(
                'Solo se permite descripciones de un tamaño menor de 100 caracteres')
