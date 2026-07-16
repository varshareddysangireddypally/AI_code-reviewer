!pip -q install google-genai gradio
from google import genai
import gradio as gr
client=genai.Client(api_key="AQ.Ab8RN6J3eXMAMfdyEI3emhAYyIkHGpHR0O5d0b_pVTLe3wXg4g")
def review_code(code):
  prompt=f"""
  Review this Python code.
  Provide:
  1.Summary
  2.Bugs
  3.Performance Improvements
  4.Code Style
  5.Security Issues
  6.Improved Code
  7.Rating out of 10
  Code:
  {code}
  """
  response=client.models.generate_content(
      model="gemini-2.5-flash",
      contents=prompt
  )
  return response.text
demo=gr.Interface(
    fn=review_code,
    inputs=gr.Textbox(label="code"),
    outputs="markdown",
    title="AI Code Reviewer (Gemini)"
)
demo.launch()
