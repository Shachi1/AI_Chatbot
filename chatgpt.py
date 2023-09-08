# import openai
# from app import create_app
# from app.utils.env import OPENAI_API_KEY
# from flask import Flask

# # app = Flask(__name__)
# app = create_app()


# @app.route('/chat')
# def index():

#   openai.api_key = OPENAI_API_KEY

#   output = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo", 
#     messages=[{"role": "assistant", "content": 
#               "You provide information for a service called SaaSpectrum. SaaSpectrum is your one-stop-shop for diverse, seamlessly integrated Software as a Service (SaaS) solutions, empowering businesses to manage all facets of their operations with unparalleled efficiency. From e-commerce to CRM, we've got the full spectrum of cutting-edge SaaS offerings to drive your success."}]
#   )

#   # Get the output text only
#   print(output['choices'][0]['message']['content'])
#   return render_template('chat.html')