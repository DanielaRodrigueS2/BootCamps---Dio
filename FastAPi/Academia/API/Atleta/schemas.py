from pydantic import Field, PositiveFloat
from typing import Annotated
from Academia.API.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome : Annotated[str, Field(description='Nome da/do Atleta', example='Dani', max_length=70)]
    cpf : Annotated[str, Field(description='CPF da/do Atleta', example='12312312312', max_length=11)]
    idade : Annotated[int, Field(description='Idaded da/do Atleta', example=21)]
    peso : Annotated[PositiveFloat, Field(description='Peso da/do Atleta', example=60.5)]
    altura : Annotated[PositiveFloat, Field(description='Altura da/do Atleta', example=1.72)]
    genero : Annotated[str, Field(description='Genero da/do Atleta', example='Feminino', max_length=20)]