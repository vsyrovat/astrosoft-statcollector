from django.test import Client, TestCase

from .models import AccessLogEntry


# Create your tests here.
class AccessLogTests(TestCase):
    def setUp(self):
        AccessLogEntry.objects.create(
            user_agent="Firef0x", ip="0:1", accept_language="Fr-de"
        )

    def test_read_object(self):
        logs = list(AccessLogEntry.objects.all())
        self.assertEquals(logs, [AccessLogEntry(id=1)])

    def test_handle_bare_request(self):
        c = Client()
        response = c.get("/data/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AccessLogEntry.objects.count(), 2)

    def test_handle_request(self):
        c = Client(headers={"user-agent": "curl/7.79.1", "accept-language": "Fr-fr"})
        c.get("/data/", REMOTE_ADDR="127.0.0.2")
        log = AccessLogEntry.objects.latest("id")
        self.assertEqual(log.accept_language, "Fr-fr")
        self.assertEqual(log.ip, "127.0.0.2")
        self.assertEqual(log.user_agent, "Other / Other / curl 7.79.1")
