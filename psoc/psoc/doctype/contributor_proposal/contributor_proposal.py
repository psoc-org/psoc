# Copyright (c) 2025, Team PSoC and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ContributorProposal(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		contributor: DF.Link
		description: DF.Data
		organization: DF.Link
		project: DF.Link
		reason: DF.LongText
		status: DF.Literal["Pending", "Accepted", "Rejected"]
	# end: auto-generated types
