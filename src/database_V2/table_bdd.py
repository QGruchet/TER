from sqlalchemy import Column, String, ForeignKey, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Auteur(Base):
    __tablename__ = "t_auteur"

    nom = Column(String, primary_key=True)
    profession = Column(String)

    def __init__(self, nom, profession):
        self.nom = nom
        self.profession = profession

    # Relationship avec EcritPar
    parents_ecritpar = relationship("EcritPar", back_populates="child_ecritpar")


class Personnalite(Base):
    __tablename__ = "t_personnalite"

    nom = Column(String, primary_key=True)

    def __init__(self, nom):
        self.nom = nom

    # Relationship avec ParleDe
    parents_parlede = relationship("ParleDe", back_populates="child_parlede")


class Article(Base):
    __tablename__ = "t_article"

    URL = Column(String, primary_key=True)
    titre = Column(String, nullable=False, unique=True)
    date_creation = Column(Date, nullable=False)
    date_modification = Column(Date)
    etiquette = Column(String, nullable=True)
    correction = Column(String, nullable=False)

    # Foreign Key de source
    source = Column(String, ForeignKey('t_source.URL'))

    def __init__(self, url: str, titre: str, date_creation, date_modification, correction: str, etiquette: str,
                 source: str):
        self.URL = url
        self.titre = titre
        self.date_creation = date_creation
        self.date_modification = date_modification
        self.correction = correction
        self.etiquette = etiquette
        self.source = source

    # Relationship avec Source
    child_source = relationship("Source", back_populates="parent_source")

    # Relationship avec ParleDe
    child_parlede = relationship("ParleDe", back_populates="parent_parlede")

    # Relationship avec EcritPar
    child_ecritpar = relationship('EcritPar', back_populates="parent_ecritpar")

    # Relationship avec Contient
    child_contient = relationship('Contient', back_populates="parent_contient")

    # Relationship avec Refere
    child_refere = relationship('Refere', back_populates="parent_refere")

    # Relationships avec EnLien
    parent_enlien_article = relationship('EnLien', back_populates="child_enlien")
    child_enlien_article = relationship('EnLien', back_populates="parent_enlien")


class Source(Base):
    __tablename__ = "t_source"

    URL = Column(String, primary_key=True)
    nom = Column(String, nullable=False)

    def __init__(self, url: str, nom: str):
        self.URL = url
        self.nom = nom

    # Relationship avec Article
    parent_source = relationship("Article", back_populates="child_source")


class Contenu(Base):
    __tablename__ = "t_contenu"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    texte = Column(String, nullable=False)

    def __init__(self, id: int, texte: str):
        self.ID = id
        self.texte = texte

    # Relationship avec Contient
    parent_contient = relationship('Contient', back_populates="child_contient")


class Reference(Base):
    __tablename__ = "t_reference"

    URL = Column(String, primary_key=True)
    nom = Column(String, nullable=False)

    def __init__(self, url: str, nom: str):
        self.URL = url
        self.nom = nom

    # Relationship avec refere
    parent_refere = relationship('Refere', back_populates="child_refere")


class ParleDe(Base):
    __tablename__ = "t_parlede"

    # Foreign Key de Article
    URL = Column(ForeignKey('t_article.URL'), primary_key=True)

    # Foreign Key de Personnalite
    nom = Column(ForeignKey('t_personnalite.nom'), primary_key=True)

    # Relationship avec Article
    parent_parlede = relationship("Article", back_populates="child_parlede")

    # Relationship avec Personnalite
    child_parlede = relationship("Personnalite", back_populates="parent_parlede")

    def __init__(self, url: str, nom: str):
        self.URL = url
        self.nom = nom


class EcritPar(Base):
    __tablename__ = "t_ecritpar"

    # Foreign Key de Article
    URL = Column(ForeignKey('t_article.URL'), primary_key=True)

    # Foreign Key de Auteur
    nom = Column(ForeignKey('t_auteur.nom'), primary_key=True)

    # Relationship avec Article
    parent_ecritpar = relationship('Article', back_populates="child_ecritpar")

    # Relationship avec Auteur
    child_parlede = relationship('Auteur', back_populates="parent_ecritpar")

    def __init__(self, url: str, nom: str):
        self.URL = url
        self.nom = nom


class Contient(Base):
    __tablename__ = "t_contient"

    # Foreign Key de Article
    URL = Column(ForeignKey('t_article.URl'), primary_key=True)

    # Foreign Key de Contenue
    ID = Column(ForeignKey('t_contenu.ID'), primary_key=True)

    # Relationship avec Article
    parent_contient = relationship('Article', back_populates="child_contient")

    # Relationship avec Contenue
    child_contient = relationship('Contenu', back_populates="parent_contient")

    def __init__(self, url: str, id: int):
        self.URL = url
        self.ID = id


class Refere(Base):
    __tablename__ = "t_refere"

    # Foreign Key de Article
    URL_article = Column(ForeignKey('t_article.URL'), primary_key=True)

    # Foreign Key de Reference
    URL_reference = Column(ForeignKey('t_reference.URL'), primary_key=True)

    # Relationship avec Article
    parent_refere = relationship('Article', back_populates="child_refere")

    # Relationship avec Reference
    child_refere = relationship('Reference', back_populates="parent_refere")

    def __init__(self, url_article: str, url_reference: str):
        self.URL_article = url_article
        self.URL_reference = url_reference


class EnLien(Base):
    __tablename__ = "t_enlien"

    # Foreign Key de Article
    URL_article1 = Column(ForeignKey('t_article.URL'), primary_key=True)

    # Foreign Key de Article
    URL_article2 = Column(ForeignKey('t_article.URL'), primary_key=True)

    # Relationship avec Article 1
    parent_enlien = relationship('Article', back_populates="child_enlien_article")

    # Relationship avec Article 2
    child_enlien = relationship('Article', back_populates="parent_enlien_article")

    def __init__(self, url1: str, url2: str):
        self.URL_article1 = url1
        self.URL_article2 = url2
