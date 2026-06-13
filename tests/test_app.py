import sys
import os

sys.path.insert(0, os.path.abspath("."))

from src.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 404

def test_sobre():
    client = app.test_client()
    response = client.get("/sobre")
    assert response.status_code == 200