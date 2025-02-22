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
		)
		if not contributor:
			return {"status": "error", "message": "Contributor not found"}

		return {"status": "success", "data": contributor}
	except Exception as e:
		frappe.log_error(frappe.get_traceback(), "get_contributor_profile Error")
		return {"status": "error", "message": str(e)}


@frappe.whitelist()
def submit_details(about: str, domain: str, technologies: str, website_url: str, linkedin: str, github: str):
	contributor = frappe.session.user
	roles = frappe.get_roles(contributor)
	allowed = False
	for role in roles:
		if role == "Contributor":
			contributor = frappe.db.get_value("User", {"username": contributor}, "name")
			contributor_details_doc = frappe.get_doc(
				{
					"doctype": "Contributor",
					"contributor": contributor.get("name"),
					"about": about,
					"domain": domain,
					"technologies": technologies,
					"website": website_url,
					"linkedin": linkedin,
					"github": github,
				}
			)
			contributor_details_doc.insert()
			contributor_details_doc.add_roles("Contributor")
			allowed = True
	if not allowed:
		frappe.throw("Cannot submit details. Please login.")


@frappe.whitelist()
def submit_proposal():
	pass
