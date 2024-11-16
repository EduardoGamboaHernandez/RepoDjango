from django import template
from ..repository import GetReadme
from django.conf import settings
import markdown
import git
import os

REPOS_DIR = getattr(settings, "REPOS_DIR", None)


register = template.Library()


@register.filter(name='commit_short')
def commit_short(hash):
    return hash[:7]


@register.filter(name='branch_date')
def branch_date(datetime_branch):
    day = datetime_branch.day
    months = [
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre"]

    month = months[datetime_branch.month-1]

    year = datetime_branch.year

    return f"{day} de {month} del {year}"


@register.inclusion_tag("repository/readme.html", takes_context=True)
def get_readme(context):
    content = "No hay nada para mostrar"
    try:
        path = os.path.join(REPOS_DIR, context["user"].username)
        readme = GetReadme(context["info"]["name"], path)
        readme_content = readme.get_readme(context["last_commit"]["hash"])
        content = markdown.markdown(readme_content)
    except git.exc.NoSuchPathError:
        print("repositorio no existe")
    except KeyError:
        print("README no existe")
    except ValueError:
        print("commit no existe")

    return {
        "readme": content,
    }
