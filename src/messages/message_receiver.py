from abc import ABC, abstractmethod

class MessageReceiver(ABC):
    @abstractmethod
    def receive(self) -> list[Any]:
        pass


class APIMessageReceiver(MessageReceiver):
    def receive(self) -> list[Any]:
        print("Receiver: ", '-'*20)
        # 1. Fetch the choosen API to get all messages
        print("Fecth chat API")
        # 2. Fetch the choosen API to get all messages
        print("Format the messages to a known format")
        print('-'*30)
        return []