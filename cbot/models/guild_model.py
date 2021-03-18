from typing import Union, Optional

from sqlalchemy import BigInteger, String
from sqlalchemy.testing.schema import Column

from database.database import db
from lang.translations import Translations


class GuildModel(db.Base):
    __tablename__ = "guilds"

    guild_id: Union[Column, int] = Column(BigInteger, primary_key=True)
    language: Union[Column, str] = Column(String(64))

    @staticmethod
    def create(guild_id: int, language: str = "en") -> "GuildModel":
        row = GuildModel(
            guild_id=guild_id,
            language=language
        )
        db.add(row)
        return row

    @staticmethod
    def get(guild_id: int) -> Optional["GuildModel"]:
        return db.first(GuildModel, guild_id=guild_id)

    @property
    def translation(self):
        return Translations(lang=self.language)
