from app import create_app
from app.utils.env import SWAGGER_URL, API_URL, APP_NAME, OPENAI_API_KEY
from flask_swagger_ui import get_swaggerui_blueprint
from flask import render_template, request
import openai
# from chatgpt import app

app = create_app()


@app.route('/', methods=['GET'])
def status():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)


def get_Chat_response(text):
        
    for step in range(3):
        openai.api_key = "OPENAI_API_KEY"
        output = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "assistant", "content": 
                    "SaaSpectrum is your one-stop-shop for diverse, seamlessly integrated Software as a Service (SaaS) solutions, empowering businesses to manage all facets of their operations with unparalleled efficiency. From e-commerce to CRM, we've got the full spectrum of cutting-edge SaaS offerings to drive your success." + text}]
        )

        # Get the output text only
        return output['choices'][0]['message']['content']


if __name__ == '__main__':
    # Call factory function to create our blueprint
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to {SWAGGER_URL}
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': APP_NAME
        }
    )
    
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    app.run()
