from db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Training(Base):
    __tablename__= "training"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    coach: Mapped[str] = mapped_column(String(50), nullable=False)
    capacity: Mapped[int] = mapped_column(nullable=False)
    registered_count: Mapped[int] = mapped_column(default= 0)
    price: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<Training(id={self.id})>"