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


@pytest.mark.django_db
def test_manager_can_only_see_their_team():
    manager_a = User.objects.create_user(
        username="manager_a",
        email="manager_a@example.com",
        password="password123",
        role=User.Role.MANAGER,
    )

    manager_b = User.objects.create_user(
        username="manager_b",
        email="manager_b@example.com",
        password="password123",
        role=User.Role.MANAGER,
    )

    employee_a1=User.objects.create_user(
        username="employeea1",
        email="employeea1@example.com",
        password="password123",
        role=User.Role.EMPLOYEE,
        manager=manager_a
    )

    employee_a2=User.objects.create_user(
        username="employeea2",
        email="employeea2@example.com",
        password="password123",
        role=User.Role.EMPLOYEE,
        manager=manager_a
    )

    employee_b=User.objects.create_user(
        username="employee2",
        email="employee2@example.com",
        password="password123",
        role=User.Role.EMPLOYEE,
        manager=manager_b
    )

    client = APIClient()

    client.post(
        '/api/auth/login/',
        {
            'email':'manager_a@example.com',
            'password':'password123'
        }
    )

    response = client.get('/api/users/')

    assert response.status_code == 200
    assert len(response.data) == 2

    employee_ids = {
        employee['id']
        for employee in response.data
    }

    assert employee_a1.id in employee_ids
    assert employee_a2.id in employee_ids

