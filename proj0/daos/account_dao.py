from abc import abstractmethod, ABC


class AccountDAO(ABC):

    @abstractmethod
    def create_account(self, account):
        pass

    @abstractmethod
    def get_account(self, account_id, client_id):
        pass

    @abstractmethod
    def all_accounts(self, client_id):
        pass

    @abstractmethod
    def update_account(self, change, client_id):
        pass

    @abstractmethod
    def delete_account(self, account_id, client_id):
        pass
