"""Get a list of Drafts from the user's mailbox.
"""

from apiclient import errors


def ListDrafts(service, user_id):
  """Get a list of all drafts in the user's mailbox.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.

  Returns:
    A list of all Drafts in the user's mailbox.
  """
  try:
    response = service.users().drafts().list(userId=user_id).execute()
    drafts = response['drafts']
    for draft in drafts:
      print 'Draft id: %s' % draft['id']
    return drafts
  except errors.HttpError, error:
    print 'An error occurred: %s' % error