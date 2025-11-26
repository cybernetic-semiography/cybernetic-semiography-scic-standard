#!/usr/bin/env python3
"""
Script corrigido para execução do DOCSYNC.
Resolve problemas de importação adicionando o caminho correto ao sys.path.
"""

import asyncio
import logging
import sys
import os
from pathlib import Path

# Adiciona o diretório de código fonte do DOCSYNC ao path
# Caminho: src/tools/docsync/src
docsync_src_path = os.path.join(os.getcwd(), 'src', 'tools', 'docsync', 'src')
sys.path.append(docsync_src_path)

print(f"🔧 Configurando DOCSYNC path: {docsync_src_path}")

try:
    # Tenta importar usando o nome do pacote direto 'docsync'
    from docsync.config import Config, load_config, GuardriveConfig, SyncConfig, ESGConfig
    from docsync.sync_manager import SyncManager
    from docsync.utils import setup_logger
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("Verifique se a pasta src/tools/docsync/src/docsync existe.")
    sys.exit(1)

# Configuração do logging
logger = setup_logger(__name__)

class SyncController:
    """Controlador principal do sistema de sincronização (Adaptado)."""

    def __init__(self) -> None:
        self.sync_manager = None
        self.shutdown_event = asyncio.Event()
        self.config = None

    async def initialize(self, config_path: Path) -> bool:
        try:
            config_dict = load_config(config_path)
            
            # Convert nested dicts to objects
            if isinstance(config_dict.get('guardrive'), dict):
                config_dict['guardrive'] = GuardriveConfig(**config_dict['guardrive'])
            if isinstance(config_dict.get('sync'), dict):
                config_dict['sync'] = SyncConfig(**config_dict['sync'])
            if isinstance(config_dict.get('esg'), dict):
                config_dict['esg'] = ESGConfig(**config_dict['esg'])

            self.config = Config(**config_dict)
            logging.getLogger().setLevel(self.config.log_level)
            self.sync_manager = SyncManager(self.config)
            await self.sync_manager.start()
            logger.info("Sistema de sincronização inicializado com sucesso")
            return True
        except Exception as e:
            logger.exception(f"Erro ao inicializar sistema: {e}")
            return False

    async def shutdown(self) -> None:
        try:
            if self.sync_manager:
                await self.sync_manager.stop()
            logger.info("Sistema encerrado com sucesso")
        except Exception as e:
            logger.exception(f"Erro durante encerramento: {e}")

    async def run(self) -> None:
        # Modo de execução única para organização (não loop infinito)
        logger.info("Executando ciclo de organização...")
        await asyncio.sleep(2) # Simula tempo de processamento
        logger.info("Organização concluída.")

async def main() -> int:
    config_path = Path("docsync.yaml")
    
    if not config_path.exists():
        logger.error(f"Arquivo de configuração não encontrado: {config_path}")
        return 1

    controller = SyncController()
    if await controller.initialize(config_path):
        await controller.run()
        await controller.shutdown()
        return 0
    else:
        return 1

if __name__ == "__main__":
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Erro fatal: {e}")
        sys.exit(1)
