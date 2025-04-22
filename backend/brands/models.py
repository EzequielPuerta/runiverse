import uuid

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from runiverse.common.models import Base


class Brand(Base):
    __tablename__ = "brands"

    _id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    name: Mapped[str] = mapped_column(String(30))
    race_editions: Mapped[list["RaceEdition"]] = relationship(  # noqa: F821
        back_populates="sponsor",
    )
