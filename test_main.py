"""
Test for the main page using fastapi.testclient.
"""
import os
import sys,requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
# Declaring test client
 
# Test for status code for get message
def test_get_message(startup_and_shutdown_server):
    "asserting status code"
    response = requests.get('http://127.0.0.1:8000/ews/v1/event/')
    assert response.status_code == 200
 
# Test for asserting random message is in the file
# def test_get_message_text():
    "asserting random message is in the file"
    # response = client.get("/ews/v1/event/")
    # message = response.json()
    # assert message