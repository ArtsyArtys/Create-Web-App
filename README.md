# Create Web App:
Welcome to Create Web App, the purpose is to remove the strain of creating all the boilerplate
for a new web project and to standardize new projects' directory system. Simply pick what initial setup you desire, install any additional tools
you would like to use, npm install, git init if you desire, and start coding!

## Installation
Ensure you have python installed on your device, you can check in the shell/cmd prompt with ```python --version```, if you don't have it you can install python through npm with ```npm install -g python``` or through their website here https://www.python.org/downloads/. In your shell/cmd line run ```pip install psycopg2 PyInquirer``` to install the dependencies for this project. Clone this project into your desired installation path with ```git clone https://github.com/ArtsyArtys/Create-Web-App```. Run Create Web App by changing directories into Create-Web-App and run it by typing in ```python create-web-app.py```. Follow the directions in the CLI to get started!

## Troubleshooting
  If you encounter any "ModuleNotFound" errors, there may have been errors during installation. While Python 2.7 and above has pip installed automatically, check to see it is installed on your machine with ```pip --version``` and install it with npm via ```npm install pip``` or by following the directions here https://pip.pypa.io/en/stable/installing/. Afterwards run ```pip install psycopg2 PyInquirer```. If you still have these errors, change directories into the psycopg2-2.8.4 folder and run ```python setup.py install```, then into the PyInquirer-1.0.3 and again run ```python setup.py install```
  Ensure you are not trying to make a project with a project name that you already have as a folder. In some cases, a failed attempt might leave a folder created named by your inputted project name. Delete the project folder create-web-app created (ensure you're not deleting any previous projects) and try again.
  If there are any issues, please describe the problem, the stacktrace that was given (if one was), and what steps you took before the problem occurred to Randy@ArtsyArtys.com.

### Next Steps
  Current bugs and incomplete parts being worked on:
  - [ ] Database connection not automatic without using Sequelize
  - [ ] Websocket.io not functioning
  - [ ] Google Oauth not functioning
  - [ ] TypeOrm not functioning
  - [ ] SQLAcademy not functioning
  - [ ] Doctrine2 not functioning
  - [ ] MySQL database not being created properly

  Additions to be made:
  - [ ] dotenv inclusion for node projects
  - [ ] Facebook Oauth
  - [ ] Production and Test environments specified during app creation.
  - [ ] Controller directory to be made in all Node.js projects for callbacks
  - [ ] http-server to be used for Node.js when no backend framework is specified
  - [ ] Examples for Fastify routes and controllers
  - [ ] Examples for Koa routes and controllers
  - [ ] Angular base setup to be made
  - [ ] Vue base setup to be made
  - [ ] Ruby on Rails to be added to Runtime Environment options

  Current focus is on fixing database connections and converting to .exe format for simplified installation across all operating systems. Then current bugs and incomplete parts will be attended and additions will then be made.



  The current version of Create Web App is version 1.0.5 and has been tested extensively with the NERD stack. Updates will be posted regularly. Issues, complaints, and design decisions are welcome to be discussed via email at Randy@ArtsyArtys.com.
