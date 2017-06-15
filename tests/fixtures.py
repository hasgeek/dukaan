# -*- coding: utf-8 -*-

from coaster.utils import buid
from dukaan.models import *


def make_fixtures():
    # Make a test user
    user = User(userid=buid(), username=u"test", fullname=u"Test")
    db.session.add(user)

    # Make some inventory

    # Add inventory types
    tshirt = InventoryType(title=u"T-shirt")
    sticker = InventoryType(title=u"Sticker")
    mug = InventoryType(title=u"Mug")
    db.session.add_all([tshirt, sticker, mug])

    # Add inventory variant attributes
    # T-shirts have two, mugs have one, stickers have none
    tshirt_size = InventoryVariantAttribute(inventory_type=tshirt, title=u"Size")
    tshirt_color = InventoryVariantAttribute(inventory_type=tshirt, title=u"Color")
    mug_color = InventoryVariantAttribute(inventory_type=mug, title=u"Color")
    db.session.add_all([tshirt_size, tshirt_color, mug_color])

    # Add some inventory
    metarefresh_tshirt = InventoryItem(inventory_type=tshirt, title=u"Meta Refresh 2013")
    fifthel_tshirt1 = InventoryItem(inventory_type=tshirt, title=u"The Fifth Elephant 2013 stacked elephants")
    fifthel_tshirt2 = InventoryItem(inventory_type=tshirt, title=u"The Fifth Elephant 2013 panel of elephants")
    fifthel_stickerpack = InventoryItem(inventory_type=sticker, title=u"The Fifth Elephant 2013 pack of stickers")
    jsfoo_mug = InventoryItem(inventory_type=mug, title=u"JSFoo 2013")
    db.session.add_all([metarefresh_tshirt, fifthel_tshirt1, fifthel_tshirt2, fifthel_stickerpack, jsfoo_mug])

    # Add variants for inventory

    size_chart = [u"S", u"M", u"L", u"XL", u"XXL", u"XXXL"]

    # Single colour, multiple sizes
    for size in size_chart:
        db.session.add(
            InventoryItemVariant(inventory_item=metarefresh_tshirt, price=400, stock=10,
                vattrs={tshirt_color: u"Black", tshirt_size: size}))

    # Two colours, multiple sizes
    for color in [u"Black", u"Blue"]:
        for size in size_chart:
            db.session.add(
                InventoryItemVariant(inventory_item=fifthel_tshirt1, price=400, stock=10,
                    vattrs={tshirt_color: color, tshirt_size: size}))

    # Multiple colours, multiple sizes, variable prices
    for color, price in [(u"Black", 400), (u"Blue", 400), (u"Green", 400), (u"Red", 400), (u"White", 350)]:
        for size in size_chart:
            db.session.add(
                InventoryItemVariant(inventory_item=fifthel_tshirt2, price=price, stock=10,
                    vattrs={tshirt_color: color, tshirt_size: size}))

    db.session.commit()
