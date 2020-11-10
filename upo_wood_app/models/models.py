# -*- coding: utf-8 -*-

 from odoo import models, fields, api


# class upo_wood_app(models.Model):
#     _name = 'upo_wood_app.upo_wood_app'
#     _description = 'upo_wood_app.upo_wood_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Venta(models.Model):
    _name = 'upo_wood_app.venta'
    _description = 'Clase venta para UPOWOOD'

    idVenta = fields.Integer("Numero de venta", required=True)
    IVA = fields.Integer("IVA asociado a la venta")
    fechaVenta = fields.Date('Fecha de la venta',required=True, autodate = True)
    total = fields.Integer('Cantidad total de la venta',required=True)
    #Añadir las relaciones entre clases


class Devolucion(models.Model):
    _name = 'upo_wood_app.devolucion'
    _description = 'Clase devolucion para UPOWOOD'

    motivo = fields.Text('Descripcion del motivo de la devolucion',required=True)
    isAprobado = fields.Boolean("Devolucion aprobada o denegada")
    fechaDevolucion = fields.Date('Fecha de la devolucion',required=True, autodate = True)
    #Añadir las relaciones entre clases


class Envio(models.Model):
    _name = 'upo_wood_app.envio'
    _description = 'Clase envio para UPOWOOD'

    idEnvio = fields.Integer("Numero de envio", required=True)
    direccion = fields.Text("Direccion del envio",required=True)
    cp = fields.Integer('Codigo postal',required=True)
    fechaEnvio = fields.Date('Fecha de envio',required=True, autodate = True)
    fechaLlegada = fields.Date('Fecha de llegada prevista',required=True)
    #Añadir las relaciones entre clases

class Albaran(models.Model):
    _name = 'upo_wood_app.albaran'
    _description = 'Clase albaran para UPOWOOD'

    isEntregado = fields.Boolean("Se ha realizado el envio correctamente?",required=True)
    fechaLlegada = fields.Date('Fecha de llegada prevista',required=True)
    descripcion = fields.Text("Descripcion de la llegada y, en caso de problemas, motivo de no haber realizado la entrega")
    #Añadir las relaciones entre clases

class Persona(models.Model):
    _name = 'upo_wood_app.persona'
    _description = 'Clase persona para UPOWOOD'

    usuario = fields.Char(string="Nombre del usuario",required=True, help = "Nombre del usuario en el sistema")
    password = fields.Char(string="Contraseña",required=True)
    #Preguntar a Aurelio como poner el campo pass mejor
    direccion = fields.Text("Direccion del usuario",required=True)
    dni =fields.Char(string="DNI o CIF del usuario",required=True)
    email = fields.Char(string="email del usuario",required=True)
    #Preguntar a Aurelio como poner el campo mail mejor
    telefono = fields.Integer("Numero de telefono")
    foto = fields.Binary("Foto usuario")
    isEmpleado = fields.Boolean("El usuario es empleado o cliente?",required=True)
    #Añadir las relaciones entre clases

class Factura(models.Model):
    _name = 'upo_wood_app.factura'
    _description = 'Clase factura para UPOWOOD'

    idFactura = fields.Integer("Numero de factura", required=True)
    fecha = fields.Date('Fecha de la factura',required=True, autodate = True)
    #Añadir las relaciones entre clases

class Producto(models.Model):
    _name = 'upo_wood_app.producto'
    _description = 'Clase producto para UPOWOOD'

    idProducto = fields.Integer("Numero del producto", required=True)
    fechaFabricacion = fields.Date('Fecha de la fabricacion del producto',required=True)
    precio = fields.Integer("Precio del producto",required=True)
    #Añadir las relaciones entre clases

class Modelo(models.Model):
    _name = 'upo_wood_app.modelo'
    _description = 'Clase modelo para UPOWOOD'

    nombre = fields.Char(string="Nombre del modelo",required=True)
    descripcion = fields.Text("Descripcion del modelo en cuestion")
    stock = fields.Integer("Stock del modelo",required=True)
    foto = fields.Binary("FotoModelo")
    #Añadir las relaciones entre clases

class Material(models.Model):
    _name = 'upo_wood_app.material'
    _description = 'Clase material para UPOWOOD'

    idMaterial = fields.Integer("Numero del material", required=True)
    nombre = fields.Char(string="Nombre del material",required=True)
    descripcion = fields.Text("DDescripcion del material en cuestion")
    precio = fields.Integer("Precio del material",required=True)
    foto = fields.Binary("FotoMaterial")
    #Añadir las relaciones entre clases

 class Proveedor(models.Model):
    _name = 'upo_wood_app.proveedor'
    _description = 'Clase proveedor para UPOWOOD'

    nombre = fields.Char(string="Nombre del proveedor",required=True)
    direccion = fields.Text("Direccion del proveedor",required=True)
    cif =fields.Char(string="CIF del proveedor",required=True)
    telefono = fields.Integer("Numero de telefono")
    #Añadir las relaciones entre clases  