class StopPresentingScreenEventHandler extends SDEventHandler {

  handleStreamDeckEvent = (message) => {
    if (message.event === "stopPresentingScreen") {
      this._stopPresentingScreen();
    }
  }

  _stopPresentingScreen = () => {
    const button = document.querySelector('[jsname="aK5XXd"]');
    if (!button) {
      throw new ControlsNotFoundError("No stop presenting screen button found!")
    }
    button.click();
  }

}
