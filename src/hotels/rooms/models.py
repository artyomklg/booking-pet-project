from typing import Optional

from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class RoomModel(Base):
    __tablename__ = "room"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotel.id"))
    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    services: Mapped[list[str]] = mapped_column(JSON)
    quantity: Mapped[int]
    image_id: Mapped[int]

    hotel: Mapped["HotelModel"] = relationship(back_populates="rooms")  # type: ignore
    bookings: Mapped[list["BookingModel"]] = relationship(back_populates="room")  # type: ignore

    def __str__(self):
        return f"Номер {self.name}"
