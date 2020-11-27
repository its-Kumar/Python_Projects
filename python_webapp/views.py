def render_template(template_name="index.html", context={}):
    html_str = ""
    with open("templates/" + template_name, "r") as f:
        html_str = f.read()
        html_str = html_str.format(**context)
    return html_str


def home(environ):
    context = {"name": "visiter"}
    return render_template(template_name="index.html", context=context)


def contact_us(environ):
    context = {}
    return render_template(template_name="contact.html", context=context)
