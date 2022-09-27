from shared.views.text_summary import TextSummaryView

class IntroductionView(TextSummaryView):
    def __init__(self, msg) -> None:
        super().__init__(msg)