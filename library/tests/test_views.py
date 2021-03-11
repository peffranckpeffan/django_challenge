import pytest
import json 
from django.urls import reverse, resolve
from django.test import TestCase


class TestBook:

    def setUp(self):
        self.client = APIClient()

    @pytest.mark.django_db
    def test_get_books(self):
        
        response = self.client.get(reverse('books'))
        content = json.loads(response.content)

        assert response.status_code == 200
        assert len(json.loads(content)) == 4
