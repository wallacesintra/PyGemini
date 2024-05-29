#!/usr/bin/python3

import google.generativeai as genai

from writePrompt import write_file

genai.configure(api_key= "your_gemini_api_key")


# model = genai.GenerativeModel('gemini-pro')


class MyGeminiApi():
    def __init__(self):
        self.generativeModel = genai.GenerativeModel('gemini-pro')

    def generate(self, text):
        response = self.generativeModel.generate_content(text)

        title = self.generativeModel.generate_content("generate a title and the title should not be more than 5 words in text for " + response.text)
        
        write_file(title.text + ".md", response.text)

        responseText = response.text

        return responseText
    