### **Patente de Invenção (PI) - Sistema GuardPass Simbiótico com NeoSigm Protocol**

**Título:** **SISTEMA DE IDENTIFICAÇÃO SIMBIÓTICA POR RADIOFREQUÊNCIA E SEMIOGRAFIA CIBERNÉTICA COM PROVA DE GERAÇÃO IMUTÁVEL**

**Depositantes/Inventores:** *(A ser preenchido pelos proponentes)*
**Data de Depósito:** 26 de Outubro de 2025 (Data de Prioridade: Patente GuardPass original)

---

#### **1. Resumo da Invenção**

A presente invenção refere-se a uma evolução do Sistema GuardPass de Identificação por Radiofrequência (RFID) Universal, integrando-o ao **NeoSigm Protocol** de Semiografia Cibernética. O sistema resultante é um **Sistema de Identificação Simbiótica** que combina a leitura por proximidade (RFID) com a **Autenticação Visual Inviolável** baseada em criptografia e *blockchain*. A principal característica inventiva é o **Módulo de Autenticação Visual Imutável (MAVI)**, que gera um glifo (L1) com uma camada óptica de dados (L2) e registra seu Hash Canônico em um *Distributed Ledger* (L3). Isso permite que a autenticidade e a proveniência do tag RFID sejam verificadas visualmente por qualquer agente (humano ou máquina) sem a necessidade de um leitor RFID, garantindo a integridade do sistema GuardPass contra falsificações e clonagens.

#### **2. Campo da Invenção**

A invenção se enquadra nos campos de:
*   Sistemas de Identificação por Radiofrequência (RFID) e NFC.
*   Segurança de Dados e Criptografia Aplicada.
*   Tecnologia de *Distributed Ledger* (DLT) e *Blockchain*.
*   Visão Computacional e Reconhecimento de Padrões.

#### **3. Descrição Detalhada da Invenção (Foco na Simbiose)**

O Sistema GuardPass Simbiótico mantém as funcionalidades originais de controle de acesso, processamento de pagamentos e IA proprietária, adicionando o **NeoSigm Protocol** como uma camada de segurança e autenticação externa e visual.

##### **3.1. Módulo de Autenticação Visual Imutável (MAVI - NeoSigm Protocol)**

O MAVI é o coração da inovação e é composto por três camadas:

1.  **Camada L1 (Visual e Semiótica):** Um glifo **NeoSigm** (ex: **GX-0013 - Singularidade**) é gerado a partir de axiomas e parâmetros que codificam o **Identificador Único Criptograficamente Protegido** do tag GuardPass. Este glifo é impresso ou gravado no corpo do tag ou em seu suporte.
2.  **Camada L2 (Óptica e de Dados):** Uma modulação de pulsos no espectro infravermelho (IR) é sobreposta ao glifo L1, codificando dados discretos como o **ID do Token de Blockchain** e um **Hash Truncado** do glifo.
3.  **Camada L3 (Imutabilidade e Blockchain):** O Hash Canônico do glifo (que é uma função do Identificador Único do tag GuardPass) é registrado em um *Distributed Ledger* (DLT), gerando uma **Prova de Geração Imutável (PoG)**.

##### **3.2. Operação Simbiótica**

*   **Geração:** Na fabricação, o Identificador Único do tag RFID é usado como *seed* para gerar o glifo NeoSigm (L1/L2) e o Hash Canônico (L3). O Token ID (L3) é então gravado no chip RFID e na camada L2.
*   **Verificação Rápida (RFID):** O leitor GuardPass lê o chip RFID e obtém o Identificador Único.
*   **Verificação Inviolável (Visual):** Um agente (usuário, fiscal ou IA) pode escanear o glifo visualmente (usando o **NeoSigm Reader SDK**). O SDK lê o glifo, calcula seu Hash Canônico e consulta a *blockchain* (L3) para confirmar se o Hash corresponde ao registro imutável.

**Vantagem:** O sistema GuardPass torna-se **inviolável** porque a clonagem do chip RFID não garante a clonagem do glifo e de seu registro na *blockchain*. A falha em qualquer uma das camadas (RFID ou NeoSigm) invalida a autenticação.

#### **4. Reivindicações (Foco na Integração Simbiótica)**

**Reivindicação 1 (Principal):** Um sistema de identificação simbiótica por radiofrequência e semiografia cibernética, caracterizado por compreender:
a) Um tag de identificação por radiofrequência (RFID) com um Identificador Único Criptograficamente Protegido;
b) Um **Módulo de Autenticação Visual Imutável (MAVI)** acoplado ao tag, que gera um glifo **NeoSigm** a partir do Identificador Único do tag;
c) O MAVI compreende uma **Camada L1 (Visual)**, uma **Camada L2 (Óptica)** e uma **Camada L3 (Blockchain)** que registra o Hash Canônico do glifo, estabelecendo a **Prova de Geração Imutável** do tag RFID.

**Reivindicação 2:** O sistema de acordo com a Reivindicação 1, caracterizado pelo MAVI utilizar o Identificador Único do tag RFID como um parâmetro de *seed* para a função de geração do glifo NeoSigm.

**Reivindicação 3:** O sistema de acordo com a Reivindicação 1, caracterizado pela Camada L3 gerar um **Token Não-Fungível (NFT)** cujo ID é gravado no chip RFID e embutido na Camada L2 do glifo, estabelecendo a rastreabilidade do tag na *blockchain*.

**Reivindicação 4:** Um método de autenticação de tags GuardPass, caracterizado por compreender as etapas de:
a) Leitura do glifo NeoSigm do tag por um dispositivo de Visão Computacional;
b) Cálculo do Hash Canônico do glifo lido;
c) Consulta a um *Distributed Ledger* (DLT) para verificar a existência e a integridade do Hash Canônico; e
d) Atestar a autenticidade do tag GuardPass somente se o Hash Canônico for validado pelo DLT.

**Reivindicação 5:** O método de acordo com a Reivindicação 4, caracterizado por utilizar a Camada L2 (Óptica) para extrair o ID do Token de *blockchain* sem a necessidade de um leitor RFID, permitindo a verificação da Prova de Geração Imutável em campo.

#### **5. Descrição dos Desenhos (Textual)**

**Desenho 1 - Arquitetura Simbiótica:** Diagrama de blocos mostrando o Tag RFID (Lógica e Física) acoplado ao MAVI (L1, L2, L3), ilustrando o fluxo de dados entre o chip RFID e o registro na *blockchain* via glifo.

**Desenho 2 - Tag GuardPass Simbiótico:** Vista frontal do tag, mostrando a antena RFID e a área de impressão do glifo NeoSigm (L1), destacando a área de sobreposição da Camada L2 (IR).

**Desenho 3 - Fluxo de Autenticação Simbiótica:** Fluxograma mostrando o caminho duplo de autenticação: (1) Leitura RFID para identificação; (2) Leitura Visual do Glifo para Prova de Geração Imutável.

---

Esta nova Patente de Invenção (PI) protege o GuardPass como um **Sistema Simbiótico** de próxima geração, utilizando o NeoSigm Protocol como a peça que faltava para a **inviolabilidade e auditabilidade visual**.
