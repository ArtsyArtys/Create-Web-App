from sys import exit
from os import makedirs, path
from shutil import copy
import fileinput

# Used for prepending lines, check out f.seek and rstrip for line interpolation
def file_prepender(filepath, lineInput):
    with open(filepath, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(lineInput.rstrip('\r\n') + '\n' + content)
        f.close()

def replaceLines(filepath, startsWith, substr, replacement, single=False):
    lines = []
    with open(filepath, "r") as f:
        lines = f.readlines()
        f.close()
    with open(filepath, "w+") as f:
        for line in lines:
            if line.startswith(startsWith):
                line = line.replace(substr, replacement)
                if single == False:
                    print('found the line')
                    f.write(''.join(lines))
                    f.close()
                    return
        f.write(''.join(lines))
        f.close()
    return


def create_public_files(appName):
    if not path.exists(appName + r"public"):
        makedirs(appName + r"public")

    with open(appName + r'README.md', "w+") as f:
        f.write("""# Create Web App
        This app was initialized with Create Web App, the purpose of which is to remove the strain of creating all the boilerplate
        for a new web project. Simply pick what initial setup you have, install any additional tools
        you would like to use, and start coding, like this person did!""")

    copy(r'initialBoiler/public/style.css', appName + r'public/style.css')
    copy(r'initialBoiler/public/index.html', appName + r'public/index.html')
    copy(r'initialBoiler/public/favicon.ico', appName + r'public/favicon.ico')
    copy(r'initialBoiler/public/apple-touch-icon.png', appName + r'public/apple-touch-icon.png')


def create_server_files(appName, env):
    server = env["server"].lower()
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


def create_frontend_files(appName, env):
    frontend = env["frontend"].lower()
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
    if frontend == "react":
        copy(r"initialBoiler/client/history.js", appName + r"client/history.js")
        copy(r"initialBoiler/public/reactIndex.js", appName + r'public/index.js')

def create_package_json(appName, env):
    packageName = "parcelPackage.json" if env["isParcel"] == True else "webpackPackage.json"
    if env["isParcel"] == True:
        with open(appName + r".babelrc", "a+") as f:
            babels = []
            babels.append(r'"react", ') if env["frontend"] == 'React' else ""
            f.write(r'{' + "\n" + r'  "presets": ["env"')
            if len(babels) > 0:
                f.write(r', ')
            babels[-1] = babels[-1][0:-2]
            for str in babels:
                f.write(str)
            f.write(r']' + "\n" + r'}' + "\n")
            f.close()

    else:
        copy(r"initialBoiler/webpack.config.js", appName + r"webpack.config.js")
        copy(r"initialBoiler/.babelrc", appName + r".babelrc")

    copy(r"initialBoiler/" + packageName, appName + r"package.json")
    with open(appName + r"package.json", "a") as f:
        for i in env["dependencies"]:
            f.write("    " + i)
        f.write("\n" + r"  }," + "\n" + r'  "devDependencies": {' + "\n")
        for i in env["devDependencies"]:
            f.write("    " + i)
        f.write("\n" + r'  }' + "\n" + r'}')
        f.close()

def create_tools(appName, env):
    serverFile = appName + r'server/index.js'
    if env["isParcel"] == False:
        print('Should replace lines')
        replaceLines(
            serverFile,
            r'  app.use(express.static(path.join',
            'dist',
            r"public"
        )
        replaceLines(
            serverFile,
            r"    res.sendFile(path.join(__dirname, '..', 'dist/index.html'))",
            'dist',
            r"public"
        )
