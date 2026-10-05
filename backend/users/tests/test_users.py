import pytest
from rest_framework.test import APIClient
from users.models import User
from department.models import Department

@pytest.mark.django_db
def test_admin_can_list_all_Employees():
    admin = User.objects.create_user(
        username="admin",
        email="admin@example.com",
        password="password123",
        role=User.Role.ADMIN,
    )

    User.objects.create_user(
        username="employee1",
        email="employee1@example.com",
        password="password123",
        role=User.Role.EMPLOYEE,
    )

    User.objects.create_user(
        username="employee2",
        email="employee2@example.com",
        password="password123",
        role=User.Role.EMPLOYEE,
    )

    client = APIClient()

    client.post(
        '/api/auth/login/',
        {
            'email':'admin@example.com',
            'password':'password123'
        }
    )

    response = client.get('/api/users/')

    assert response.status_code == 200
    assert len(response.data) == 3