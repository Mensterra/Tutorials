import sys
import types

class MockModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        

    def __getattr__(self, name):
       return None
    
sys.modules['chromadb'] = MockModule('chromadb')
sys.modules['karo.memory.service.chromadb_service'] = MockModule('karo.memory.service.chromadb_service')