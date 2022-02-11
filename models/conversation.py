from enums.conv_type import ConvType


class Conversation:
    def __init__(self, id: str, text: str) -> None:
        self.__id = id
        self.__text = text

    def get_conv_text(self)-> str:
        return self.__text

    def get_conv_id(self)-> str:
        return self.__id
