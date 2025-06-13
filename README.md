# House Furtune <img align="center" alt="wlady-java" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg"/> <img align="center" alt="wlady-java" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/php/php-original.svg"/> <img align="center" alt="wlady-java" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg"/> <img align="center" alt="wlady-java" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original-wordmark.svg"/> <img align="center" alt="wlady-java" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original-wordmark.svg" /> <img align="center" alt="wlady-java" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg" /> <img align="center" alt="wlady-java" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" />

⚠️ Aviso: Este projeto é apenas para fins de estudo e aprendizado. Nenhuma funcionalidade está vinculada a apostas reais ou transações financeiras com dinheiro real.

### Project 

![Descrição da imagem](./fundo.png)


A arquitetura visualizada ganha vida com a escolha de tecnologias robustas e adequadas para cada camada, promovendo uma integração harmônica entre performance, escalabilidade e segurança. No centro da operação, orquestrando a lógica intrincada do cassino, o Python e o JavaScript formam uma dupla de excelência — cada um assumindo papéis específicos para entregar uma experiência completa, responsiva e segura. Foi estrategicamente desenhada para promover segurança, desempenho e escalabilidade, utilizando uma abordagem moderna e modular. Nela Python, JavaScript, PHP e bancos de dados distribuídos trabalham em conjunto, integrados por uma API robusta. A arquitetura está sendo progressivamente transformada em microsserviços independentes, cada um com uma função clara e isolada, esta e apenas uma arquitetura.

Vivemos em uma era onde a experiência do usuário e a confiança na plataforma são tão valiosas quanto a diversão em si. Pensando nisso, o Cassino Castelo Fortune foi idealizado como um ambiente digital que vai além do convencional — um verdadeiro reino de possibilidades, onde cada detalhe foi cuidadosamente projetado para proporcionar não apenas entretenimento, mas também transparência, justiça e segurança.
Inspirado no games mas atuais, nossa proposta é construir uma plataforma digital com bases sólidas: infraestrutura escalável, tecnologia de ponta, integração segura de dados financeiros e uma experiência imersiva para jogadores de todo o mundo.
Este material visa descrever com clareza a visão por trás do projeto, a estrutura técnica que o sustenta e os diferenciais que fazem do Cassino Castelo Fortune uma aplicação de destaque em inovação no setor de jogos online.
Entre os pilares fundamentais que sustentam o Cassino Castelo Fortune destacam-se: infraestrutura escalável e resiliente capaz de suportar alto tráfego com desempenho e estabilidade garantindo disponibilidade contínua da plataforma, arquitetura baseada em microsserviços que permite maior modularidade manutenção simplificada e integração dinâmica entre os diversos sistemas e componentes, integração segura com carteiras digitais e sistemas financeiros internacionais aceitando moedas como Real Euro Dólar e criptomoedas como Bitcoin e Solana, sistema antifraude inteligente com monitoramento em tempo real de padrões suspeitos mitigação de ataques como DDoS e SQL Injection e alertas automatizados via email e Telegram para incidentes críticos, gamificação refinada com gráficos avançados trilha sonora temática e recursos visuais inspirados na estética medieval promovendo uma imersão sensorial completa,banco de dados altamente estruturado com registros criptografados logs auditáveis backups frequentes e segregação lógica de informações críticas. 

O Cassino Castelo Fortune nasce com a proposta de ir além do jogo, oferecendo uma experiência digital moderna, transparente e segura. Inspirado e impulsionado pelos avanços da tecnologia, buscamos construir um ambiente onde cada detalhe foi pensado para surpreender.
Convidamos você a conhecer os pilares que sustentam este projeto e os diferenciais que o tornam interessante e envolvente.

<p align="center">
  <img src="./assents/python.gif" alt="Demonstração do jogo" width="100">
</p>

![Descrição da imagem](./arq.png)

<p align="center">
  <img src="./assents/cassino.gif" width="100" alt="Jogo 1" style="margin-right: 10px;">
  <img src="./assents/níqueis.gif" width="100" alt="Jogo 2" style="margin-right: 10px;">
  <img src="./assents/espadas.gif" width="100" alt="Jogo 3">
</p>

