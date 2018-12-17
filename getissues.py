# This script shows how to connect to a JIRA instance with a
# username and password over HTTP BASIC authentication.

from collections import Counter
from jira import JIRA
import sys


pargs = sys.argv
if len(pargs) != 3:
    print("Please pass username and password as arguments: ex : python getissues.py uname pwd")
    exit(0)

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK.
# See
# https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK
# for details.
options = {
    'server': 'https://oropiri.atlassian.net'}
jira = JIRA(options, basic_auth=(pargs[1], pargs[2]))

# Get the mutable application properties for this server (requires
# jira-system-administrators permission)
props = jira.application_properties()

# Find all issues reported by the admin
issues = jira.search_issues('assignee=admin')

# Find the top three projects containing issues reported by admin
for issue in issues:
    print("{} : {}".format(issue, issue.fields.summary))
