from sys import exit
from os import makedirs, path
from shutil import copy
import fileinput

def file_prepender(filepath, lineInput):
    with open(filepath, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(lineInput.rstrip('\r\n') + '\n' + content)
        f.close()

# inserts newString to file one line after stringToFind
def insert_line(filepath, stringToFind, newString):
    actualLines = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
    f.close()
    with open(filepath, 'w+') as f:
        for line in lines:
            actualLines.append(line)
            if line.startswith(stringToFind):
                actualLines.append(newString + '\n')
        f.write("".join(actualLines))
    f.close()
    return

def replace_line_substring(filepath, stringToFind, substr, replacement):
    actualLines = []
    with open(filepath, "r") as f:
        lines = f.readlines()
    f.close()
    with open(filepath, "w+") as f:
        for line in lines:
            if line.startswith(stringToFind):
                line = line.replace(substr, replacement)
            actualLines.append(line)
        f.write("".join(actualLines))
    f.close()
    return

def pad_line(filepath, stringToFind, pad = "  ", numOfLines = 1):
    actualLines = []
    startPadding = False
    with open(filepath, 'r') as f:
        lines = f.readlines()
    f.close()
    with open(filepath, "w+") as f:
        for line in lines:
            if line.startswith(stringToFind):
                startPadding = True
            if startPadding == True:
                line = pad + line
                numOfLines -= 1
                if numOfLines <= 0:
                    startPadding = False
            actualLines.append(line)
        f.write("".join(actualLines))
    f.close()
    return


def create_public_files(appName):
    publicPath = appName + r'public/'
    if not path.exists(publicPath):
        makedirs(publicPath)

    with open(appName + r'README.md', "w+") as f:
        f.write("""# Create Web App
        This app was initialized with Create Web App, the purpose of which is to remove the strain of creating all the boilerplate
        for a new web project and standardize the filesystem architecture. Simply pick what initial setup you have, install any additional tools
        you would like to use, and start coding, like this person did!""")

    copy(r'initialBoiler/public/style.css', publicPath + r'style.css')
    copy(r'initialBoiler/public/index.html', publicPath + r'index.html')
    copy(r'initialBoiler/public/favicon.ico', publicPath + r'favicon.ico')
    copy(r'initialBoiler/public/apple-touch-icon.png', publicPath + r'apple-touch-icon.png')


def create_server_files(appName, env):
    server = env["server"].lower()
    with open(r"initialBoiler/server/" + server + r".js", "r") as f:
        serverIndex = f.read()
        try:
            makedirs(appName + 'server')
            makedirs(appName + 'server/api')
            if server.startswith('express'):
                copy(r'initialBoiler/server/api/index.js', appName + r'server/api/index.js')
        except FileExistsError:
            print("The app name you gave already exists as a folder, either delete it or move to a different directory")
            exit()
        with open(appName + r'server/index.js', "w+") as f1:
            f1.write(serverIndex)
            f1.close()
        f.close()


def create_frontend_files(appName, env):
    frontend = env["frontend"].lower()
    if frontend != 'none':
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
            with open(appName + r"client/App.js", "w+") as f1:
                f1.write(clientApp)
            f1.close()
        f.close()
        if frontend == "react":
            makedirs(appName + r"components")
            copy(r"initialBoiler/client/components/index.js", appName + r"client/components/index.js")
            copy(r"initialBoiler/client/history.js", appName + r"client/history.js")
            copy(r"initialBoiler/public/reactIndex.js", appName + r'public/index.js')
            copy(r"initialBoiler/client/reactIndex.js", appName + r'client/index.js')
            if 'React-Redux' in env['tools']:
                insert_line(
                appName + r"client/index.js",
                r"import ReactDOM",
                r"import store from '../client/store'"
                )
                insert_line(
                    appName + r"client/index.js",
                    r"import ReactDOM",
                    r"import {Provider} from 'react-redux'"
                )
                pad_line(
                    appName + r"client/index.js",
                    r"  <Router",
                    "  ",
                    3
                )
                insert_line(
                    appName + r"client/index.js",
                    r"export default",
                    r"  <Provider store={store}>"
                )
                insert_line(
                    appName + r"client/index.js",
                    r"    </Router",
                    r"  </Provider>,"
                )
                insert_line(
                    appName + r"public/index.js",
                    r"    </Router",
                    r"  </Provider>,"
                )
                replace_line_substring(
                    appName + r"client/index.js",
                    r"    </Router",
                    ",",
                    ""
                )
                # copy(r"initialBoiler/client/reactReduxIndex.js", appName + r'public/index.js')
            if 'Webpack' in env['tools']:
                # this will replace each import statement for webpack filestructure
                replace_line_substring(
                    appName + r'client/index.js',
                    "import",
                    r"../client",
                    r"."
                )

def create_package_json(appName, env):
    packagePath = appName + r"package.json"
    copy(r"initialBoiler/package.json", packagePath)
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
    elif 'Webpack' in env['tools']:
        copy(r"initialBoiler/webpack.config.js", appName + r"webpack.config.js")
        copy(r"initialBoiler/.babelrc", appName + r".babelrc")
        replace_line_substring(
            packagePath,
            r'    "start"',
            r"parcel watch public/index.html & nodemon server",
            r"npm run build-watch -- npm run start-server"
        )
        replace_line_substring(
            packagePath,
            r'    "build-watch"',
            r"parcel watch ./public/index.html",
            r"webpack -w"
        )
        replace_line_substring(
            packagePath,
            r'  "main"',
            r"index.js",
            r"webpack.config.js"
        )

    with open(packagePath, "a") as f:
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
        replace_line_substring(
            serverFile,
            r'  app.use(express.static(path.join',
            r'dist',
            r"public"
        )
        replace_line_substring(
            serverFile,
            r"    res.sendFile(path.join(__dirname, '..', 'dist/index.html'))",
            r'dist',
            r"public"
        )
    if 'Sequelize' in env['tools']:
        if not path.exists(appName + 'server/db'):
            makedirs(appName + r'server/db')
        if not path.exists(appName + r'server/db/models'):
            makedirs(appName + r'server/db/models')
        copy(r'initialBoiler/server/db/index.js', appName + r'server/db/index.js')
        copy(r'initialBoiler/server/db/db.js', appName + r'server/db/db.js')
        copy(r'initialBoiler/server/db/models/index.js', appName + r'server/db/models/index.js')
        if env['database'] == 'PostgreSQL':
            with open(appName + r'server/db.js', 'w+') as f:
                f.write("""const Sequelize = require('sequelize')
const databaseName = """ + "'" + env['dbname'] + "' " +"""+ (process.env.NODE_ENV === 'test' ? '-test' : '')

const db = new Sequelize(
  process.env.DATABASE_URL || `postgres://localhost:5432/${databaseName}`,
  { logging: false }
)
module.exports = db
""")
                f.close()
    if 'Redux' in env['tools']:
        try:
            makedirs(appName + 'client/store')
        except FileExistsError:
            print('The app name you picked already exists as a directory. Exiting installation')
            exit()
        copy(r'initialBoiler/client/store/index.js', appName + r'client/store/index.js')
        copy(r'initialBoiler/client/store/user.js', appName + r'client/store/user.js')
