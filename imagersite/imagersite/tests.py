"""."""

from django.test import Client
from django.test import TestCase
from django.core import mail
import pdb

from contextlib import contextmanager
from io import StringIO
import sys


@contextmanager
def captured_output():
    """Used to capture standard output."""
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class ProfileTestCase(TestCase):
    """."""

    def test_home_route_response_200(self):
        """."""
        c = Client()
        response = c.get('/')
        self.assertTrue(response.status_code == 200)

    def test_login_route_response_200(self):
        """."""
        c = Client()
        response = c.get('/accounts/login/')
        self.assertTrue(response.status_code == 200)

    def test_register_route_response_200(self):
        """."""
        c = Client()
        response = c.get('/accounts/register/')
        self.assertTrue(response.status_code == 200)

    def test_mailbox_empty(self):
        """."""
        self.assertEqual(len(mail.outbox), 0)

    def test_register_post_new_account_redirects(self):
        """."""
        c = Client()
        response = c.post('/accounts/register', {'username': 'test1',
                                                 'email': 'test@test.com',
                                                 'password1': 'UltraTest',
                                                 'password2': 'UltraTest'}, follow=True)
        self.assertTrue(response.status_code == 200)

    # def test_register_post_new_account_makes_email(self):
    #     """."""
    #     with captured_output() as (out, err):
    #         c = Client()
    #         c.post('/accounts/register', {'username': 'test1',
    #                                       'email': 'test@test.com',
    #                                       'password1': 'UltraTest',
    #                                       'password2': 'UltraTest'})

    #         pdb.set_trace()