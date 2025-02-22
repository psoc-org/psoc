import frappe


@frappe.whitelist(allow_guest=True)
def register_and_login(organization_name: str, organization_id: str, organization_email: str, password: str):
	try:
		organization_exists = frappe.db.exists("User", {"username": organization_id})
		if organization_exists:
			frappe.throw("Organization is already taken")
		organization_doc = frappe.get_doc(
			{
				"doctype": "User",
				"username": organization_id,
				"email": organization_email,
				"full_name": organization_name,
				"first_name": organization_name,
			}
		).insert(ignore_permissions=True)
		from frappe.utils.password import update_password

		update_password(organization_id, password)
		organization_doc.add_roles("Organization")
		login(organization_id, password)
	except Exception:
		frappe.throw("An exception occurred")
	login(organization_id, password)


@frappe.whitelist(allow_guest=True)
def login(organization_id: str, password: str):
	try:
		organization_exists = frappe.db.exists("User", {"username": organization_id})
		if not organization_exists:
			frappe.throw("Organization does not exist")

		from frappe.utils.password import check_password

		check_password(organization_id, password)
		organization = frappe.db.get_value("User", {"username": organization_id}, "name")

		from frappe.auth import LoginManager

		login_manager = LoginManager()
		login_manager.login_as(organization)

	except frappe.AuthenticationError:
		frappe.throw("Authentication error")


@frappe.whitelist()
def submit_details(
	tagline: str, about: str, domain: str, technologies: str, website_url: str, linkedin: str, github: str
):
	organization = frappe.session.user
	roles = frappe.get_roles(organization)
	allowed = False
	for role in roles:
		if role == "Organization":
			organization = frappe.db.get_value("User", {"username": organization}, "name")
			organization_details_doc = frappe.get_doc(
				{
					"doctype": "Organization",
					"organization": organization.get("name"),
					"tagline": tagline,
					"about": about,
					"domain": domain,
					"technologies": technologies,
					"website": website_url,
					"linkedin": linkedin,
					"github": github,
				}
			)
			organization_details_doc.insert()
			organization_details_doc.add_roles("Organization")
			allowed = True
	if not allowed:
		frappe.throw("Cannot submit details. Please login.")


@frappe.whitelist()
def submit_proposal():
	pass
