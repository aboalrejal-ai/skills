#!/usr/bin/env python3
import argparse
import os
import sys
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client-id")
    parser.add_argument("--client-secret")
    args = parser.parse_args()
    
    client_id = args.client_id or os.environ.get("GOOGLE_CLIENT_ID")
    client_secret = args.client_secret or os.environ.get("GOOGLE_CLIENT_SECRET")
    
    if not client_id or client_secret is None:
        print("ERROR: Need client_id and client_secret.")
        sys.exit(1)
    
    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
        }
    }
    
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    flow.redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
    
    auth_url, _ = flow.authorization_url(prompt="consent")
    
    print("\n" + "="*60)
    print("1. Open this URL in your browser:")
    print(auth_url)
    print("="*60 + "\n")
    
    code = input("2. Enter the authorization code: ").strip()
    
    flow.fetch_token(code=code)
    creds = flow.credentials
    
    print("\n" + "="*60)
    print("SUCCESS! Add these to your .env file:")
    print(f"GOOGLE_CLIENT_ID={client_id}")
    print(f"GOOGLE_CLIENT_SECRET={client_secret}")
    print(f"GOOGLE_REFRESH_TOKEN={creds.refresh_token}")
    print("="*60)

if __name__ == "__main__":
    main()
