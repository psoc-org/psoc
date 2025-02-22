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
		domain: DF.Data | None
		github: DF.Data | None
		linkedin: DF.Data | None
		organization: DF.Link
		tagline: DF.Data | None
		technologies: DF.Data | None
		website: DF.Data | None
	# end: auto-generated types
