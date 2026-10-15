
from messages.message_receiver import APIMessageReceiver, MessageReceiver
from files.organizer import FileOrganizer, Organizer

class Orchestrator:
    def __init__(
        self, message_receiver: MessageReceiver = None, organizer: Organizer = None
    ):
        self.message_receiver = message_receiver or APIMessageReceiver()
        self.organizer = organizer or FileOrganizer()

    def execute(self, config: Any | None = None):
        messages = self.message_receiver.receive()
        self.organizer.organize(messages, config)
