from sys import exit
from os import makedirs, path
from shutil import copy

def create_public_files(appName):
    if not path.exists(appName + r"public"):
        makedirs(appName + r"public")

    with open(appName + r'README.md', "w+") as f:
        f.write("""#Build Web App:
        Welcome to BuildWebApp, the purpose is to remove the strain of creating all the boilerplate
        for a new web project. Simply pick what initial setup you have, install any additional tools
        you would like to use, and start coding!""")

    copy(r'initialBoiler/public/style.css', appName + r'public/style.css')
    copy(r'initialBoiler/public/index.html', appName + r'public/index.html')
    copy(r'initialBoiler/public/favicon.ico', appName + r'public/favicon.ico')


def create_server_files(appName, server):
    with open(r"initialBoiler/server/" + server + r".js", "r") as f:
        serverIndex = f.read()
        try:
            makedirs(appName + 'server')
        except FileExistsError:
            print("The app name you gave already exists as a folder, either delete it or move to a different directory")
            exit()
        with open(appName + r'server/index.js', "w+") as f1:
            f1.write(serverIndex)
            f1.close()
        f.close()

def create_frontend_files(appName, frontend):
    with open(r"initialBoiler/client/" + frontend + r"Index.js", "r") as f:
        clientIndex = f.read()
        try:
            makedirs(appName + "client")
        except FileExistsError:
            print("The app name you gave already exists as a folder, either delete it or move to a different directory")
            exit()
        with open(appName + r"client/index.js", "w+") as f1:
            f1.write(clientIndex)
            f1.close()
        f.close()
    with open(r"initialBoiler/client/" + frontend + r"App.js", "r") as f:
        clientApp = f.read()
        with open(appName + r"client/app.js", "w+") as f1:
            f1.write(clientApp)
            f1.close()
        f.close()

def create_package_json(appName, dependencies, devDependencies):
    copy(r"initialBoiler/package.json", appName + r"package.json")
    with open(appName + r"package.json", "a") as f:
        for i in dependencies:
            f.write("  " + i)
        f.write("\n" + r"}," + "\n" + r'"devDependencies": {' + "\n    ")
        for i in devDependencies:
            f.write(i)
        f.write("\n" + r'}' + "\n" + r'}')
