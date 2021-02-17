from padinfo.view_state.base import ViewStateBase


class ClosableEmbedViewState(ViewStateBase):
    def __init__(self, original_author_id, menu_type, raw_query,
                 color, view_type, **kwargs):
        super().__init__(original_author_id, menu_type, raw_query)
        self.color = color
        self.view_type = view_type
        self.kwargs = kwargs
