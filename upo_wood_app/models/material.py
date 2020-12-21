from odoo import models, fields, api


class Material(models.Model):
    _name = 'upo_wood_app.material'
    _description = 'Clase material para UPOWOOD'

    idMaterial = fields.Integer("Numero del material", required=True)
    name = fields.Char(string="Nombre del material", required=True)
    descripcion = fields.Text("Descripcion del material en cuestion")
    precio = fields.Integer("Precio del material", required=True)
    foto = fields.Binary("FotoMaterial")
    # Añadir las relaciones entre clases
    producto_id = fields.One2many(
        "upo_wood_app.producto", "material_id", "Producto relacionado con el material")
    proveedor_ids = fields.Many2many(
        "upo_wood_app.proveedor", string="Proveedor relacionado con el material")
    _sql_constraints = [('material_idmaterial_unique', 'UNIQUE (idMaterial)',
                         'El idMaterial del material debe ser único')]

    # Funcion para que la descripcion no sobrepase 100 caracteres
    @api.constrains('descripcion')
    def _check_len_content(self):
        if len(self.descripcion) > 100:
            raise models.ValidationError(
                'Solo se permite descripciones de un tamaño menor de 100 caracteres')
