
from typing import Annotated

from pydantic import Field
from FastAPi.Academia.API.contrib.schemas import BaseSchema


class Categorias(BaseSchema):
    nome : Annotated[str, Field(description='Categoria', examples='Scale', max_length=70)]