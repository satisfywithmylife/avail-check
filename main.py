# -*- coding: utf-8 -*-
import json
import time

import requests
from eth_account import Account
from web3 import Web3
from eth_account.messages import encode_defunct
from loguru import logger

logger.remove()
logger.add('my.log', format='<g>{time:YYYY-MM-DD HH:mm:ss:SSS}</g> | <c>{level}</c> | <level>{message}</level>')
logger.add(sys.stdout, format='<g>{time:YYYY-MM-DD HH:mm:ss:SSS}</g> | <c>{level}</c> | <level>{message}</level>')

class Avail(obj):
    
    def __init__(self, seed: str) -> None:
        Account.enable_unaudited_hdwallet_features()
        seed = seed.strip()
        if ' ' in seed:
            self.account = Account.from_mnemonic(seed)
        else:
            self.account = Account.from_key(seed)
          
    def check(self):
        ts = time.time() 
        msg = f'''Greetings from Avail!

Sign this message to check your eligibility. This signature will not cost you any fees.

Timestamp: {ts}'''

        msghash = encode_defunct(text=msg)
        sign = self.account.sign_message(msghash)
        
        url = 'https://claim-api.availproject.org/check-rewards'
        sign = sign.signature.hex()
        payload = {
            'account': self.account.address,
            'signedMessage': sign,
            'timestamp': ts,
            'type': 'ETHEREUM'
        }
    
        res = requests.post(url=url, json=payload)
        logger.info(self.account.address + ' ' + res.text)
       
