import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from django.urls import reverse

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def course(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return course


@pytest.mark.django_db
def test_course(client, course_factory):
    courses = course_factory(_quantity=3)
    URL = reverse('courses-detail', args=[courses[0].id])
    response = client.get(URL)
    assert response.status_code == 200
    assert response.data['id'] == courses[0].id


@pytest.mark.django_db
def test_course_list(client, course_factory):
    course = course_factory(_quantity=5)
    URL = reverse('courses-list')
    response = client.get(URL)
    assert response.status_code == 200
    for i, v in enumerate(response.data):
        assert v['name'] == course[i].name


@pytest.mark.django_db
def test_course_filter_id(client, course_factory):
    course = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/', {'id': course[0].id})
    assert response.status_code == 200
    assert response.data[0]['id'] == course[0].id


@pytest.mark.django_db
def test_course_filter_name(client, course_factory):
    course = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/', {'name': course[1].name})
    assert response.status_code == 200
    assert response.data[0]['name'] == course[1].name


@pytest.mark.django_db
def test_create_course(client):
    URL = reverse('courses-list')
    response = client.post(URL, {'name': 'biology'})
    assert response.status_code == 201
    assert response.data['name'] == 'biology'


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=5)
    URL = reverse('courses-detail', args=[course[1].id])
    response = client.patch(URL, {'name': 'math'})
    assert response.status_code == 200
    assert response.data['name'] == 'math'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=5)
    URL = reverse('courses-detail', args=[course[1].id])
    response = client.delete(URL)
    assert response.status_code == 204
    assert response.data is None


# @pytest.mark.parametrize('count1, count2', [(10, 20)])
# def test_student_count(count1, count2):
#     assert count1 == count2