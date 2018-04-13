from django.test import TestCase
from sigedb.contractors.forms import ContractorForm

class ContractorTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/contractor/')

    def test_get(self):
        """Get /contractor/ must return status 200"""
        response = self.client.get('/contractor/')
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use contractors/contractor_form.html"""
        response = self.client.get('/contractor/')
        self.assertTemplateUsed(self.resp, 'contractors/contractor_form.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have contractor form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, ContractorForm)

    def form_has_fields(self):
        """Form must have 5 fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['contractor', 'director', 'address', 'telephone', 'email'], list(form.fields))


class ContractorPostTest(TestCase):
    def setUp(self):
        data = dict(contractor='Timor-Timor Lda', director='João do Timor', address='R. Jacinto, 233',
                    telephone='670-7777-1234', email='timortimor@gmail.com')
        self.resp = self.client.post('/contractor/', data)

    def test_post(self):
        """Valid POST should redirect /contractor/"""
        self.assertEqual(302, self.resp.status_code)


# class ContractorInvalidPost(TestCase):
#     def setUp(self):
#         self.resp = self.client.post('/contractor/', {})
#
#     def test_post(self):
#         """Invalid POST should not redirect"""
#         self.assertEqual(200, self.resp.status_code)
#
#     def test_template(self):
#         self.assertTemplateUsed(self.resp, 'contractors/contractor_form.html')
