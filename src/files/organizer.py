from abc import ABC, abstractmethod

class Organizer(ABC):
    @abstractmethod
    def organize(self, messages: list[Any], config: Any):
        pass

class FileOrganizer(Organizer):
    def organize(self, messages: list[Any], config: Any):
        print('Organizer: ', '-'*19)
        print("1. Receive all messages")
        # ---
        print("2. Create a backup for choosen path")
        # ---
        print("3. Organize new ideas and notes")
        print('-'*30)

