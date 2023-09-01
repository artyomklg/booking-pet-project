from sqlalchemy import JSON, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class HotelModel(Base):
    __tablename__ = "hotel"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    rooms: Mapped[list["RoomModel"]] = relationship(back_populates="hotel")  # type: ignore

    def __str__(self):
        return f"Отель {self.name} {self.location[:30]}"
