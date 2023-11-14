from typing import Any, List, Dict
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from jinja2 import select_autoescape
from pathlib import Path


class EmailSchema(BaseModel):
    email: List[EmailStr]
    body: Dict[str, Any]
    subject : str
    template : str

class Email:
    async def sendMailTeste(self, email):
        # Define the config
        conf = ConnectionConfig(
            MAIL_USERNAME='john.lenon@smarti.com.br',
            MAIL_PASSWORD='ytqcdbddolxukfyj',
            MAIL_FROM='john.lenon@smarti.com.br',
            MAIL_PORT='465',
            MAIL_SERVER='smtp.gmail.com',
            USE_CREDENTIALS=True,
            VALIDATE_CERTS=True,
            TEMPLATE_FOLDER = 'app/templates',
        )
        # Generate the HTML template base on the template name

        message = MessageSchema(
            subject=email.dict().get("subject"),
            recipients=email.dict().get("email"),
            template_body=email.dict().get("body"),
            subtype='html',
        )

        # Send the email
        fm = FastMail(conf)
        await fm.send_message(message, template_name=f'{email.dict().get("template")}.html.j2')

    async def sendVerificationCode(self, token):
        test = list()
        test.append('fansubsbrasil@gmail.com')
        email = EmailSchema(email=test, body={'title': 'Hello World', 'name': 'John Doe', 'token': token}, subject='Your verification code (Valid for 10min)', template='verification' )
        await self.sendMailTeste(email=email)