"""Get Draft with specified Draft ID.
"""

from apiclient import errors


def GetDraft(service, user_id, draft_id):
  """Get Draft with ID matching draft_id.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    draft_id: The ID of the Draft to return.

  Returns:
    Draft with ID matching draft_id.
  """
  try:
    draft = service.users().drafts().get(user_id=user_id, id=draft_id).execute()

    print 'Draft id: %s\nDraft message: %s' % (draft['id'], draft['message'])

    return draft
  except errors.HttpError, error:
    print 'An error occurred: %s' % error