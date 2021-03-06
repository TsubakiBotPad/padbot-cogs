from typing import TYPE_CHECKING, List

from discordmenu.embed.base import Box
from discordmenu.embed.components import EmbedMain, EmbedField
from discordmenu.embed.view import EmbedView
from tsutils import char_to_emoji, embed_footer_with_state

from padinfo.common.config import UserConfig
from padinfo.view.components.monster.header import MonsterHeader
from padinfo.view.components.view_state_base import ViewStateBase

if TYPE_CHECKING:
    from dadguide.models.monster_model import MonsterModel


class MonsterListViewState(ViewStateBase):
    def __init__(self, original_author_id, menu_type, raw_query, query, color,
                 monster_list: List["MonsterModel"], title, message,
                 reaction_list=None,
                 extra_state=None,
                 child_message_id=None
                 ):
        super().__init__(original_author_id, menu_type, raw_query,
                         extra_state=extra_state)
        self.message = message
        self.child_message_id = child_message_id
        self.title = title
        self.monster_list = monster_list
        self.reaction_list = reaction_list
        self.color = color
        self.query = query

    def serialize(self):
        ret = super().serialize()
        ret.update({
            'pane_type': MonsterListView.VIEW_TYPE,
            'title': self.title,
            'monster_list': [str(m.monster_no) for m in self.monster_list],
            'reaction_list': self.reaction_list,
            'child_message_id': self.child_message_id,
            'message': self.message,
        })
        return ret

    @staticmethod
    async def deserialize(dgcog, user_config: UserConfig, ims: dict):
        if ims.get('unsupported_transition'):
            return None
        monster_list = [dgcog.database.graph.get_monster(int(m)) for m in ims['monster_list']]
        title = ims['title']

        raw_query = ims['raw_query']
        query = ims.get('query') or raw_query
        original_author_id = ims['original_author_id']
        menu_type = ims['menu_type']
        reaction_list = ims.get('reaction_list')
        child_message_id = ims.get('child_message_id')
        message = ims.get('message')

        return MonsterListViewState(original_author_id, menu_type, raw_query, query, user_config.color,
                                    monster_list, title, message,
                                    reaction_list=reaction_list,
                                    extra_state=ims,
                                    child_message_id=child_message_id
                                    )


def _monster_list(monsters):
    if not len(monsters):
        return []
    return [
        MonsterHeader.short_with_emoji(mon, link=True, prefix=char_to_emoji(i))
        for i, mon in enumerate(monsters)
    ]


class MonsterListView:
    VIEW_TYPE = 'MonsterList'

    @staticmethod
    def embed(state: MonsterListViewState):
        fields = [
            EmbedField(state.title,
                       Box(*_monster_list(state.monster_list)))
        ]

        return EmbedView(
            EmbedMain(
                color=state.color,
            ),
            embed_footer=embed_footer_with_state(state),
            embed_fields=fields)
