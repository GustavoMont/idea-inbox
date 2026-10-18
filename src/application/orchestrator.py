from abc import ABC

from files.organizer import FileOrganizer, Organizer
from messages.message_receiver import APIMessageReceiver, MessageReceiver


class Orchestrator:
    def __init__(
        self, message_receiver: MessageReceiver = None, organizer: Organizer = None
    ) -> None:
        self.message_receiver = message_receiver or APIMessageReceiver()
        self.organizer = organizer or FileOrganizer()

    def execute(self, config: ABC | None = None) -> None:
        messages = self.message_receiver.receive()
        self.organizer.organize(messages, config)
