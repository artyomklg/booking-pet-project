from datetime import date

from sqlalchemy import Computed, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class BookingModel(Base):
    __tablename__ = "booking"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    date_from: Mapped[date] = mapped_column(Date)
    date_to: Mapped[date] = mapped_column(Date)
    price: Mapped[int]
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))

    user: Mapped["UserModel"] = relationship(back_populates="bookings")  # type: ignore
    room: Mapped["RoomModel"] = relationship(back_populates="bookings")  # type: ignore

    def __str__(self):
        return f"Booking #{self.id}"
