import pytest
from rest_framework.reverse import reverse
from butter_exercise.users.models import Agreement

# pytest butter_exercise/users/api/tests -s


@pytest.mark.django_db
class TestAgreementViewSet:

    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.client = api_client

    def test_list(self, agreement):
        url = reverse("user-agreements-list", [agreement.user.pk])
        response = self.client.get(url)

        assert response.status_code == 200

        data = response.json()

        assert len(data) == 1
        assert data[0]['pk'] == agreement.pk
        assert data[0]['html'] == agreement.get_html()

    def test_post(self, user):
        url = reverse("user-agreements-list", [user.pk])
        data = {
            "first_name": "Harald",
            "last_name": "Bluetooth",
            "street": "Denmark street",
            "post_code": "01234"
        }
        response = self.client.post(url, data={"data": data})

        assert response.status_code == 201
        agreement = Agreement.objects.get()
        assert agreement.user == user

    def test_update_not_allowed(self, agreement):
        url = reverse("user-agreements-detail", [agreement.user.pk, agreement.pk])
        response = self.client.put(url, data={"data": {}})
        assert response.status_code == 405
        response = self.client.patch(url, data={"data": {}})
        assert response.status_code == 405
