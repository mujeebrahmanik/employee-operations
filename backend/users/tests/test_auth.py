import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.mark.django_db
def test_login_success():
    user = User.objects.create_user(
        username = 'testuser',
        email = 'test@example.com',
        password = 'testpassword123'
    )

    client = APIClient()

    response = client.post(
        '/api/auth/login/',{
            'email':'test@example.com',
            'password':'testpassword123'
        },
    )

    assert response.status_code == 200
    assert response.data['user']['email'] == user.email

    assert 'access_token' in response.cookies
    assert 'refresh_token' in response.cookies 


@pytest.mark.django_db
def test_with_wrong_password():
    User.objects.create_user(
        username = 'testuser',
        email = 'test@example.com',
        password = 'testpassword123'
    )

    client = APIClient()

    response = client.post(
        '/api/auth/login/',
        {
            'email':'test@example.com',
            'password':'wrongpassword'
        },
    )

    assert response.status_code == 400