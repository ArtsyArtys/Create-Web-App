from __future__ import print_function, unicode_literals
from writeFromFileToFile import create_public_files, create_server_files, create_frontend_files, create_package_json, create_tools, insert_line
from sys import exit
from PyInquirer import style_from_dict, Token, prompt#, Separator
from connectdb import connectdb
from os import makedirs

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


env = {}
dependencies = []
devDependencies = []
appName = input('Input the name of your app: ') + r'/'

def create_folders(env):
    if env['frontend'] != 'None' and env['server'] != 'None':
        list = ['public', 'client', 'server']
        for dir in list:
            try:
                makedirs(appName + dir)
            except FileExistsError:
                print("The app name you gave already exists as a folder, either delete it or move to a different directory")
                exit()
        create_public_files(appName)


question = [
    {
        'type': 'list',
        'message': 'Select Runtime Environment: ',
        'name': 'runtime',
        'choices': [
            # { 'name': 'User FSA Stack', 'checked': True },
            { 'name': 'Node' },
            { 'name': 'Python', 'disabled': True },
            { 'name': 'Elixir', 'disabled': True },
            { 'name': 'Go', 'disabled': True },
            { 'name': 'Deno (insecure)', 'disabled': True },
            { 'name': 'None (raw)', 'disabled': True }
        ],
    }
]



runtime = prompt(question, style=style)['runtime']
env['runtime'] = runtime

if runtime == 'User FSA Stack':
    env = {'frontend': 'React', 'server': 'Express'}
    create_folders(appName, env)
    exit()

backendChoices = []
if runtime == 'Node':
    backendChoices.append({'name': 'Express', 'checked': True})
    backendChoices.append({'name': 'Fastify'})
    backendChoices.append({'name': 'Koa'})
    dependencies.append(r'"compression": "^1.7.3",' + "\n")
elif runtime == 'Python':
    backendChoices.append({ 'name': 'Django' })
    backendChoices.append({ 'name': 'Flask'})
    # backendChoices.append({ 'name': 'Sinatra'})

backendChoices.append({'name': 'None'})

serverQuestion = [
    {
        'type': 'list',
        'message': 'Select Backend Server: ',
        'name': 'server',
        'choices': backendChoices,
    },
]

server = prompt(serverQuestion, style=style)['server']
env['server'] = server
if server == 'Express':
    dependencies.append(r'"express": "^4.16.4",' + "\n")
    devDependencies.append(r'"morgan": "^1.9.1",' + "\n")
elif server == 'Fastify':
    devDependencies.append(r'"fastify": "^2.10.0"')

frontendQuestion = [
    {
        'type': 'list',
        'message': 'Select Frontend Framework',
        'name': 'frontend',
        'choices': [
            { 'name': 'React' },
            { 'name': 'Angular', 'disabled': True },
            { 'name': 'Ember', 'disabled': True },
            { 'name': 'Backbone', 'disabled': True },
            { 'name': 'Vue', 'disabled': True },
            { 'name': 'Meteor', 'disabled': True },
            { 'name': 'Mithril', 'disabled': True },
            { 'name': 'None' }
        ]
    }
]

frontend = prompt(frontendQuestion, style=style)['frontend']
env['frontend'] = frontend

if frontend == 'React':
    theseDependencies = [
        r'"history": "^4.9.0",' + "\n",
        r'"react": "^16.8.6",' + "\n",
        r'"react-dom": "^16.8.6",' + "\n",
        r'"react-router-dom": "^5.0.0",' + "\n"
    ]
    dependencies.extend(theseDependencies)

databaseQuestion = [
    {
        'type': 'list',
        'message': 'Select Database',
        'name': 'database',
        'choices': [
            { 'name': 'MySQL' },
            { 'name': 'PostgreSQL' },
            { 'name': 'Oracle', 'disabled': True },
            { 'name': 'MS SQL', 'disabled': True },
            { 'name': 'MongoDB', 'disabled': True },
            { 'name': 'DB2', 'disabled': True },
            { 'name': 'Neo4J', 'disabled': True },
            { 'name': 'DataStax Enterprise Graph', 'disabled': True },
            { 'name': 'None'}
        ]
    }
]