A imagem a seguir revela os bastidores, construído sobre a poderosa base de microsserviços. Prepare-se para uma jornada visual através de seus componentes essenciais, desde o portão de entrada que recebe seus lances até os motores que impulsionam cada giro, cada carta e cada resultado. Essa intrincada rede de serviços independentes colabora para criar a magia do entretenimento digital, garantindo uma experiência de usuário impecável segura e resiliente. A arquitetura visualizada ganha vida com a escolha de tecnologias robustas e adequadas para cada camada. No coração do servidor, controlando a lógica intrincada do cassino, o Python emerge como uma linguagem poderosa e versátil. Sua sintaxe clara, vasta biblioteca e forte comunidade a tornam ideal para construir sistemas complexos e escaláveis.


🧠 Backend Inteligente com Python
No coração do servidor, o Python se destaca como uma linguagem poderosa e versátil. Sua sintaxe clara, bibliotecas maduras e comunidade ativa o tornam ideal para construir microsserviços escaláveis e de alta confiabilidade. Dentro desse ecossistema Python, duas ferramentas ganham protagonismo:

FastAPI: Responsável pela construção da API principal, é a ponte entre os diversos microsserviços e os clientes externos (web/mobile). Com base no ASGI, o FastAPI oferece suporte nativo a operações assíncronas, validação automática com Pydantic e documentação interativa. É a espinha dorsal de um ambiente dinâmico e altamente concorrente como o de um cassino online.

Flask: Escolhido estrategicamente para os "Game Services", como os módulos GME Service e CAINO, o Flask permite a construção modular e leve das regras de cada jogo. Sua flexibilidade e extensibilidade possibilitam que cada jogo tenha suas próprias particularidades implementadas de forma isolada e eficiente.

🚨ATENÇAO A PASTA SECURITY🚨

🛡️ Segurança como camada transversal
A pasta security/, presente como um serviço independente, cumpre uma função crítica: centralizar a lógica de segurança, proteção contra ataques e validação de integridade. Os códigos e mecanismos implementados nela — como detecção de anomalias, filtros contra SQL Injection, proteção contra DDoS e lógica de autorização — são compartilháveis e reutilizáveis entre os demais serviços. Essa abordagem garante segurança uniforme, facilitando a manutenção e evitando falhas isoladas.

⚙️ Gerenciamento de Servidores com PHP
Na camada de infraestrutura, entra em cena o PHP, aplicado especificamente no server-service. Sua função não está ligada diretamente à lógica de negócio, mas sim ao gerenciamento de servidores e configuração do ambiente de hospedagem. Entre suas responsabilidades estão:

Controle e roteamento interno entre serviços em execução;

Manipulação de variáveis de ambiente (quando necessário);

Integração com Apache/Nginx via XAMPP ou outro servidor local;

Diagnósticos de disponibilidade e comunicação entre os serviços;

Neste contexto, o PHP funciona como uma camada administrativa, atuando nos bastidores para manter o ecossistema de microsserviços organizado, monitorado e em pleno funcionamento.


💡 Frontend Responsivo com JavaScript
Do lado do cliente, o JavaScript entra em ação para oferecer uma interface interativa, fluida e em tempo real. Bibliotecas como React.js ou mesmo aplicações em Vanilla JS permitem ao usuário:

Realizar apostas;

Visualizar resultados em tempo real via WebSockets;

Receber feedback instantâneo do backend.

Essa camada comunica-se constantemente com a API Python, seja via REST, seja por conexões WebSocket, mantendo a experiência sincronizada com os dados reais processados no servidor.

🔄 Interação entre camadas
Usuário interage via JavaScript → ações como apostas, giros ou entradas em mesas.

JavaScript envia dados à API FastAPI (Python) → os dados são validados, registrados e processados.

Se necessário, a lógica de jogo (Flask) é ativada → determinando resultados com base nas regras do jogo.

Camada de segurança é ativada sempre que preciso → validando comportamento, tokens, e monitorando padrões de acesso.

Resposta volta ao frontend → com resultados renderizados dinamicamente para o usuário.

🗃️ Banco de Dados (em desenvolvimento)
Tecnologia: PostgreSQL🐘.

Funções:

Armazenamento de usuários, histórico de apostas, resultados de jogos e movimentações financeiras.

Integração via ORM (como SQLAlchemy).

Separado por microsserviço (ex: auth-db, bank-db, game-db) para manter isolamento de responsabilidades.

Considerações futuras:

Monitoramento de queries lentas.

Backup automatizado e replicação para garantir disponibilidade.

Integração com sistema de alertas para falhas ou tentativas de acesso indevido.







