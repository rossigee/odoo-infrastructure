# -*- coding: utf-8 -*-

from odoo import models, fields, api


class User(models.Model):
    _inherit = 'res.users'

    posix_uid = fields.Integer(string="POSIX user ID")
    posix_gid = fields.Integer(string="POSIX primary group ID")
    password_sha256 = fields.Text(string="SHA256 encoded password")
    ssh_pubkey = fields.Text(string="SSH keys")
