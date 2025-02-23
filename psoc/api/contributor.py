import logging

import frappe


@frappe.whitelist(allow_guest=True)
def register_and_login(first_name: str, last_name: str | None, username: str, email: str, password: str):
	try:
		contributor_exists = frappe.db.exists("User", {"username": username})
		if contributor_exists:
			frappe.throw("Username is already taken")
		full_name = f"{first_name} {last_name}"
		contributor_doc = frappe.get_doc(
			{
				"doctype": "User",
				"username": username,
				"email": email,
				"first_name": first_name,
				"last_name": last_name,
				"full_name": full_name,
			}
		).insert(ignore_permissions=True)
		from frappe.utils.password import update_password

		update_password(username, password)
		contributor_doc.add_roles("Contributor")
		login(username, password)
	except Exception:
		frappe.throw("An exception occurred")


@frappe.whitelist(allow_guest=True)
def login(username: str, password: str):
	try:
		user_exists = frappe.db.exists("User", {"username": username})
		if not user_exists:
			frappe.throw("User does not exist")

		from frappe.utils.password import check_password

		check_password(username, password)
		user = frappe.db.get_value("User", {"username": username}, "name")

		from frappe.auth import LoginManager

		login_manager = LoginManager()
		login_manager.login_as(user)

	except frappe.AuthenticationError:
		frappe.throw("Authentication error")


@frappe.whitelist(allow_guest=True)
def get_contributor_profile(contributor_id: str):
	try:
		# Fetch a specific contributor profile based on ID
		contributor = frappe.get_all(
			"Contributor",
			filters={"name": contributor_id},
			fields=["about", "contributor", "linkedin", "github", "resume"],
			ignore_permissions=False,
		)

		if not contributor:
			return {"status": "error", "message": "Contributor not found"}

		return {"status": "success", "data": contributor}

	except Exception as e:
		frappe.log_error(frappe.get_traceback(), "Error while fetching contributor information")
		return {"status": "error", "message": str(e)}


logging.basicConfig()

# organization_id: str, project_id: str, description: str, reason: str


@frappe.whitelist(allow_guest=True)
def get_all_proposals_for_user():
	user = frappe.session.user
	try:
		# Fetch proposals associated with the user
		contributor_data = frappe.db.get(
			"Contributor",
			filters={"user", user},
			fields=[
				"name",
			],
			ignore_permissions=True,
		)

		if contributor_data:
			proposals = frappe.get_all(
				"Contributor Proposal",
				filters={"contributor": contributor_data.get("name")},
				fields=["name", "project", "status", "reason", "description", "organization"],
				ignore_permissions=True,
			)
			if not proposals:
				return {"status": "error", "message": "No proposals found for the user"}

			total_proposals = []
			for proposal in proposals:
				proposal_id = proposal.get("name")
				organization_data = frappe.db.get(
					"Organization",
					filters={"organization", proposal.get("organization")},
					fields=["name", "organization"],
					ignore_permissions=True,
				)
				organization_id = organization_data.get("organization")
				organization_details = frappe.db.get(
					"User",
					filters={"email", organization_id},
					fields=["full_name as organization_name", "username as organization_slug"],
					ignore_permissions=True,
				)

				project_data = frappe.db.get(
					"Project",
					filters={"name", proposal.get("project")},
					fields=["name as project_id", "project_name", "description"],
					ignore_permissions=True,
				)

				proposal_doc = {
					"proposal_id": proposal_id,
					"organization": {
						"org_id": organization_id,
						"name": organization_details.get("organization_name"),
						"slug": organization_details.get("organization_slug"),
					},
					"project": project_data,
					"status": proposal.get("status"),
					"reason": proposal.get("reason"),
					"description": proposal.get("description"),
				}
				total_proposals.append(proposal_doc)

			return {"status": "success", "data": total_proposals}
		else:
			return {"status": "failure", "data": [], "message": "No contributor found"}

	except Exception as e:
		frappe.log_error(frappe.get_traceback(), "get_all_proposal Error")
		return {"status": "error", "message": str(e)}


@frappe.whitelist()
def submit_details(
	about: str,
	domain: str,
	technologies: str,
	website_url: str,
	linkedin: str,
	github: str,
):
	contributor = frappe.session.user
	roles = frappe.get_roles(contributor)

	logging.info(contributor, "contributor")
	logging.info(roles, "roles")

	contributor_details_doc = frappe.get_doc(
		{
			"doctype": "Contributor",
			"contributor": contributor,
			"about": about,
			"domain": domain,
			"technologies": technologies,
			"website": website_url,
			"linkedin": linkedin,
			"github": github,
		}
	)
	contributor_details_doc.insert(ignore_permissions=True)
	contributor_details_doc.add_roles("Contributor")

	user_permission = frappe.new_doc("User Permission")
	user_permission.user = contributor
	user_permission.allow = "Contributor"
	user_permission.for_value = contributor_details_doc

	# Save the document
	user_permission.insert(ignore_permissions=True)
	frappe.db.commit()

	# roles = frappe.get_roles(contributor)
	# allowed = False
	# for role in roles:
	# 	if role == "Contributor":
	"""
	allowed = True
	if not allowed:
		frappe.throw("Cannot submit details. Please login.")
	"""


@frappe.whitelist()
def submit_proposal():
	pass
