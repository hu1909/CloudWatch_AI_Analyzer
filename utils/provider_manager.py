import os 
from dataclasses import dataclass
from typing import Dict, Optional
from data_model.ai_provider_config import APIProviderConfig

class AIProviderManager:
    def __init__(self):
        self.providers = {
            'openai': APIProviderConfig(
                name='OpenAI',
                api_key=os.getenv('OPEN_API_KEY'),
                base_url='https://api.openai.com/v1',
                rate_limit=3500,
                timeout=30
            ),
            'gemini': APIProviderConfig(
                name='Gemini',
                api_key=os.getenv('OPEN_API_KEY'),
                base_url='https://gemini.googleapis.com',
                rate_limit=2000,
                timeout=30
            )

        }
    
    def get_provider(self, provider_name:str) -> APIProviderConfig:
        if provider_name not in self.providers:
            raise ValueError(f"Provider {provider_name} not configured")
        provider = self.providers[provider_name]
        if not provider.api_key:
            raise ValueError(f"API key for {provider_name} is missing")
    
        return provider