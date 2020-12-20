# -*- coding: utf-8 -*-
from odoo import models, fields, api

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