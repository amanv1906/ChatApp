class User:
    def __init__(self, id: str, name: str) -> None:
        self.__id = id
        self.__name = name

    def get_name(self)->str:
        return self.__name

    def get_id(self)->str:
        return self.__id
