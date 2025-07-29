from dataclasses import dataclass


@dataclass
class APIProviderConfig: 
    name: str 
    api_key: str 
    base_url: str 
    rate_limit: int 
    timeout: int 
