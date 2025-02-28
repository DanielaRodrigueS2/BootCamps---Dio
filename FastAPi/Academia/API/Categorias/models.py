from sqlalchemy import Integer, String

from sqlalchemy.orm import Mapped, mapped_column, relationship

from Academia.API.Atleta.models import AtletaModel
from Academia.API.contrib.models import BaseModel


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome : Mapped[str] = mapped_column(String(70),unique=True, nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')