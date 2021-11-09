from datetime import datetime
import json

import pendulum
from sqlalchemy import TypeDecorator, Text, DateTime, Date, BigInteger, Numeric, Float
from sqlalchemy.dialects import mysql, sqlite


BigIntegerType = BigInteger()
BigIntegerType = BigIntegerType.with_variant(mysql.BIGINT(), 'mysql')
BigIntegerType = BigIntegerType.with_variant(sqlite.INTEGER(), 'sqlite')

NumericType = Numeric()
NumericType = NumericType.with_variant(Numeric(8, 2), 'mysql')
NumericType = NumericType.with_variant(Float(2), 'sqlite')


class Json(TypeDecorator):
    """Simple wrapper to serialize and unserialize json from text fields"""

    impl = Text

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        return json.loads(value)


class DateTime(TypeDecorator):
    impl = DateTime

    def process_bind_param(self, value, dialect):
        if value is None:
            return None

        return datetime(
            year=value.year,
            month=value.month,
            day=value.day,
            hour=value.hour,
            minute=value.minute,
            second=value.second
        )

    def process_result_value(self, value, dialect):
        if value is None:
            return None

        naive_date = pendulum.parse(str(value))

        return datetime(
            year=naive_date.year,
            month=naive_date.month,
            day=naive_date.day,
            hour=naive_date.hour,
            minute=naive_date.minute,
            second=naive_date.second,
            tzinfo=pendulum.local_timezone()
        )


class Date(TypeDecorator):
    impl = Date

    def process_bind_param(self, value, dialect):
        if value is None:
            return None

        return datetime(
            year=value.year,
            month=value.month,
            day=value.day,
        )

    def process_result_value(self, value, dialect):
        if value is None:
            return None

        naive_date = pendulum.parse(str(value))

        return datetime(
            year=naive_date.year,
            month=naive_date.month,
            day=naive_date.day,
            tzinfo=pendulum.local_timezone()
        )
