import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, user4@exclude.net"

#original
#emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

#modified to exclude emails at exclude.com
pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
emails = pattern.findall(text)

print(emails)