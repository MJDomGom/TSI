from odoo import models, fields, api
import re


class Persona(models.Model):
    _name = 'upo_wood_app.persona'
    _description = 'Clase persona para UPOWOOD'

    nombre = fields.Char(string="Nombre del usuario",
                         required=True, help="Nombre del usuario en el sistema")
    password = fields.Char(string="Contraseña", required=True)
    direccion = fields.Text("Direccion del usuario", required=True)
    name = fields.Char(string="DNI o CIF del usuario", required=True)
    email = fields.Char(string="email del usuario", required=True)
    telefono = fields.Integer("Numero de telefono")
    foto = fields.Binary("Foto usuario")
    isEmpleado = fields.Selection([('empleado', 'Empleado'), (
        'cliente', 'Cliente')], "El usuario es empleado o cliente?", required=True)
    # Añadir las relaciones entre clases
    venta_ids = fields.Many2many(
        "upo_wood_app.venta", string="Ventas asociadas a la persona")
    _sql_constraints = [('persona_name_unique', 'UNIQUE (name)',
                         'El dni de la persona ya está registrado')]

    @api.constrains('name')
    def _check_name(self):
            if not re.match("/^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$/",self.name):
                raise models.ValidationError('Formato de DNI erroneo')
