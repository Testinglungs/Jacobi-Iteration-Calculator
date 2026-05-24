"""Serverless function handler for Vercel deployment."""
import sys
import os

# Add the parent directory to the path so we can import the app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from app import app
except ImportError as e:
    print(f"[ERROR] Failed to import app: {e}")
    import traceback
    traceback.print_exc()
    raise

# Export the Flask app as the handler for Vercel
# Vercel will call this WSGI application for all requests
