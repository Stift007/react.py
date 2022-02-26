# React.py
Flask Utility to create your own HTML Components


## Usage

### Setup
to *start* a React Project, run this command: `python3 -m react.create_react_app your_project_name`   (Make sure your project's name has no spaces!)  
this will create a quick starter Project!

Inside, you will find this file structure:

```
|_.react-data
|_templates
  |_index.html
|_main.py
```

You should ignore .react-data, it isn't important for you  

### Create a Component

A component is made like this:

```py
@app.component()
def componentname(args):
  return "html goes here"
```

### Implementing the component
Inside templates/index.html, just do this:
`<componentname>` and that's it.

### Rendering the Project
Just like Flask does, react.py also uses Jinja2 to render it's HTML. This is done using the `render_template` function

```py
@server.route("/test")
def test():
  return render_template("templatename.html",appd)
```

### Deleting your Project  
Whyever you want to do this, you can delete your Project using `py -m react.create_react_app -R eject`.  
This will remove all Project Files
