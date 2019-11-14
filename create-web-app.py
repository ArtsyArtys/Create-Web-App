from __future__ import print_function, unicode_literals
from writeFromFileToFile import create_public_files, create_server_files, create_frontend_files
from sys import exit
from PyInquirer import style_from_dict, Token, prompt#, Separator
from connectdb import connectdb
from os import makedirs

# Used for prepending lines, check out f.seek and rstrip for line interloping

def line_prepender(filepath, lineInput, lineNum = 0):
    with open(filepath, 'r+') as f:
        content = f.read()
        f.seek(lineNum, 0)
        f.write(lineInput.rstrip('\r\n') + '\n' + content)
        f.close()



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

def create_server(env):
    create_server_files(appName, env['server'].lower())

def create_client(env):
    create_frontend_files(appName, env['frontend'].lower())


print(appName)
question = [
    {
        'type': 'list',
        'message': 'Select Runtime Environment: ',
        'name': 'runtime',
        'choices': [
            { 'name': 'User FSA Stack', 'checked': True },
            { 'name': 'Node' },
            { 'name': 'Python' },
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
create_public_files(appName)

backendChoices = []
if runtime == 'Node':
    backendChoices.append({'name': 'Express', 'checked': True})
    backendChoices.append({'name': 'Fastify'})
    backendChoices.append({'name': 'Koa'})
elif runtime == 'Python':
    backendChoices.append({ 'name': 'Django' })
    backendChoices.append({ 'name': 'Flask'})
    # backendChoices.append({ 'name': 'Sinatra'})

backendChoices.append({'name': 'None'})

print(backendChoices)


question = [
    {
        'type': 'list',
        'message': 'Select Backend Server: ',
        'name': 'server',
        'choices': backendChoices,
    },
]

server = prompt(question, style=style)['server']
env['server'] = server
if server == 'Express':
    dependencies.append(r'"express": "^4.16.4",' + "\n" + r'"history": "^4.9.0",' + "\n")

create_server(env)

question = [
    {
        'type': 'list',
        'message': 'Select Frontend Framework',
        'name': 'frontend',
        'choices': [
            { 'name': 'React' },
            { 'name': 'Ember', 'disabled': True },
            { 'name': 'Backbone', 'disabled': True },
            { 'name': 'Angular', 'disabled': True },
            { 'name': 'Vue', 'disabled': True },
            { 'name': 'Meteor', 'disabled': True },
            { 'name': 'Mithril', 'disabled': True },
            { 'name': 'None' }
        ]
    }
]

frontend = prompt(question, style=style)['frontend']
env['frontend'] = frontend

if frontend == 'React':
    theseDependencies = [
        r'"history": "^4.9.0",' + "\n",
        r'"react": "^16.8.6",' + "\n",
        r'"react-dom": "^16.8.6",' + "\n",
        r'"react-router-dom": "^5.0.0",' + "\n"
    ]
    dependencies.extend(theseDependencies)
    create_client(env)

question = [
    {
        'type': 'list',
        'message': 'Select Database',
        'name': 'database',
        'choices': [
            { 'name': 'PostgreSQL' },
            { 'name': 'MySQL' },
            { 'name': 'Oracle' },
            { 'name': 'MS SQL' },
            { 'name': 'MongoDB' },
            { 'name': 'DB2' },
            { 'name': 'Neo4J' },
            { 'name': 'DataStax Enterprise Graph' },
            { 'name': 'None'}
        ]
    }
]

database = prompt(question, style=style)['database']
if database != 'None':
    print("Remember -- database name will always be lowercase with underscores only")
    dbname = input("Input desired name of db: ")
    dbuser = input("Input database owner username: ")
    dbpass = input("Input database owner password (hit enter if null): ")
    connectdb(database, dbname, dbuser, dbpass)

#     {
#         'type': 'checkbox',
#         'message': 'Select Tools and Libraries',
#         'name': 'database',
#         'choices': [
#             { 'name': 'Redux' },
#             { 'name': 'React-Redux' },
#             { 'name': 'Sequelize' },
#             { 'name': 'Websocket -io'},
#             { 'name': 'Webpack' },
#             { 'name': 'Parcel' },
#             { 'name': 'SQLAcademy' },
#             { 'name': 'Doctrine 2' },
#             { 'name': 'Google Oauth'},
#             { 'name': 'TypeOrn'}
#         ]
#     },
# ]



# answers = prompt(questions, style=style)
# print(answers)
