from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class MethodEnum(enum.Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    COPY = "COPY"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    LINK = "LINK"
    UNLINK = "UNLINK"
    PURGE = "PURGE"
    LOCK = "LOCK"
    UNLOCK = "UNLOCK"
    PROPFIND = "PROPFIND"
    VIEW = "VIEW"

    @property
    def to_list(self):
        return [
            self.GET,
            self.POST,
            self.PUT,
            self.PATCH,
            self.DELETE,
            self.COPY,
            self.HEAD,
            self.OPTIONS,
            self.LINK,
            self.UNLINK,
            self.PURGE,
            self.LOCK,
            self.UNLOCK,
            self.PROPFIND,
            self.VIEW,
        ]


class Topic(db.Model):
    __tablename__ = "topics"

    id = Column(String(36), primary_key=True, index=True)
    user_id = Column(ForeignKey("users.id"), index=True, nullable=True)
    name = Column(String(191), nullable=False, index=True, unique=True)
    allow_anonymous = Column(Boolean(create_constraint=False), nullable=False, default=False)
    publish_url = Column(Text(), nullable=False)
    header = Column(types.Json(), nullable=True, default={})
    method = Column(Enum(MethodEnum), default=MethodEnum.POST, index=True)
    send_as_come = Column(Boolean(create_constraint=False), nullable=False, default=False)


class TopicMetric(db.Model):
    __tablename__ = "topics_metrics"

    id = Column(types.BigIntegerType, primary_key=True, autoincrement=True)
    topic_id = Column(ForeignKey("topics.id"), index=True)
    created_at = Column(types.DateTime(), default=pendulum.now)
    consumers = Column(BigInteger, default=0)
    messages = Column(BigInteger, default=0)
    unacked = Column(BigInteger, default=0)
