from .bridge import BridgeResource
from .bridge_port import BridgePortResource
from .interface import InterfaceResource



RESOURCES_SET = dict(
    bridge=BridgeResource,
    bridge_port=BridgePortResource,
    interface=InterfaceResource,
)