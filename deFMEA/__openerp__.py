# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'FMEA Failure Mode Effect Analysis',
    'version': '0.1',
    'category': 'Engineering',
    'description': """
This module installs the base for FMEA (Failure Mode Effect Analysis) 
======================================================================================================================

The ability to extract to design systems and components according functional abilities.
    """,
    'author': 'diethelm engineering',
    'website': 'www.diethelm-engineering.ch',
    'depends': ['base'],
    'data': ['defmea_data.xml' , 'defmea_view.xml'],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
