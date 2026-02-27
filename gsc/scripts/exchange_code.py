#!/usr/bin/env python3
import argparse
from google_auth_oauthlib.flow import InstalledAppFlow

def main():
    client_id = "29882678687-kb7ljjvds7jps8q8k36i9gmg5i6glrge.apps.googleusercontent.com"
    client_secret = "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"
    code = "4/0AfrIepBJAf0m_dg8jO1ripPDS0rjMr043_KMEsxpn_vSJOMeXIoCwr9otSVHMDiqDwTkAw"
    
    client_config = {
        "web": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost:9090"]
        }
    }
    
    flow = InstalledAppFlow.from_client_config(client_config, scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
    flow.redirect_uri = "http://localhost:9090"
    
    flow.fetch_token(code=code)
    creds = flow.credentials
    
    print(f"GOOGLE_REFRESH_TOKEN={creds.refresh_token}")

if __name__ == "__main__":
    main()
