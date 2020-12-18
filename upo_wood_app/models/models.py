# -*- coding: utf-8 -*-
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


class Albaran(models.Model):
    _name = 'upo_wood_app.albaran'
    _description = 'Clase albaran para UPOWOOD'

    name = fields.Integer("Numero de albaras", required=True) #Atributo creado para que odoo ponga Albaran / numero , pero este atributo no esta en el uml
    isEntregado = fields.Boolean("Se ha realizado el envio correctamente?",required=True)
    fechaLlegada = fields.Date('Fecha de llegada prevista',required=True)
    descripcion = fields.Text("Descripcion de la llegada y, en caso de problemas, motivo de no haber realizado la entrega")
    #Añadir las relaciones entre clases
    envio_id = fields.Many2one("upo_wood_app.venta",string="Envio relacionado con el albaran")
    _sql_constraints = [('albaran_name_unique','UNIQUE (name)','El número del albarán debe ser único')]

class Persona(models.Model):
    _name = 'upo_wood_app.persona'
    _description = 'Clase persona para UPOWOOD'

    nombre = fields.Char(string="Nombre del usuario",required=True, help = "Nombre del usuario en el sistema")
    password = fields.Char(string="Contraseña",required=True)
    direccion = fields.Text("Direccion del usuario",required=True)
    name =fields.Char(string="DNI o CIF del usuario",required=True)
    email = fields.Char(string="email del usuario",required=True)
    telefono = fields.Integer("Numero de telefono")
    foto = fields.Binary("Foto usuario")
    isEmpleado = fields.Selection([('empleado','Empleado'),('cliente','Cliente')],"El usuario es empleado o cliente?",required=True)
    #Añadir las relaciones entre clases
    venta_ids = fields.Many2many("upo_wood_app.venta",string="Ventas asociadas a la persona")
    _sql_constraints = [('persona_name_unique','UNIQUE (name)','El dni de la persona ya está registrado')]

class Factura(models.Model):
    _name = 'upo_wood_app.factura'
    _description = 'Clase factura para UPOWOOD'

    name = fields.Integer("Numero de factura", required=True)
    fecha = fields.Date('Fecha de la factura',required=True, autodate = True)
    #Añadir las relaciones entre clases
    venta_id = fields.Many2one("upo_wood_app.venta",string="Venta asociada a la factura") 
    _sql_constraints = [('factura_name_unique','UNIQUE (name)','El número de la factura debe ser único')]   

class Producto(models.Model):
    _name = 'upo_wood_app.producto'
    _description = 'Clase producto para UPOWOOD'

    name = fields.Char(string="Nombre del producto", required=True)
    fechaFabricacion = fields.Date("Fecha de la fabricacion del producto",required=True)
    precio = fields.Integer("Precio del producto",required=True)
    stock = fields.Integer("Stock del producto",required=True)
    foto = fields.Binary("FotoProducto")
    #Añadir las relaciones entre clases
    venta_ids = fields.Many2many("upo_wood_app.venta",string="Venta asociados al producto") 
    categoria_id = fields.Many2one("upo_wood_app.categoria",string="Categoria asociada al producto")
    material_id = fields.Many2one("upo_wood_app.material",string="Material asociado al producto")
    _sql_constraints = [('producto_name_unique','UNIQUE (name)','Ya existe un producto con ese nombre')]

class Categoria(models.Model):
    _name = 'upo_wood_app.categoria'
    _description = 'Clase categoria para UPOWOOD'

    name = fields.Char(string="Nombre de la categoria",required=True)
    descripcion = fields.Text("Descripcion de la categoria en cuestion")
    #Añadir las relaciones entre clases
    producto_id = fields.One2many("upo_wood_app.producto","categoria_id","Producto relacionado con la categoria")
    _sql_constraints = [('categoria_name_unique','UNIQUE (name)','Ya existe una categoría con ese nombre')]

class Material(models.Model):
    _name = 'upo_wood_app.material'
    _description = 'Clase material para UPOWOOD'

    idMaterial = fields.Integer("Numero del material", required=True)
    name = fields.Char(string="Nombre del material",required=True)
    descripcion = fields.Text("Descripcion del material en cuestion")
    precio = fields.Integer("Precio del material",required=True)
    foto = fields.Binary("FotoMaterial")
    #Añadir las relaciones entre clases
    producto_id = fields.One2many("upo_wood_app.producto","material_id","Producto relacionado con el material")
    proveedor_ids = fields.Many2many("upo_wood_app.proveedor",string="Proveedor relacionado con el material")
    _sql_constraints = [('material_idmaterial_unique','UNIQUE (idMaterial)','El idMaterial del material debe ser único')]

class Proveedor(models.Model):
    _name = 'upo_wood_app.proveedor'
    _description = 'Clase proveedor para UPOWOOD'

    name = fields.Char(string="Nombre del proveedor",required=True)
    direccion = fields.Text("Direccion del proveedor",required=True)
    cif = fields.Char(string="CIF del proveedor",required=True)
    telefono = fields.Integer("Numero de telefono")
    #Añadir las relaciones entre clases  
    material_ids = fields.Many2many("upo_wood_app.material",string="Materiales relacionados con proveedor") 

    _sql_constraints = [('proveedor_cif_unique','UNIQUE (cif)','El cif del proveedor debe ser único')]