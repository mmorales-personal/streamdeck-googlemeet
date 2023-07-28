from event_handlers.base_event_handler import EventHandler


class StopPresentingScreenEventHandler(EventHandler):
    """
    A Stream Deck button that stop presenting the screen.
    """

    STREAM_DECK_ACTION = "com.chrisregado.googlemeet.stoppresentingscreen"

    async def _key_up_handler(self, event: dict) -> None:
        leave = self._make_simple_sd_event("stopPresentingScreen")
        await self._browser_manager.send_to_clients(leave)
