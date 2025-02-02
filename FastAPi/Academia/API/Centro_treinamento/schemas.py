
from typing import Annotated

from pydantic import Field

from Academia.API.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    
    nome : Annotated[str, Field(description='Nome do centro treinamento', example='Scale', max_length=20)]
    endereco : Annotated[str, Field(description='endereco do local', example='endereco abacaxi', max_length=60)]
    proprietario : Annotated[str, Field(description='Nome do proprietario', example='Daniela', max_length=30)]
    