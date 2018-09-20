# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ni_dark_theme"
app_title = "Ni Dark Theme"
app_publisher = "Randy Lowery"
app_description = "Custom Theme for Frappe"
app_icon = "octicon octicon-file-directory"
app_color = "black"
app_email = "lowerymayorga@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/ni_dark_theme/css/ni.dark.theme.css"

# app_include_js = "/assets/ni_dark_theme/js/ni_dark_theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/ni_dark_theme/css/ni_dark_theme.css"
# web_include_js = "/assets/ni_dark_theme/js/ni_dark_theme.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ni_dark_theme.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ni_dark_theme.install.before_install"
# after_install = "ni_dark_theme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ni_dark_theme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ni_dark_theme.tasks.all"
# 	],
# 	"daily": [
# 		"ni_dark_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"ni_dark_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ni_dark_theme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ni_dark_theme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ni_dark_theme.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ni_dark_theme.event.get_events"
# }

