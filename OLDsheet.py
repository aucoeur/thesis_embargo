from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow, 
from google.auth.transport.requests import Request
from dotenv import load_dotenv
import json

load_dotenv()


if __name__ == "__main__":
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    API_KEY = os.getenv("API_KEY")
    SHEET_ID = os.getenv("SPREADSHEET_ID")

    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',
        SCOPES,
    )

    creds = flow.run_local_server(port=0)

    # Construct resource for interacting with API
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=100).execute()

    values = result.get("values", [])

