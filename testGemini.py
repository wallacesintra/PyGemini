#!/usr/bin/python3

import google.generativeai as genai

from writePrompt import write_file

genai.configure(api_key= "your_gemini_api_key")




model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("Gemini API")
# print(response.text)


class MyGeminiApi():
    def __init__(self):
        self.generativeModel = genai.GenerativeModel('gemini-pro')

    def generate(self, text):
        response = self.generativeModel.generate_content(text)

        title = self.generativeModel.generate_content("generate a title for " + response.text)
        write_file("history_" +title.text + ".md", response.text)

        return response.text
    
