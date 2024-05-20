#!/usr/bin/python3

import google.generativeai as genai

genai.configure(api_key= "your_gemini_api_key")

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Gemini API")
print(response.text)

