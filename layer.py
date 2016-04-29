from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.auth import YowAuthenticationProtocolLayer
from yowsup.layers import YowLayerEvent, EventCallback
from yowsup.layers.network import YowNetworkLayer
import sys
from yowsup.common import YowConstants
import datetime
import os
from yowsup.layers.protocol_receipts.protocolentities    import *
from yowsup.layers.protocol_groups.protocolentities      import *
from yowsup.layers.protocol_presence.protocolentities    import *
from yowsup.layers.protocol_messages.protocolentities    import *
from yowsup.layers.protocol_acks.protocolentities        import *
from yowsup.layers.protocol_ib.protocolentities          import *
from yowsup.layers.protocol_iq.protocolentities          import *
from yowsup.layers.protocol_contacts.protocolentities    import *
from yowsup.layers.protocol_chatstate.protocolentities   import *
from yowsup.layers.protocol_privacy.protocolentities     import *
from yowsup.layers.protocol_media.protocolentities       import *
from yowsup.layers.protocol_media.mediauploader import MediaUploader
from yowsup.layers.protocol_profiles.protocolentities    import *
from yowsup.common.tools import Jid
from yowsup.common.optionalmodules import PILOptionalModule, AxolotlOptionalModule
import subprocess
import threading
import logging
logging.basicConfig(level=logging.DEBUG)

class Robotinic(YowInterfaceLayer):


    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())


            command = messageProtocolEntity.getBody().split()
            phone = messageProtocolEntity.getFrom().split('@')

            txtmessage = None

            if (str.lower(command[0]) == "name"):
                txtmessage = "My name is Robotinic."
            elif (str.lower(command[0]) == "live"):
                txtmessage = "I still alive!"
                

            if txtmessage is not None:
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    txtmessage,
                    to = messageProtocolEntity.getFrom())
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
    

