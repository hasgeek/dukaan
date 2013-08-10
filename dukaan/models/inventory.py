# -*- coding: utf-8 -*-

from . import db, BaseMixin, BaseNameMixin, BaseScopedNameMixin

__all__ = ['InventoryType', 'InventoryVariantAttribute', 'InventoryItem',
    'InventoryItemVariant', 'InventoryItemVariantAttribute']


class InventoryType(BaseNameMixin, db.Model):
    """
    Type of inventory (tshirt, sticker, etc)
    """
    __tablename__ = 'inventory_type'


class InventoryVariantAttribute(BaseScopedNameMixin, db.Model):
    """
    Describes an attribute for which there are variants within each item (size, colour, etc)
    """
    __tablename__ = 'inventory_variant_attribute'

    inventory_type_id = db.Column(None, db.ForeignKey('inventory_type.id'), nullable=False)
    inventory_type = db.relationship(InventoryType, backref=db.backref('variantattrs', cascade='all, delete-orphan'))
    parent = db.synonym('inventory_type')

    __table_args__ = (db.UniqueConstraint('name', 'inventory_type_id'),)


class InventoryItem(BaseScopedNameMixin, db.Model):
    """
    Describes an item for sale.
    """
    __tablename__ = 'inventory_item'

    inventory_type_id = db.Column(None, db.ForeignKey('inventory_type.id'), nullable=False)
    inventory_type = db.relationship(InventoryType, backref=db.backref('inventory', cascade='all, delete-orphan'))
    parent = db.synonym('inventory_type')

    __table_args__ = (db.UniqueConstraint('name', 'inventory_type_id'),)


class InventoryItemVariant(BaseMixin, db.Model):
    """
    Describes a single variant of an inventory item. There is always at least one variant of any item.
    """
    __tablename__ = 'inventory_item_variant'

    inventory_item_id = db.Column(None, db.ForeignKey('inventory_item.id'), nullable=False)
    inventory_item = db.relationship(InventoryItem, backref=db.backref('variants', cascade='all, delete-orphan'))
    parent = db.synonym('inventory_item')

    price = db.Column(db.Numeric, nullable=False)  # Price (in the default currency)
    stock = db.Column(db.Integer, nullable=False)  # Availability


class InventoryItemVariantAttribute(BaseMixin, db.Model):
    """
    Links a variant and variant attribute with a value.
    """
    __tablename__ = 'inventory_item_variant_attribute'

    attribute_id = db.Column(None, db.ForeignKey('inventory_variant_attribute.id'), nullable=False)
    attribute = db.relationship(InventoryVariantAttribute, backref=db.backref('variant_values', cascade='all, delete-orphan'))

    variant_id = db.Column(None, db.ForeignKey('inventory_item_variant.id'), nullable=False)
    variant = db.relationship(InventoryItemVariant,
       backref=db.backref('variant_attributes', cascade='all, delete-orphan'))

    value = db.Column(db.Unicode(250), nullable=False)

    __table_args__ = (db.UniqueConstraint('attribute_id', 'variant_id', 'value'),)
