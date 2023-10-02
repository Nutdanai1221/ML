import unittest
from flask import Flask
import sys
import os
import requests
import pytest

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from app import app  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_homepage_response(client):
    response = client.get('/')
    assert response.status_code == 200  # Check if the homepage responds with a 200 status code
    print("Homepage Test Passed")  # Print a message indicating the test passed


def test_receive_data_post_response(client):
    data = {
        'engine': '1248',
        'maxpower': '83.14',
        'year': '2016'
    }
    response = client.post('/receive_data', data=data)
    assert response.status_code == 200  # Check if the post request to receive_data responds with a 200 status code
    print("Receive Data Test Passed")  # Print a message indicating the test passed

if __name__ == '__main__':
    pytest.main()