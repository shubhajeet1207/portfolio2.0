![mockupmockup](https://user-images.githubusercontent.com/76960580/169701652-a38f928e-8415-400b-9d75-4485480f2bd0.png)

<hr>

## Tech Stack Used


<img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?logo=javascript&logoColor=black"></a>
<img alt="Markdown" src="https://img.shields.io/badge/Markdown-000000.svg?logo=markdown&logoColor=white"></a>
<img alt="Python" src="https://img.shields.io/badge/Python-14354C.svg?logo=python&logoColor=white"></a>
<img alt="django" src="https://custom-icon-badges.herokuapp.com/badge/django-25A162.svg?logo=django&logoColor=white"></a>
<img alt="CSS" src="https://img.shields.io/badge/CSS-1572B6.svg?logo=css3&logoColor=white"></a>
<img alt="HTML" src="https://img.shields.io/badge/HTML-E34F26.svg?logo=html5&logoColor=white"></a>
<img alt="Bootstrap" src="https://img.shields.io/badge/Bootstrap-7952B3.svg?logo=bootstrap&logoColor=white"></a>
<img alt="Heroku" src="https://img.shields.io/badge/Heroku-430098.svg?logo=heroku&logoColor=white"></a>
<img alt="MongoDB" src ="https://img.shields.io/badge/MongoDB-4ea94b.svg?logo=mongodb&logoColor=white"></a>
<img alt="SQLite" src ="https://img.shields.io/badge/SQLite-07405e.svg?logo=sqlite&logoColor=white"></a>
<img alt="Pycharm" src="https://img.shields.io/badge/Pycharm-FFD700.svg?logo=Pycharm&logoColor=black"></a>
</div>
<hr>

## Deployment

To get this portfolio on your system follow the below steps:

1. Clone this repository
```bash
  git clone https://github.com/shubhajeet1207/portfolio2.0
```
2. Create a new Virtual environment so that, no package version confilct issue raise.
```bash
  virtualenv your_virtual_env_name
```
3. Activate your Virtual Environment
```bash
  .\your_virtual_env_name\Scripts\activate
```
4. Install al the requirements mentioned in the requirements.txt
```bash
  pip install -r requirements.txt
```
5. Now,  generate the SQL commands for preinstalled apps.
```bash
  python manage.py makemigrations
```
6. Now, migrate the changes made in the Database.
```bash
  python manage.py migrate
```
7. Create a super user so that, you can view the your Admin Panel.
```bash
  python manage.py createsuperuser
```
<hr>

## Documentation

- [django](https://docs.djangoproject.com/en/4.0/)
- [Cloudinary](https://cloudinary.com/documentation/django_integration#overview)
- [SendGrid](https://www.twilio.com/blog/using-twilio-sendgrid-send-emails-python-django)
- [MongoDb with Django](https://www.analyticsvidhya.com/blog/2021/06/how-to-connect-mongodb-database-with-django/)
- [Serializers](https://www.django-rest-framework.org/tutorial/1-serialization/)

<hr>

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

- `SENDGRID_API_KEY` - This would be your sendgrid api key.

- `DEFAULT_FROM_EMAIL` - This would be your default email which you'll be using as your sender mail id.

- `API_KEY` - This is your Cloudinary API Key.

- `API_SECRET` - This would be your Cloudinary Secret Key.


