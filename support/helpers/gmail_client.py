import os
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GmailClient:
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    TOKEN_PATH = 'token.json'
    CREDENTIALS_PATH = 'credentials.json'

    def __init__(self):
        self.creds = self._authenticate()

    def _authenticate(self):
        creds = None

        if os.path.exists(self.TOKEN_PATH):
            creds = Credentials.from_authorized_user_file(self.TOKEN_PATH, self.SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.CREDENTIALS_PATH, self.SCOPES)
                creds = flow.run_local_server(port=0)

            with open(self.TOKEN_PATH, 'w') as token_file:
                token_file.write(creds.to_json())

        return creds

    def _build_service(self):
        return build('gmail', 'v1', credentials=self.creds)

    def get_last_message(self, user_id='me'):
        try:
            service = self._build_service()
            messages = service.users().messages().list(userId=user_id, maxResults=1).execute().get('messages', [])

            if not messages:
                print("No messages found.")
                return None

            message_id = messages[0]['id']
            return service.users().messages().get(userId=user_id, id=message_id).execute()

        except HttpError as error:
            print(f"Gmail API error: {error}")
            return None

    def check_email_received(self, expected_sender, expected_subject, timeout_seconds=60):
        start_time = time.time()

        while time.time() - start_time < timeout_seconds:
            message = self.get_last_message()

            if message:
                headers = {h['name']: h['value'] for h in message.get('payload', {}).get('headers', [])}
                subject = headers.get('Subject')
                sender = headers.get('From')

                if subject == expected_subject and sender == f"<{expected_sender}>":
                    print("Email received.")
                    return

            time.sleep(1)

        raise TimeoutError(
            f"Email from <{expected_sender}> with subject '{expected_subject}' not received within {timeout_seconds} seconds.")
