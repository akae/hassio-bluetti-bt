import logging
from ctypes import *

try:
    import bluetti_crypt
    CRYPT_AVAILABLE = True
except ImportError:
    CRYPT_AVAILABLE = False
    logging.warning("bluetti_crypt module not available - encryption features disabled")


_LOGGER = logging.getLogger(__name__)

class bleEncrypt:
    def __init__(self):
        self.cryptoClient = None
        self.enable = False
        # Force disable encryption for compatibility testing
        self.force_no_encryption = True
        if not CRYPT_AVAILABLE:
            _LOGGER.warning("Encryption module not available - all devices will use non-encrypted communication")

    def start(self, enable: bool = True):
        # Force non-encrypted mode for testing
        if self.force_no_encryption or not CRYPT_AVAILABLE:
            self.enable = False
            _LOGGER.info("Encryption forcibly disabled for compatibility testing")
            return
            
        self.cryptoClient = bluetti_crypt.BluettiCrypt()
        self.enable = enable
        software_version = self.cryptoClient.get_software_version()
        _LOGGER.info('Crypt module software version: ' + str(software_version))

    def encrypt_link(self, data: bytearray):
        if not CRYPT_AVAILABLE or not self.enable:
            return 4, bytearray()  # Return success status for non-encrypted devices
            
        _LOGGER.info(' encrypt link data: ' + data.hex())

        message, ret = self.cryptoClient.ble_crypt_link_handler(bytes(data))
        _LOGGER.info(' ble crypt link result: ' + str(ret) + ' message: ' + message.hex())
        return ret, message

    def send_message(self, data: bytearray):
        if not CRYPT_AVAILABLE or not self.enable:
            return len(data), data
            
        _LOGGER.info(f'send message: ' + data.hex())

        message = self.cryptoClient.encrypt_data(bytes(data))
        _LOGGER.info(f' send encrypt message: {message.hex()}')
        return len(message), message

    def message_handle(self, data: bytearray):
        if not CRYPT_AVAILABLE or not self.enable:
            return len(data), data
            
        message = self.cryptoClient.decrypt_data(bytes(data))
        _LOGGER.info('receive message: ' + message.hex())
        return len(message), message