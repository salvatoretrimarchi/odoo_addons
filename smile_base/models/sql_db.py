# -*- coding: utf-8 -*-
# (C) 2010 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import traceback

from odoo.sql_db import Cursor, _logger

native_execute = Cursor.execute


@Cursor.check
def execute(self, query, params=None, log_exceptions=None):
    try:
        return native_execute(self, query, params, log_exceptions)
    except Exception:
        _logger.error('Traceback (most recent call last):\n' + ''.join(
            traceback.format_stack()))
        raise


Cursor.execute = execute
