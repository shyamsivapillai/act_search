from sqlalchemy import Column, Integer, Text, Index
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.dialects.postgresql
from sqlalchemy.sql import func

Base = declarative_base()


class Sections(Base):
    __tablename__ = "sections"
    id = Column(Integer(), primary_key=True, auto_increment=True)
    section_text = Column(Text(), nullable=True)
    section_text_clean = Column(Text(), nullable=True)
    est_section_num = Column(Integer(), nullable=True)
    act_id = Column(Integer(), nullable=False)

    __table_args__ = (
        Index(
            'ix_examples_tsv',
            func.to_tsvector('english', section_text),
            postgresql_using='gin'
            ),
        )

class Acts(Base):
    __tablename__ = "acts"
    id = Column(Integer(), primary_key=True, auto_increment=True, index=True)
    name = Column(Text(), nullable=True, index=True)
    blob = Column(Text(), nullable=True, index=True)
