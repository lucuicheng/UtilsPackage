from jinja2 import Environment, PackageLoader


def template(name, nodule):
    env = Environment(loader=PackageLoader(nodule))
    return env.get_template(name + '.jinja2')
