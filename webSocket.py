#!/usr/bin/env python
# -*- coding: utf-8 -*-

from websocket_server import WebsocketServer

def new_client(client, server):
    server.send_message_to_all("New client has joined")

def send_msg_allclient(client, server, message):
    server.send_message_to_all("webSocket->" + message)

server = WebsocketServer(9999, host='localhost')
server.set_fn_new_client(new_client)
server.set_fn_message_received(send_msg_allclient)
server.run_forever()
