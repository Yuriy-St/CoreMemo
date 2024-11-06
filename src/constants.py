import re

PHONE_REGEXP = re.compile(r"^\d{10}$")

EMAIL_REGEXP = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")