from layer import Robotinic

from yowsup.layers                             import YowParallelLayer
from yowsup.layers.auth                        import YowCryptLayer, YowAuthenticationProtocolLayer
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.stanzaregulator             import YowStanzaRegulator
from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks               import YowAckProtocolLayer
from yowsup.stacks import YowStack
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.layers.axolotl                     import YowAxolotlLayer
from yowsup.env                                import YowsupEnv




CREDENTIALS = ("phone number here", "password here") # replace with your phone and password

if __name__ == "__main__":
    layers = (
        Robotinic,
        YowParallelLayer([YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer, YowAckProtocolLayer]),
        YowAxolotlLayer,
        YowCoderLayer,
        YowCryptLayer,
        YowStanzaRegulator,
        YowNetworkLayer
    )

    stack = YowStack(layers)
    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)  # setting credentials
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])  # whatsapp server address
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
    stack.setProp(YowCoderLayer.PROP_RESOURCE, YowsupEnv.getCurrent().getResource())  # info about us as WhatsApp client

    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))  # sending the connect signal

    stack.loop()  # this is the main program loop
