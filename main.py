from services.chat_app_service import ChatAppService

if __name__ == "__main__":
    chat_app_service = ChatAppService()
    user1 = chat_app_service.create_user("U1", "Aman")
    user2 = chat_app_service.create_user("U2","Amit")
    user3 = chat_app_service.create_user("U3","Amsa")
    user4 = chat_app_service.create_user("U4","Amisdft")
    user5 = chat_app_service.create_user("U5","Amitasd")

    c1 = chat_app_service.create_conversation("c1","Hello How are you")
    c2 = chat_app_service.create_conversation("c2","Hello How are you")
    chat_app_service.send_direct_message_conversation("U1","U2",c1)
    chat_app_service.send_direct_message_conversation("U3","U2",c2)

    group1 = chat_app_service.create_group("G1","Friends")
    chat_app_service.add_members_in_group("G1","U1")
    chat_app_service.add_members_in_group("G1","U4")
    chat_app_service.add_members_in_group("G1","U5")

    c3 = chat_app_service.create_conversation("c3","Hello How are you all in group")
    chat_app_service.send_message_in_group("U1","G1",c3)
    print(chat_app_service.retrive_chats("U2"))


