from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from services.models import Category, Type, Service

User = get_user_model()

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Test Category", image_url="http://example.com/image.png")
        self.type = Type.objects.create(name="Test Type", category=self.category)
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.service = Service.objects.create(category=self.category, types=self.type, user=self.user, price_min=10, price_max=100)
        self.client.login(username='testuser', password='testpassword')
    
    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        self.assertContains(response, self.category.name)

    def test_service_list_view(self):
        response = self.client.get(reverse('service_list', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_list.html')
        self.assertContains(response, self.service.price_min)

    def test_add_service_view_get(self):
        response = self.client.get(reverse('add_service'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_service.html')

    def test_add_service_view_post(self):
        response = self.client.post(reverse('add_service'), {
            'category': self.category.id,
            'types': self.type.id,
            'price_min': 20,
            'price_max': 200,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Service.objects.count(), 2)

    def test_get_my_profile_view(self):
        response = self.client.get(reverse('my_profile_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, self.user.email)

    def test_get_profile_view(self):
        response = self.client.get(reverse('profile_page', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, self.user.email)

    def test_login_page_view(self):
        self.client.logout()
        response = self.client.get(reverse('login_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_view(self):
        response = self.client.get(reverse('logout_user'))
        self.assertEqual(response.status_code, 302) 

    def test_register_page_view_get(self):
        response = self.client.get(reverse('register_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_page_view_post(self):
        response = self.client.post(reverse('register_page'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword',
