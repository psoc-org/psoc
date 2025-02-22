# Copyright (c) 2025, Team PSoC and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Organization(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		about: DF.Data | None
		org_id: DF.Link
		tagline: DF.Data | None
	# end: auto-generated types
