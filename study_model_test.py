from django.test import TestCase
from learning_logs.models import Topic,Entry


class ModelTest(TestCase):

    def setUp(self):
        Topic.objects.create(id=8, text='Running2', date_added='datetime', owner_id=1)
        Entry.objects.create(id=7, text='浩浩', date_added='datetime', topic_id=2)

    def test_topic_models(self):
        result = Topic.objects.get(id=8)
        self.assertEqual(result.text, 'Running2')
        elf.assertEqual(result.owner_id, 1)

    def test_entry_models(self):
        result1 = Entry.objects.get(id=7)
        self.assertEqual(result1.text, '浩浩')
        self.assertEqual(result1.topic_id, 1)
