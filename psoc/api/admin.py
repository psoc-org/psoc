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
		contributor_doc.add_roles("SoC Admin")
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
def get_organization_proposal(organization_proposal_id: str):
	try:
		organization_proposal = frappe.db.get(
			"Organization Proposal",
			filter={"name": organization_proposal_id},
			fields=[
				"name as id",
				"organization",
				"reason",
				"projects",
				"mentoring_plan",
				"support_from_soc",
				"status",
			],
			ignore_permissions=True,
		)
		if organization_proposal:
			organization = frappe.db.get(
				"Organization",
				filters={"name": organization_proposal.get("name")},
				fields=[
					"name as id",
					"organization",
					"tagline",
					"about",
					"domain",
					"technologies",
					"website",
					"linkedin",
					"github",
				],
				ignore_permissions=True,
			)
			data = {"proposal": organization_proposal, "organization": organization}
			return {"status": "success", "data": data}
		else:
			return {"status": "failure", "data": [], "message": "No contributor found"}

	except Exception as e:
		frappe.log_error(frappe.get_traceback(), "get_all_proposal Error")
		return {"status": "error", "message": str(e)}


@frappe.whitelist(allow_guest=True)
def get_organization_proposals():
	try:
		organization_proposals = frappe.get_all(
			"Organization Proposal",
			filter={"status": "Pending"},
			fields=[
				"name as id",
				"organization",
				"reason",
				"projects",
				"mentoring_plan",
				"support_from_soc",
				"status",
			],
			ignore_permissions=True,
		)

		organization_proposals_list = []
		for organization_proposal in organization_proposals:
			organization = frappe.db.get(
				"Organization",
				filters={"name": organization_proposal.get("organization")},
				fields=[
					"name",
					"project",
					"organization",
					"tagline",
					"about",
					"domain",
					"technologies",
					"website",
					"linkedin",
				],
				ignore_permissions=True,
				as_dict=True,
			)

			organization_user = frappe.db.get(
				"User",
				filters={"email": organization.get("organization")},
				fields=["name", "full_name as organization_name", "username as organization_slug"],
				ignore_permissions=True,
			)
			proposal_doc = {
				"proposal_id": organization_proposal.get("id"),
				"organization": {
					"org_id": organization_proposal.get("name"),
					"name": organization_user.get("organization_name"),
					"slug": organization_user.get("organization_slug"),
				},
				"status": organization_proposal.get("status"),
			}
			organization_proposals_list.append(proposal_doc)

			return {"status": "success", "data": organization_proposals_list}
		else:
			return {"status": "failure", "data": [], "message": "No contributor found"}

	except Exception as e:
		frappe.log_error(frappe.get_traceback(), "get_all_proposal Error")
		return {"status": "error", "message": str(e)}


@frappe.whitelist(allow_guest=True)
def approve_organization_proposal(proposal_id: str):
	organization_proposal = frappe.get_doc("Organization Proposal", proposal_id, for_update=True)
	organization_proposal.status = "Approved"
	organization_proposal.save(ignore_permissions=True)


@frappe.whitelist(allow_guest=True)
def reject_organization_proposal(proposal_id: str):
	organization_proposal = frappe.get_doc("Organization Proposal", proposal_id, for_update=True)
	organization_proposal.status = "Rejected"
	organization_proposal.save(ignore_permissions=True)
