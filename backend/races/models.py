import uuid
from datetime import date, datetime

from sqlalchemy import Column, Enum, ForeignKey, String, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from brands.models import Brand
from races.enums import RaceEditionStatus
from runiverse.common.models import Base

race_edition_distances = Table(
    "race_edition_distances",
    Base.metadata,
    Column("distance_id", UUID, ForeignKey("distances._id"), primary_key=True),
    Column(
        "race_edition_id",
        UUID,
        ForeignKey("race_editions._id"),
        primary_key=True,
    ),
)


class Distance(Base):
    __tablename__ = "distances"

    _id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    kilometers: Mapped[float]
    race_editions: Mapped[list["RaceEdition"]] = relationship(
        "RaceEdition",
        secondary=race_edition_distances,
        back_populates="distances",
    )


class Race(Base):
    __tablename__ = "races"

    _id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    full_name: Mapped[str] = mapped_column(String(100))
    fixed_date: Mapped[date | None] = mapped_column(nullable=True)
    editions: Mapped[list["RaceEdition"]] = relationship(back_populates="race")
    series_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("series._id"),
        nullable=True,
    )
    series: Mapped["Series"] = relationship(back_populates="races")


class Series(Base):
    __tablename__ = "series"

    _id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    name: Mapped[str] = mapped_column(String(100))
    races: Mapped[list["Race"]] = relationship(back_populates="series")
    editions: Mapped[list["SeriesEdition"]] = relationship(
        back_populates="series"
    )


class RaceEdition(Base):
    __tablename__ = "race_editions"

    _id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    race_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("races._id"),
    )
    race: Mapped["Race"] = relationship(
        back_populates="editions",
    )
    series_edition_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("series_editions._id"),
        nullable=True,
    )
    series_edition: Mapped["SeriesEdition"] = relationship(
        back_populates="race_editions",
    )
    year: Mapped[int]
    date_time: Mapped[datetime]
    location: Mapped[str] = mapped_column(String(256))
    sponsor_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("brands._id"),
        nullable=True,
    )
    sponsor: Mapped["Brand"] = relationship(
        back_populates="race_editions",
    )
    status: Mapped[RaceEditionStatus] = mapped_column(Enum(RaceEditionStatus))
    distances: Mapped[list["Distance"]] = relationship(
        "Distance",
        secondary=race_edition_distances,
        back_populates="race_editions",
    )


class SeriesEdition(Base):
    __tablename__ = "series_editions"

    _id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    series_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("series._id"),
    )
    series: Mapped["Series"] = relationship(
        back_populates="editions",
    )
    year: Mapped[int]
    race_editions: Mapped[list["RaceEdition"]] = relationship(
        back_populates="series_edition",
    )
