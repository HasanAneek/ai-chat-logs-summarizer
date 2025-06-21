import unittest
import os
from chat_summarizer import ChatSummarizer

class TestChatSummarizer(unittest.TestCase):

    def setUp(self):
        """Set up a test chat file and summarizer instance."""
        self.summarizer = ChatSummarizer()
        self.test_chat_content = (
            "User: Hello\n"
            "AI: Hi there\n"
            "User: test python\n"
            "AI: python is a language\n"
        )
        self.test_file_path = "test_chat.txt"
        with open(self.test_file_path, "w") as f:
            f.write(self.test_chat_content)

    def tearDown(self):
        """Remove the test chat file."""
        os.remove(self.test_file_path)

    def test_parse_chat_log(self):
        """Test parsing of a chat log."""
        user_msgs, ai_msgs = self.summarizer.parse_chat_log(self.test_file_path)
        self.assertEqual(len(user_msgs), 2)
        self.assertEqual(len(ai_msgs), 2)
        self.assertEqual(user_msgs[1], "test python")
        self.assertEqual(ai_msgs[1], "python is a language")

    def test_get_message_statistics(self):
        """Test calculation of message statistics."""
        user_msgs = ["msg1", "msg2"]
        ai_msgs = ["resp1"]
        stats = self.summarizer.get_message_statistics(user_msgs, ai_msgs)
        self.assertEqual(stats['total_messages'], 3)
        self.assertEqual(stats['user_messages'], 2)
        self.assertEqual(stats['ai_messages'], 1)

    def test_extract_keywords(self):
        """Test keyword extraction."""
        messages = ["python is great for python programming", "I love programming in python"]
        keywords = self.summarizer.extract_keywords(messages, top_n=3)
        self.assertEqual(keywords[0], ('python', 3))
        self.assertEqual(keywords[1], ('programming', 2))
        self.assertEqual(keywords[2], ('great', 1))

if __name__ == '__main__':
    unittest.main()