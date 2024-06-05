#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from console import MyPrompt

from Gemini_api import MyGeminiApi
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.table import Table
from util import Util

gemini = MyGeminiApi()
console = Console()
text = Text()
util = Util()

table = Table(title="History")
table.add_column("Title", style="bold yellow")

class MyPromptTest(unittest.TestCase):
    def setUp(self):
        self.prompt = MyPrompt()

    def test_exit(self):
        with patch('builtins.print') as mock_print:
            self.assertTrue(self.prompt.do_exit(None))
            mock_print.assert_called_with("Goodbye, see you soon ...", style="bold yellow")

    def test_hello(self):
        with patch('builtins.print') as mock_print:
            self.prompt.do_hello("Alice")
            mock_print.assert_called_with("Hello", "Alice")

    def test_generate(self):
        with patch('builtins.print') as mock_print:
            self.prompt.do_generate("content")
            mock_print.assert_called_with("Generating content for", "content")

    def test_clear(self):
        with patch('os.system') as mock_system:
            self.prompt.do_clear(None)
            mock_system.assert_called_with('clear')

    def test_default(self):
        with patch('rich.markdown.Markdown') as mock_markdown, \
                patch('rich.console.Console.print') as mock_print:
            self.prompt.default("content")
            mock_markdown.assert_called_with(gemini.generate("content"))
            mock_print.assert_called_with(mock_markdown.return_value, style="bold green")

    def test_history_no_files(self):
        with patch('os.listdir') as mock_listdir, \
                patch('rich.console.Console.print') as mock_print:
            mock_listdir.return_value = []
            self.prompt.do_history("")
            mock_print.assert_called_with("No history available", style="bold yellow")

    def test_history_with_files(self):
        with patch('os.listdir') as mock_listdir, \
                patch('rich.table.Table.add_row') as mock_add_row, \
                patch('rich.console.Console.print') as mock_print:
            mock_listdir.return_value = ["file1.md", "file2.md"]
            self.prompt.do_history("")
            mock_add_row.assert_called_with(util.replace_underscore.return_value)
            mock_print.assert_called_with(table)

    def test_history_view_content(self):
        with patch('os.listdir') as mock_listdir, \
                patch('os.system') as mock_system:
            mock_listdir.return_value = ["file1.md", "file2.md"]
            self.prompt.do_history("file1")
            mock_system.assert_called_with('python3 -m rich.markdown history/file1.md')

    def test_complete_history(self):
        with patch('os.listdir') as mock_listdir:
            mock_listdir.return_value = ["file1.md", "file2.md"]
            completions = self.prompt.complete_history("f", "", 0, 1)
            self.assertEqual(completions, ["file1"])

    def test_clear_history(self):
        with patch('os.system') as mock_system, \
                patch('rich.console.Console.print') as mock_print:
            self.prompt.do_clear_history(None)
            mock_system.assert_called_with('rm -rf history/*')
            mock_print.assert_called_with("History cleared", style="bold red")

if __name__ == '__main__':
    unittest.main()
