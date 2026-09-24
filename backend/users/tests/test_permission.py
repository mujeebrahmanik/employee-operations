import pytest
from rest_framework.test import APIRequestFactory,APIClient
from users.models import User
from users.permissions import IsAdmin,IsManager,IsEmployee,IsAdminOrManager

@pytest.mark.django_db
def test_admin_has_permission():
    user = User.objects.create_user(
        username='admin',
        email='admin@example.com',
        password='password123',
        role=User.Role.ADMIN,
    )

    factory = APIRequestFactory()
    request = factory.get('/')

    request.user= user
    permission = IsAdmin()

    assert permission.has_permission(request,None) is True



@pytest.mark.django_db
@pytest.mark.parametrize(
    'role',
    [
        User.Role.MANAGER,
        User.Role.EMPLOYEE,
    ],
)
def test_non_admin_has_no_permission(role):
    user = User.objects.create_user(
        username='admin',
        email='admin@example.com',
        password='password123',
        role=role
    )

    factory = APIRequestFactory()
    request = factory.get('/')

    request.user= user
    permission = IsAdmin()

    assert permission.has_permission(request,None) is False


@pytest.mark.django_db
def test_manager_has_permission():
    user = User.objects.create_user(
        username='manager',
        email='manager@example.com',
        password='password123',
        role=User.Role.MANAGER
    )

    factory = APIRequestFactory()
    request = factory.get('/')

    request.user = user
    permission = IsManager()

    assert permission.has_permission(request,None) is True


@pytest.mark.django_db
def test_employee_has_no_manager_permission():
    user = User.objects.create_user(
        username='employee',
        email='employee@example.com',
        password='password123',
        role=User.Role.EMPLOYEE
    )

    factory = APIRequestFactory()
    request = factory.get('/')

    request.user = user
    permission = IsManager()

    assert permission.has_permission(request,None) is False

@pytest.mark.django_db
def test_employee_has_permission():
    user = User.objects.create_user(
        username='employee',
        email='employee@example.com',
        password='password123',
        role=User.Role.EMPLOYEE
    )

    factory = APIRequestFactory()
    request = factory.get('/')

    request.user = user
    permission = IsEmployee()

    assert permission.has_permission(request,None) is True


@pytest.mark.django_db
def test_manager_has_no_employee_permission():
    user = User.objects.create_user(
        username='manager',
        email='manager@example.com',
        password='password123',
        role=User.Role.MANAGER
    )

    factory = APIRequestFactory()
    request = factory.get('/')

    request.user = user
    permission = IsEmployee()

    assert permission.has_permission(request,None) is False


@pytest.mark.django_db
@pytest.mark.parametrize(
    'role',
    [
        User.Role.MANAGER,
        User.Role.ADMIN,
    ],
)
def test_admin_or_manager_has_permission(role):
    user = User.objects.create_user(
        username='user',
        email='user@example.com',
        password='password123',
        role=role
    )

    factory = APIRequestFactory()
    request = factory.get('/')

    request.user= user
    permission = IsAdminOrManager()

    assert permission.has_permission(request,None) is True

@pytest.mark.django_db
def test_employee_has_no_admin_or_manager_permission():
    user = User.objects.create_user(
        username="employee",
        email="employee@example.com",
        password="password123",
        role=User.Role.EMPLOYEE,
    )

    factory = APIRequestFactory()
    request = factory.get("/")

    request.user = user

    permission = IsAdminOrManager()

    assert permission.has_permission(request, None) is False



@pytest.mark.django_db
def test_admin_can_access_admin_endpoint():
    user = User.objects.create_user(
        username="admin",
        email="admin@example.com",
        password="password123",
        role=User.Role.ADMIN,
    )

    client = APIClient()

    login_response = client.post(
        '/api/auth/login/',
        {
            "email":"admin@example.com",
            "password":"password123",
        }
    )

    assert login_response.status_code == 200
    response = client.get('/api/auth/admin-test/')

    assert response.status_code == 200
    assert response.data['message'] == 'you have admin access'


@pytest.mark.django_db
def test_manager_cannot_access_admin_endpoint():
    user = User.objects.create_user(
        username="manager",
        email="manager@example.com",
        password="password123",
        role=User.Role.MANAGER,
    )

    client = APIClient()

    login_response = client.post(
        '/api/auth/login/',
        {
            "email":"manager@example.com",
            "password":"password123",
        }
    )

    assert login_response.status_code == 200
    response = client.get('/api/auth/admin-test/')

    assert response.status_code == 403


@pytest.mark.django_db
def test_employee_cannot_access_admin_endpoint():
    User.objects.create_user(
        username="employee",
        email="employee@example.com",
        password="password123",
        role=User.Role.EMPLOYEE,
    )

    client = APIClient()

    login_response = client.post(
        '/api/auth/login/',
        {
            "email":"employee@example.com",
            "password":"password123",
        }
    )

    assert login_response.status_code == 200
    response = client.get('/api/auth/admin-test/')

    assert response.status_code == 403