"""Welcome The User To Masonite."""
from ding.managers.DingManager import DingManager
from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller


class WelcomeController(Controller):
    """Controller For Welcoming The User."""

    def show(self, view: View, request: Request, ding_manager: DingManager):
        """Show the welcome page.

        Arguments:
            view {masonite.view.View} -- The Masonite view class.
            request {masonite.request.Request} -- The Masonite request class.

        Returns:
            masonite.view.View -- The Masonite view class.
        """
        dd(ding_manager.show_message('Testing package with manager, drivers and contracts.'))
        return view.render('welcome')
