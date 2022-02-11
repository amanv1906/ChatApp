
from models.group import Group
from models.user import User
from models.conversation import Conversation
from exceptions.user_already_found_exception import UserAlreadyFoundException
from exceptions.user_not_found_exception import UserNotFoundException
from enums.conv_type import ConvType


class ChatAppService:
    def __init__(self):
        self.__user_conversation_map = {}
        self.group_map = {}
        self.user_map = {}

    def create_user(self, id, name):
        if self.user_map.get(id) == None:
            user = User(id,name)
            self.user_map[id] = user
            return user
        raise UserAlreadyFoundException("User is already present in database")
    
    def create_group(self, id, name):
        group = Group(id, name)
        self.group_map[id] = []
        return group

    def create_conversation(self, id, text):
        conversation = Conversation(id, text)
        return conversation

    def send_direct_message_conversation(self, user_a: str, user_b: str, conv: Conversation, conv_type=ConvType.DIRECT_MESSAGE, group_id=""):
        if(not self.user_map.get(user_a) and not self.user_map.get(user_b)):
            raise UserNotFoundException("User Not Found in database")

        if not self.__user_conversation_map.get(user_b):
            self.__user_conversation_map[user_b] = []
        if conv_type == ConvType.DIRECT_MESSAGE:
            self.__user_conversation_map[user_b].append([ConvType.DIRECT_MESSAGE, conv, user_a])
        elif conv_type==ConvType.GROUP_MESSAGE:
            self.__user_conversation_map[user_b].append([ConvType.GROUP_MESSAGE, conv, user_a, group_id])

    def add_members_in_group(self, group_id, user_id):
        if(not self.group_map.get(group_id) or not self.user_map.get(user_id)):
            return False
        self.group_map.add(user)

    def send_message_in_group(self, user_id, group_id, conv):
        if(not self.group_map.get(group_id) or not self.user_map.get(user_id)):
            return False
        for member in group_map[group_id]:
            self.send_direct_message_conversation(user_id, member.get_id(),conv, ConvType.GROUP_MESSAGE)
        return True


    def retrive_chats(self, user_id: str):

        if(not self.__user_conversation_map.get(user_id)):
            return "No Conversations"

        ui_dict = {}
        ui_dict[ConvType.DIRECT_MESSAGE]  = ""
        ui_dict[ConvType.GROUP_MESSAGE]  = ""
        for conversation in self.__user_conversation_map[user_id]:
            if conversation[0]==ConvType.DIRECT_MESSAGE:
                ui_dict[conversation[0]] += f" {conversation[1].get_conv_text()} from user {self.user_map.get(conversation[2]).get_id()} \n"
        for conversation in self.__user_conversation_map[user_id]:
            if conversation[0]==ConvType.GROUP_MESSAGE:
                ui_dict[conversation[0]] += f" {conversation[1].get_conv_text()} from user {self.user_map.get(conversation[2]).get_id()} from group {conversation[3]} \n"

        ui_display_text = f"Direct Messages -> {ui_dict[ConvType.DIRECT_MESSAGE]}"
        return ui_display_text


    



        


    


    
