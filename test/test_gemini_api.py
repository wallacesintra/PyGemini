#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from Gemini_api import MyGeminiApi

class MyGeminiApiTest(unittest.TestCase):
    def setUp(self):
        self.gemini = MyGeminiApi()

    def test_generate(self):
        with patch('genai.GenerativeModel.generate_content') as mock_generate_content, \
                patch('util.Util.replace_whitespace') as mock_replace_whitespace, \
                patch('writePrompt.write_file') as mock_write_file:
            mock_generate_content.return_value.text = "Generated content"
            mock_replace_whitespace.return_value = "Generated_Title"
            result = self.gemini.generate("input text")
            mock_generate_content.assert_called_with("input text")
            mock_replace_whitespace.assert_called_with(mock_generate_content.return_value.text)
            mock_write_file.assert_called_with("Generated_Title.md", "Generated content")
            self.assertEqual(result, "Generated content")

if __name__ == '__main__':
    unittest.main()