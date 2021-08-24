# ZetuFeed Web Application
#### A blog app.

#### By **Patrick Mwangangi**
## Description
This a nifty application created to serve as a platform where interested users are able to maintain a blog while sharing their views on matters that matter to them.

Further to the above usage, this master piece was created as practice on concepts learnt in Python Flask (at Moringa School).
## Demo

Here is a working live demo : https://zetufeed.herokuapp.com/
## Setup/Installaction Requirements
- Clone the repository (repo).
    ```
    git clone https://github.com/kiman121/kwetu-feed.git
    ```
- Open the project on VS Code or any editor of choice.
- Navigate to the projects root directory.
- Open the virtual environment by running the `source virtual/bin/activate` command.
- Install the required packages: `pip install -r requirements.txt`
- Create a .env file and add the following data instances
    ```
    FLASK_APP=<'app name'>
    FLASK_ENV=<'environment'>
    DATABASE=<'database_name'>
    POSTGRES_USER=<'postgres_user'>
    POSTGRES_PASSWORD=<'postgres_password'>
    SQLALCHEMY_DATABASE_URI=<'database_urli'>
    MAIL_USERNAME = <'email_username'>
    MAIL_PASSWORD = <'email_password>
    ```
- Run migrations to update the changes to db: `flask db upgrade`
- Configure a start.sh file to execute your app
- Execute you start.sh file from terminal to lauch app
- open this url on your browser "http://127.0.0.1:5000/"
## Known Bugs

No Known bugs

## Technology Used
- HTML
- CSS
- Javascript
- Bootstrap
- Python
- Flask

## Support and contact details

If you want to contact us, email us on info@kwetu-feed.com

### License

[MIT licence](https://github.com/kiman121/kwetu-feed/blob/master/LICENCE)
Copyright (c) 2021 **ZetuFeed**