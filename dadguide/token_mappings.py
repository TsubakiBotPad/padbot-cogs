from enum import Enum
from collections import defaultdict

COLOR_MAP = {0: ('r','red','fire'),
             1: ('b','blue','water'),
             2: ('g','green','wood'),
             3: ('l','light','yellow','white'),
             4: ('d','dark','purple','black'),
             6: ('x','none','null','nil')}

SERIES_MAP = {130: ('halloween', 'hw', 'h'),
              136: ('xmas', 'christmas'),
              125: ('summer', 'beach'),
              114: ('school', 'academy', 'gakuen'),
              139: ('new years', 'ny'),
              149: ('wedding', 'bride'),
              154: ('padr'),
              175: ('valentines', 'vday', 'v'),
              183: ('gh', 'gungho'),
              117: ('gh', 'gungho'),
              187: ('sam3', 'samurai3', 'samiii')}


class EvoTypes(Enum):
    BASE = 'base'
    EVO = 'evolved'
    UVO = 'ulimate'
    UUVO = 'super ultimate'
    TRANS = 'transform'
    AWOKEN = 'awoken'
    MEGA = 'mega awoken'
    REVO = 'reincarnated'
    SREVO = 'super reincarnated'
    PIXEL = 'pixel'
    EQUIP = 'equip'

EVO_PREFIX_MAP = {EvoTypes.BASE: ('base',),
                  EvoTypes.EVO: ('evo', 'evolved'),
                  EvoTypes.UVO: ('uvo', 'ult', 'ultimate', 'uevo'),
                  EvoTypes.UUVO: ('uuvo', 'uult', 'uultimate', 'uuevo'),
                  EvoTypes.TRANS: ('trans', 'transform', 'transformed'),
                  EvoTypes.AWOKEN: ('awo', 'a'),
                  EvoTypes.MEGA: ('mega', 'mawoken', 'mawo', 'ma'),
                  EvoTypes.REVO: ('revo',),
                  EvoTypes.SREVO: ('srevo', 'super', 'sr'),
                  EvoTypes.PIXEL: ('p', 'pixel', 'dot'),
                  EvoTypes.EQUIP: ('equip', 'assist')}


class MiscPrefixes(Enum):
    CHIBI = 'chibi'
    FARMABLE = 'farmable'

MISC_PREFIX_MAP = {MiscPrefixes.CHIBI: ('chibi', 'mini'),
                   MiscPrefixes.FARMABLE: ('farmable', 'nrem')}


TOKEN_REPLACEMENTS = defaultdict(tuple, {
    'tamadra': ('tama',),
    'evolution': ('evo',),
})