from flask_sqlalchemy import SQLAlchemy
from decimal import Decimal
from sqlalchemy import Numeric

db = SQLAlchemy()

db.Model.registry.type_annotation_map.update({
    Decimal: Numeric(10, 2) # Decimal type for accuracy
})
