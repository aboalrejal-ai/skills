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
    
    client_config = {
        "web": {
            "client_id": args.client_id,
            "client_secret": args.client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "redirect_uris": ["http://localhost:9090"]
        }
    }
    
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    
    # Force redirect_uri to be localhost:9090 exactly as registered in Google
    flow.redirect_uri = "http://localhost:9090"
    
    auth_url, _ = flow.authorization_url(prompt="consent", access_type="offline")
    
    print("\n" + "="*60)
    print("1. Open this URL in your browser:")
    print(auth_url)
    print("="*60 + "\n")
    
    # Run the server on 0.0.0.0 so we can receive the callback, 
    # but Google will redirect to 'localhost' in your browser.
    creds = flow.run_local_server(
        host='0.0.0.0',
        port=9090, 
        open_browser=False
    )
    
    print("\n" + "="*60)
    print("SUCCESS! Add these to your .env file:")
    print(f"GOOGLE_CLIENT_ID={args.client_id}")
    print(f"GOOGLE_CLIENT_SECRET={args.client_secret}")
    print(f"GOOGLE_REFRESH_TOKEN={creds.refresh_token}")
    print("="*60)

if __name__ == "__main__":
    main()
