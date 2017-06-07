"""Get a list of Messages from the user's mailbox.
"""

from apiclient import errors


def ListMessagesMatchingQuery(service, user_id, query='',maxResults = 10):
  """List all Messages of the user's mailbox matching the query.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    query: String used to filter messages returned.
    Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

  Returns:
    List of Messages that match the criteria of the query. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate ID to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               maxResults = maxResults,
                                               q=query).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError, error:
    print 'An error occurred: %s' % error


def ListMessagesWithLabels(service, user_id, label_ids=[],maxResults = 10):
  """List all Messages of the user's mailbox with label_ids applied.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    label_ids: Only return Messages with these labelIds applied.

  Returns:
    List of Messages that have all required Labels applied. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate id to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               maxResults = maxResults,
                                               labelIds=label_ids,).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id,
                                                 labelIds=label_ids,
                                                 includeSpamTrash = True,
                                                 pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError, error:
    print 'An error occurred: %s' % error


def ListMessages(service, user_id = 'me', label_ids=[],maxResults = 10,pageToken = '',q = ''):
  '''
  Path parameters
  userId	string	The user's email address. The special value me can be used to indicate the authenticated user.
  Optional query parameters
  includeSpamTrash	boolean	Include messages from SPAM and TRASH in the results. (Default: false)
  labelIds	string	Only return messages with labels that match all of the specified label IDs.
  maxResults	unsigned integer	Maximum number of messages to return.
  pageToken	string	Page token to retrieve a specific page of results in the list.
  q	string	Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, "from:someuser@example.com rfc822msgid: is:unread". Parameter cannot be used when accessing the api using the gmail.metadata scope.
  '''
  try:
    response = service.users().messages().list(userId=user_id,
                                               labelIds=label_ids,
                                               maxResults = maxResults,
                                               pageToken = pageToken,
                                               q = q).execute()
    messages = []
    nextPageToken = ''
    if 'messages' in response:
      messages.extend(response['messages'])
    if 'nextPageToken' in response:
      nextPageToken = response['nextPageToken']
    return messages,nextPageToken
  except errors.HttpError, error:
    print 'An error occurred: %s' % error