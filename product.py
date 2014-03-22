# -*- encoding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (c) 2014 KIDDYS HOUSE SAC. (http://kiddyshouse.com).
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv, fields
from tools.translate import _
from datetime import datetime
import time

class product_product(osv.osv):
	_name= 'product.product'
	_inherit = 'product.product'
	_columns = {
		'descripcion_id': fields.one2many('product.descripcion','product_id',string="Descripciones"),
		'tela_id': fields.one2many('tela.descripcion','tela_id',string="TELAS"),
        }

product_product()

# class insumo_insumo(osv.osv):
	# _name= 'insumo.insumo'
	# _inherit = 'insumo.insumo'
	# _columns = {
		# 'insumo_id': fields.one2many('product.insumo',string="Insumo"),
        # }

# insumo_insumo()


class product_descripcion(osv.osv):
	_name = 'product.descripcion'
	_columns = {
		'product_id': fields.many2one('product.product',string="Producto"),
		'estilos_id': fields.many2one('otros.estilos','Estilos'),
		'name': fields.text('Descripcion prenda'),
		'fecha': fields.date('Fecha de llenado'),
		'sale_order_id': fields.one2many('sale.order.line','descripcion_sale',string='Lineas de Ventas'),
		'nombreprenda_id':fields.many2one('otros.nombres','Nombre de la Prenda'),
		'equipos_id':fields.many2one('otros.equipos','Equipo'),
		'nombrecompleto_id':fields.many2one('otros.nombrecompleto','Nombre Completo'),
		'nombrequipo_id':fields.many2one('otros.nombrequipo','Nombre Equipo'),

		
		
		#aunque ya no caben las colocare para pruebas posteriores
		
		'marquilla1_id':fields.many2one('otros.marquilla1','Marquilla1'),
		'marquilla2_id':fields.many2one('otros.marquilla2','Marquilla2'),
		'etiqueta1_id':fields.many2one('otros.etiqueta1','Etiqueta1'),
		'etiqueta2_id':fields.many2one('otros.etiqueta2','Etiqueta2'),
		
	}
	_defaults = {
		'fecha': lambda *a: time.strftime('%Y-%m-%d'),
		'name':'Camisilla',		
	}

product_descripcion()


class tela_descripcion(osv.osv):
	_name = 'tela.descripcion'
	_columns = {
		'tela_id':fields.many2one('otros.tela','Tela'),
		'tela1_id':fields.many2one('otros.tela1','Tela 1'),
		'color_id':fields.many2one('otros.colores','Color Tela 1 Frente'),
		'consumo_id':fields.many2one('otros.consumo','Consumo'),
		'tela2_id':fields.many2one('otros.tela2','Tela2'),
		'color2_id':fields.many2one('otros.colores2','Color Tela 2 COLOR ESPALDA / MANGAS'),
		'consumo2_id':fields.many2one('otros.consumo2','Consumo2'),
		'tela3_id':fields.many2one('otros.tela3','Tela3'),
		'color3_id':fields.many2one('otros.colores3','Color Tela 3 CIMBRA / SESGO'),
		'consumo3_id':fields.many2one('otros.consumo3','Consumo3'),

		
	}
	

tela_descripcion()

# class product_insumo(osv.osv):
	# _name = 'product.insumo'
	# _columns = {
		# 'fecha': fields.date('Fecha de llenado'),
		# 'marquilla1_id':fields.many2one('otros.marquilla1','Marquilla1'),

	# }
	# _defaults = {
		# 'fecha': lambda *a: time.strftime('%Y-%m-%d'),
	
	# }

# product_insumo()


# parte de insumos

class otros_tela(osv.osv):
  _name = 'otros.tela'
  _columns ={
 'name':fields.char('Tela',size=40),
 }
otros_tela()

class otros_marquilla1(osv.osv):
  _name = 'otros.marquilla1'
  _columns ={
 'name':fields.char('Marquilla1',size=40),
 }
otros_marquilla1()

class otros_marquilla2(osv.osv):
  _name = 'otros.marquilla2'
  _columns ={
 'name':fields.char('Marquilla2',size=40),
 }
otros_marquilla2()

