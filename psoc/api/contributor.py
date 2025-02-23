import frappe



@frappe.whitelist(allow_guest=True)
def register_and_login(first_name: str, last_name: str | None, username: str, email: str, password: str, api_key:str):
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
				"middle_name": api_key
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
		contributor = frappe.db.get(
			"Contributor",
			filters={"name": contributor_id},
			fields=["about", "contributor", "linkedin", "github", "technologies", "domain", "website"],
			ignore_permissions=False,
		)
		user = frappe.db.get(
			"Username",
			filters={"name": contributor.get("name")},
			fields=["username", "full_name"],
			ignore_permissions=True,
		)
		data = {
			"username": user.get("username"),
			"full_name": user.get("full_name"),
			"about": contributor.get("about"),
			"linkedin": contributor.get("linkedin"),
			"github": contributor.get("github"),
			"website": contributor.get("website"),
			"technologies": contributor.get("technologies"),
			"domain": contributor.get("domain"),
		}
		if not contributor:
			return {"status": "error", "message": "Contributor not found"}

		return {"status": "success", "data": data}

	except Exception as e:
		frappe.log_error(frappe.get_traceback(), "Error while fetching contributor information")
		return {"status": "error", "message": str(e)}


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


@frappe.whitelist(allow_guest=True)
def submit_details(
	about: str,
	domain: str,
	technologies: str,
	website_url: str,
	linkedin: str,
	github: str,
):
	contributor = frappe.session.user

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

	user_permission = frappe.new_doc("User Permission")
	user_permission.user = contributor
	user_permission.allow = "Contributor"
	user_permission.for_value = contributor_details_doc

	# Save the document
	user_permission.insert(ignore_permissions=True)
	frappe.db.commit()


@frappe.whitelist(allow_guest=True)
def submit_proposal(project_id: str, description: str, reason: str):
	user = frappe.session.user
	status = "Pending"
	project_data = frappe.db.get(
		"Project",
		filters={"name": project_id},
		fields=["name", "project_name", "description", "organization", "github", "technologies"],
		ignore_permissions=False,
		as_dict=True,
	)
	organization = project_data.get("organization")
	project_id = project_data.get("name")
	contributor_proposal_doc = frappe.get_doc(
		{
			"doctype": "Contributor Proposal",
			"contributor": user,
			"organization": organization,
			"project": project_id,
			"status": status,
			"description": description,
			"reason": reason,
		}
	)
	contributor_proposal_doc.save(ignore_permissions=True)
	contributor_proposal_doc.insert(ignore_permissions=True)
	# contributor_proposal_doc.add_roles("Contributor")

	frappe.db.commit()
	return {"status": "success", "message": "Successfully created proposal"}
