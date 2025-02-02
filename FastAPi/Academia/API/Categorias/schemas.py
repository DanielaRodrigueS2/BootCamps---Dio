
from typing import Annotated

from pydantic import Field

from Academia.API.contrib.schemas import BaseSchema


class Categorias(BaseSchema):
    
    
    nome : Annotated[str, Field(description='Categoria', example='Scale', max_length=70)]