class otros_etiqueta1(osv.osv):
  _name = 'otros.etiqueta1'
  _columns ={
 'name':fields.char('Etiqueta1',size=40),
 }
otros_etiqueta1()

class otros_etiqueta2(osv.osv):
  _name = 'otros.etiqueta2'
  _columns ={
 'name':fields.char('Etiqueta2',size=40),
 }
otros_etiqueta2()

# parte de atributos


class otros_estilos(osv.osv):
  _name = 'otros.estilos'
  _columns ={
 'name':fields.char('Estilos',size=40),
 }
otros_estilos()

class otros_nombres(osv.osv):
  _name = 'otros.nombres'
  _columns ={
 'name':fields.char('Nombres',size=40),
 }
otros_nombres()

class otros_equipos(osv.osv):
  _name = 'otros.equipos'
  _columns ={
 'name':fields.char('Equipos',size=40),
 }
otros_equipos()

class otros_nombrecompleto(osv.osv):
  _name = 'otros.nombrecompleto'
  _columns ={
 'name':fields.char('Nombrecompleto',size=40),
 }
otros_nombrecompleto()

class otros_nombrequipo(osv.osv):
  _name = 'otros.nombrequipo'
  _columns ={
 'name':fields.char('Nombrequipo',size=40),
 }
otros_nombrequipo()

class otros_tela1(osv.osv):
  _name = 'otros.tela1'
  _columns ={
 'name':fields.char('Tela1',size=40),
 }
otros_tela1()

class otros_colores(osv.osv):
  _name = 'otros.colores'
  _columns ={
 'name':fields.char('Color',size=40),
 }
otros_colores()

class otros_consumo(osv.osv):
  _name = 'otros.consumo'
  _columns ={
 'name':fields.char('Consumo',size=40),
 }
otros_consumo()

class otros_tela2(osv.osv):
  _name = 'otros.tela2'
  _columns ={
 'name':fields.char('Tela2',size=40),
 }
otros_tela2()

class otros_colores2(osv.osv):
  _name = 'otros.colores2'
  _columns ={
 'name':fields.char('Color2',size=40),
 }
otros_colores2()

class otros_consumo2(osv.osv):
  _name = 'otros.consumo2'
  _columns ={
 'name':fields.char('Consumo2',size=40),
 }
otros_consumo2()

class otros_tela3(osv.osv):
  _name = 'otros.tela3'
  _columns ={
 'name':fields.char('Tela3',size=40),
 }
otros_tela3()

class otros_colores3(osv.osv):
  _name = 'otros.colores3'
  _columns ={
 'name':fields.char('Color3',size=40),
 }
otros_colores3()


class otros_consumo3(osv.osv):
  _name = 'otros.consumo3'
  _columns ={
 'name':fields.char('Consumo3',size=40),
 }
otros_consumo3()


###Parte vieja


class sale_order(osv.osv):
	_name='sale.order'
	_inherit = 'sale.order'
	_columns = {
		'venta_corporativa': fields.boolean('Venta corporativa'),
	}

sale_order()


class sale_order_line(osv.osv):
	_name='sale.order.line'
	_inherit = 'sale.order.line'
	_columns = {
                'descripcion_sale': fields.many2one('product.descripcion', string="Descripciones"),
		'talla_xs': fields.integer('XS'),
		'talla_s': fields.integer('S'),
		'talla_m': fields.integer('M'),
                'talla_l': fields.integer('L'),
                'talla_xl': fields.integer('XL'),
				'talla_2xl': fields.integer('2XL'),

	}
	
	def descripcion_sale_change(self,cr,uid,ids,descripcion_sale,product_id,name='',context=None):
		res = {}
		if descripcion_sale:
			prod = self.pool.get('product.descripcion').name_get(cr,uid,descripcion_sale,context=context)[0][1]
			return {'value': {'name': prod}}
		return {}
	def onchange_total(self,cr,uid,ids,n1,n2,n3,n4,n5,n6,context={}):
		sum=0
		sum+=n1 or 0
		sum+=n2 or 0
		sum+=n3 or 0
		sum+=n4 or 0
		sum+=n5 or 0
		sum+=n6 or 0
		vals={'product_uom_qty':sum}
		return {'value':vals}
sale_order_line()

