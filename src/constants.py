import re

PHONE_REGEXP = re.compile(r"^\d{10}$")

EMAIL_REGEXP = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

DATE_REGEXP = re.compile(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$")