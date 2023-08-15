import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Google Drive API scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

def create_shared_folder(folder_name):
    creds = None
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

  # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_authorized_user_info())

    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=creds)

    # Create a folder
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = drive_service.files().create(body=file_metadata,
                                          fields='id').execute()

    # Share the folder
    permission = {
        'type': 'anyone',
        'role': 'reader'
    }
    drive_service.permissions().create(fileId=folder['id'], body=permission).execute()

    print(f"Shared folder '{folder_name}' created with ID: {folder['id']}")

if __name__ == '__main__':
    folder_name = input("Enter the folder name: ")
    create_shared_folder(folder_name)
