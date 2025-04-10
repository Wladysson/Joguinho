# House Furtune <img align="center" alt="wlady-java" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg"/> <img align="center" alt="wlady-java" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/php/php-original.svg"/> <img align="center" alt="wlady-java" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg"/> <img align="center" alt="wlady-java" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original-wordmark.svg"/> <img align="center" alt="wlady-java" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original-wordmark.svg" /> <img align="center" alt="wlady-java" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg" /> <img align="center" alt="wlady-java" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" />

⚠️ Nota: Este projeto foi desenvolvido exclusivamente para fins de estudo. Seu objetivo é explorar arquiteturas modernas de software, boas práticas de desenvolvimento, segurança e integração de múltiplas tecnologias em um sistema modular. Nenhuma funcionalidade aqui descrita está ligada a operações com dinheiro real ou apostas legais.

### Project

A arquitetura visualizada ganha vida com a escolha de tecnologias robustas e adequadas para cada camada, promovendo uma integração harmônica entre performance, escalabilidade e segurança. No centro da operação, orquestrando a lógica intrincada do cassino, o Python e o JavaScript formam uma dupla de excelência — cada um assumindo papéis específicos para entregar uma experiência completa, responsiva e segura. Foi estrategicamente desenhada para promover segurança, desempenho e escalabilidade, utilizando uma abordagem moderna e modular. Nela Python, JavaScript, PHP e bancos de dados distribuídos trabalham em conjunto, integrados por uma API robusta. A arquitetura está sendo progressivamente transformada em microsserviços independentes, cada um com uma função clara e isolada, esta e apenas uma arquitetura.

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



