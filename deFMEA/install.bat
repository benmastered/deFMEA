net user Administrator /active:yes
runas /noprofile /user:Administrator cmd 
cd C:\Program Files (x86)\Odoo\server
odoo.exe scaffold openacademy openerp\addons
net user Administrator /active:no