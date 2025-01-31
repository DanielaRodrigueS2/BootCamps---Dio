from sqlalchemy import Integer
from FastAPi.Academia.API.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)