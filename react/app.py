from jinja2 import FileSystemLoader,Environment
from flask import Flask, send_from_directory
import typing as t


class ReactBuiltinServer(Flask):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def list_components(self,app):
        return [c["name"] for c in app.components]

    def run(self,*,ignore_components=False,**flask_args):
        super().run(**flask_args)

def render_template(template_name,app,**ctx):
    """Renders a Template with given Context and ReactApp Components.

    Args:
        template_name (str): Template Name
        app (ReactApp): Components get passed in automatically
    """
    comps = []
    for c in app.components:
        component = Component(**c)
        comps.append(component)
        component.func(component.props)
    with open("templates/"+template_name) as f:
        tmp = f.read()
    for component in comps:
        tmp = tmp.replace(f'<{component.name}>',component.resp)
    with open("react-src/"+template_name,"w+") as f:
        f.write(tmp)
    loader = FileSystemLoader('react-src')
    
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**ctx)
    


class ReactApp:    
    def __init__(self,server:t.Any or None=None):
        self.server = server
        self.components = []

    def get_app(self):
        app = ComponentProps(self.server)
        return app

    def component(self, **kwargs):
        """Represents a new Component"""
        def wrap(funct):
            name = kwargs.get("name",funct.__name__)
            pass_context = kwargs.get("pass_context",True)
            props = self.get_app()
            if pass_context:
                self.resp = funct(props)
            else:
                self.resp = funct()
            self.components.append({
                    'name':name,
                    'pass_ctx':pass_context,
                    'funct':funct,
                    'props':props,
                    'resp':self.resp
                })
            return self.resp

        return wrap 


class Component:
    def __init__(self,name,pass_ctx,funct,props,resp):
        self.name = name
        self.context_set = pass_ctx
        self.func = funct
        self.props = props
        self.resp = resp

    
class ComponentProps:
    def __init__(self,app) -> None:
        """Represents the properties of a component

        Args:
            app (Any)
        """
        self.app = app
    
    @property
    def initialized(self):
        return self.app is not None

    