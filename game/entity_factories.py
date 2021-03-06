import random

from game.components import ai, consumable
from game.entity import Actor, Item
from game import color
from game.render_order import RenderOrder
 
player = Actor(
    char="@",
    color=color.player,
    name="you",
    ai_cls=ai.Changeling,
    render_order=RenderOrder.PLAYER,
    description="That's you!"
)

NPC = Actor(
	color=color.npc,
	ai_cls=ai.DefaultNPC,
	render_order=RenderOrder.ACTOR,
	description="a foolish human"
)

rock = Item(
	color = color.grey,
	name='rock',
	usable=consumable.DamagingProjectile(damage=1),
	flavor='do not place in mouth'
)

item_factories = [rock]