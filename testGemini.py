#!/usr/bin/python3

import google.generativeai as genai

genai.configure(api_key= "your_gemini_api_key")



model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("Gemini API")
# print(response.text)


class MyGeminiApi():
    def __init__(self):
        self.generativeModel = genai.GenerativeModel('gemini-pro')

    def generate(self, text):
        response = self.generativeModel.generate_content(text)
        return response.text