database = prompt(databaseQuestion, style=style)['database']
env['database'] = database
if database == 'PostgreSQL':
    myDependencies = [
        '"pg": "^7.9.0",' + "\n"
        '"pg-hstore": "^2.3.2",' + "\n"
    ]
    dependencies.extend(myDependencies)
    print("Remember -- database name will always be lowercase with underscores only")
    dbname = input("Input desired name of db: ")
    dbuser = input("Input database owner username: ")
    dbpass = input("Input database owner password (hit enter if null): ")
    connectdb(database, dbname, dbuser, dbpass)
    env['dbname'] = dbname

toolsQuestion = [
    {
        'type': 'checkbox',
        'message': r'Select Tools and Libraries (note parcel will be used if no bundler is picked)',
        'name': 'tools',
        'choices': [
            { 'name': 'Redux' },
            { 'name': 'React-Redux' },
            { 'name': 'Sequelize' },
            { 'name': 'TypeOrm'},
            { 'name': 'Websocket -io'},
            { 'name': 'Webpack' },
            { 'name': 'Parcel', 'checked': True }, # default
            { 'name': 'SQLAcademy' },
            { 'name': 'Doctrine 2' },
            { 'name': 'Google Oauth'},
        ]
    },
]

tools = prompt(toolsQuestion, style=style)['tools']
env['tools'] = tools
print(tools)
isParcel = False if 'Webpack' in tools else True
if 'Redux' in tools:
    dependencies.append('"redux": "^4.0.4",' + "\n")
    dependencies.append('"axios": "^0.19.0",' + "\n")
    dependencies.append('"redux-devtools-extension": "^2.13.8",' + "\n")
    dependencies.append('"redux-thunk": "^2.3.0",' + "\n")
if 'React-Redux' in tools:
    dependencies.append('"react-redux": "^7.1.3",' + "\n")
if 'Webpack' in tools:
    dependencies.append(r'"webpack": "^4.16.4",' + "\n")
    devDependencies.extend(['"@babel/core": "^7.4.3",' + "\n",
        '"@babel/plugin-proposal-class-properties": "7.4.0",' + "\n",
        '"@babel/plugin-proposal-decorators": "7.4.0",' + "\n",
        '"@babel/plugin-proposal-export-namespace-from": "7.2.0",' + "\n",
        '"@babel/plugin-proposal-function-sent": "7.2.0",' + "\n",
        '"@babel/plugin-proposal-json-strings": "7.2.0",' + "\n",
        '"@babel/plugin-proposal-numeric-separator": "7.2.0",' + "\n",
        '"@babel/plugin-proposal-throw-expressions": "7.2.0",' + "\n",
        '"@babel/plugin-syntax-dynamic-import": "7.2.0",' + "\n",
        '"@babel/plugin-syntax-import-meta": "7.2.0",' + "\n",
        '"@babel/polyfill": "^7.4.3",' + "\n",
        '"@babel/preset-env": "^7.4.3",' + "\n",
        '"@babel/preset-react": "^7.0.0",' + "\n",
        '"@babel/register": "^7.4.0",' + "\n",
        '"babel-eslint": "^10.0.1",' + "\n",
        '"babel-loader": "^8.0.5",' + "\n",
        '"webpack-cli": "^3.1.0",' + "\n",
        '"webpack": "^4.16.4",' + "\n"
    ])
else:
    dependencies.append(r'"parcelmon": "0.0.9",' + "\n")
    myDevDependencies = [
        '"babel-core": "^6.26.3",' + "\n",
        '"babel-preset-env": "^1.7.0",' + "\n",
        '"babel-preset-react": "^6.24.1",' + "\n",
        '"parcel-bundler": "^1.12.4",' + "\n"
    ]
    devDependencies.extend(myDevDependencies)
if 'Sequelize' in tools:
    dependencies.append(r'"crypto": "^1.0.1",' + "\n")
    devDependencies.append(r'"sequelize": "^5.21.2",' + "\n")


dependencies[-1] = dependencies[-1][0:-2]
devDependencies[-1] = devDependencies[-1][0:-2]
env["dependencies"] = dependencies
env["devDependencies"] = devDependencies
env["isParcel"] = isParcel
create_public_files(appName)
create_server_files(appName, env)
create_frontend_files(appName, env)
create_package_json(appName, env)
create_tools(appName, env)
print(appName + r' has been created. Change directories to ' + appName + r' and run npm install to get started!')
