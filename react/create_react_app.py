import sys
import os
from loguru import logger

index_efml = """
webd: html
<efml>
  <head>
    <meta html-equiv="a" translate="hyperlink">
    <meta html-equiv="link" translate="insert">
    <meta html-equiv="pass" translate="ReactPassin">
    <meta html-equiv="mix" translate="ReactMixin">
  </head>
  <outmix>
    <mix rel="localhost:5000/react/dll">
  </outmix>
</efml>
"""

react_yaml = """
react:
  server:
    password: "youshallnotpass"
    
metrics:
  prometheus:
    enabled: false
    endpoint: /metrics

sentry:
  dsn: ""
  environment: ""
#  tags:
#    some_key: some_value
#    another_key: another_value

logging:
  file:
    max-history: 30
    max-size: 1GB
  path: ./logs/

  level:
    root: INFO
    react: INFO
"""


proj_name = sys.argv[1]
if proj_name == "-R":
    command = sys.argv[2]
    print(command)
    if command == "eject":
        logger.info(f'Searching for react.yaml file...')
        for roots,_s,files in os.walk(os.getcwd()):
          for _ in _s:
           for file in _:
            print(f'Checking Usability of {file}...')
            if file == "react.yaml":
                logger.warning('React is uninstalling itself from ',_)
                for _root,_dir,_file in os.walk('.'):
                    os.remove(_file)
                    os.remove(_dir)
    exit()

logger.info(f"Creating new empty React.py App in {proj_name}...")
os.mkdir(proj_name)
os.chdir(proj_name)
logger.info("\nCreating Files, Please wait:")
logger.info("\nCreating `index.efml`, `react.yaml`, `react-gyp.ymx`")
os.mkdir("react-data")
with open("react-data/index.efml",'w+') as f:
    f.write(index_efml)
with open("react-data/react.yaml",'w+') as f:
    f.write(react_yaml)
with open("react-data/react-gyp.ymx",'w+') as f:
    f.write(index_efml)

os.mkdir("react-src")
os.mkdir("templates")
with open("main.py",'w+') as f:
    f.write("""
from react.app import ReactApp, ReactBuiltinServer, render_template

server = ReactBuiltinServer(__name__)
app = ReactApp(server)

@app.component()
def helloworld(props):
    return "<h1>Hello World!</h1>"

@server.route("/")
def main():
    return render_template("index.html",app)

server.run()
    """)
with open("templates/index.html",'w+') as f:
    f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <helloworld>
</body>
</html>
    """)


logger.info("Success! The React App has been built. Run `main.py` to see.\nRun py -m create_react_app.py -R eject to remove the project\n\nHappy hacking! :)")
