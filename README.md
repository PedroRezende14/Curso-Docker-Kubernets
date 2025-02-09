
### **1. Parar e deletar todos os contêineres**

- **Parar todos os contêineres em execução:** `docker stop $(docker ps -q)`
    
- **Deletar todos os contêineres:** `docker rm $(docker ps -aq)`
    
- **Deletar todas as imagens:** `docker rmi $(docker images -q) --force`
    
- **Deletar tudo, incluindo volumes:** `docker system prune -a --volumes -f`
    

---

### **Comandos básicos para containers**

- **Rodar um contêiner:**  
    `docker run nome_da_imagem`
    
- **Parar um contêiner:**  
    `docker stop id/nome_do_container`
    
- **Listar todos os contêineres (incluindo os que não estão rodando):**  
    `docker ps -a`
    
- **Listar apenas os contêineres que estão rodando:**  
    `docker ps`
    
- **Ver os logs de um contêiner:**  
    `docker logs id/nome_do_container`
    
- **Remover contêineres:**
    
    - Se o contêiner não estiver rodando:  
        `docker rm id/nome_do_container`
    - Forçar a remoção (mesmo que esteja rodando):  
        `docker rm -f id/nome_do_container`
- **Utilizar um contêiner com acesso interativo:**  
    `docker run -it nome_da_imagem`
    
- **Rodar uma aplicação sem ocupar o terminal:**  
    `docker run -d nome_da_imagem`
    
- **Rodar uma aplicação e mapear uma porta específica:**  
    `docker run -d -p numero_da_porta:80 nome_da_imagem`
    
- **Dar um nome personalizado ao contêiner:**  
    `docker run --name nome_personalizado nome_da_imagem`
    
- **Rodar um contêiner com o terminal interativo (quando o contêiner já está criado):**  
    `docker start -i nome_do_container`
    
- **Deletar o contêiner automaticamente após ele ser encerrado:**  
    `docker run --rm nome/id`
    
- **Analisar o contêiner:**  
    `docker top nome/id`
    
- **Visualizar como o contêiner está configurado:**  
    `docker inspect nome/id`
    
- **Ver o consumo de recursos dos contêineres:**  
    `docker stats`
    

---

### **Trabalhando com imagens e Dockerfile**

#### Estrutura básica de um **Dockerfile**:

dockerfile

Copiar código

`FROM imagem_base      # Imagem base da qual sua aplicação vai depender WORKDIR /app          # Diretório de trabalho no container EXPOSE 80             # Porta exposta pela aplicação COPY . .              # Copiar os arquivos da aplicação para o container`

#### Comandos para imagens:

1. **Construir a imagem:**  
    `docker build -t nome_da_imagem diretorio_da_imagem`
    
2. **Rodar uma imagem:**  
    `docker run nome_da_imagem`
    
3. **Fazer o download de uma imagem:**  
    `docker pull nome_da_imagem`
    
4. **Renomear uma imagem:**  
    `docker tag id_imagem novo_nome_da_imagem`
    
5. **Criar uma imagem com tag específica:**  
    `docker build -t nome_da_imagem:tag_da_imagem .`
    
6. **Deletar uma imagem:**
    
    - Caso a imagem não esteja em uso:  
        `docker rmi id/nome_imagem`
    - Forçar a remoção:  
        `docker rmi -f id/nome_imagem`
7. **Enviar uma imagem para o Docker Hub:**  
    `docker push nome_da_imagem`
    

---

### **Tipos de Volume**

- **Volumes Anônimos:** São criados automaticamente pelo Docker, com nomes aleatórios. Difíceis de organizar e reaproveitar.
- **Volumes Nomeados:** São criados com um nome específico, tornando mais fácil gerenciar e organizar os volumes.
- **Bind Mounts:** Permitem mapear um diretório ou arquivo da máquina local para dentro do contêiner. Útil para persistir dados na máquina host.

---

### **Comandos para Trabalhar com Volumes**

- **Criar um volume nomeado:** `docker volume create nome_do_volume`
    
- **Listar volumes:** `docker volume ls`
    
- **Inspecionar volume:** `docker volume inspect nome_do_volume`
    
- **Deletar um volume:** `docker volume rm nome_do_volume`
    
- **Rodar um contêiner com volume nomeado:** `docker run -v nome_do_volume:/caminho/no/container nome_da_imagem`
    
- **Rodar um contêiner com Bind Mount:** `docker run -v /caminho/na/maquina:/caminho/no/container nome_da_imagem`
  
### **Redes**

#### Tipos de redes (drivers):

- **bridge:** Rede padrão que permite a comunicação entre contêineres no mesmo host.
- **host:** Contêiner compartilha a pilha de rede do host, sem isolamento de rede.
- **macvlan:** Permite que contêineres tenham endereços MAC exclusivos na rede física.
- **none:** Desativa o acesso à rede para o contêiner.
- **plugin:** Permite usar drivers de rede personalizados desenvolvidos por terceiros.

#### **Comandos para Trabalhar com Volumes**

**Comando para listar as redes**
	`docker network ls`
	
**Comando para criar redes**
	`docker network create <nome>`
	**Para criar uma rede com um drive especifico** 
	`docker network create -d <drive> <nome da rede>

**Comando remover redes**
	`docker network rm <nome/id>`

**Comando p remover varias redes que não estão em execução **
	`docker network prune`
	

### **COMPOSE

para rodar um compose
`docker compose up'

para desligar o compose 
`docker compose down´
  
para rodar um compose sem ocupar o terminal e não ver os logs
`docker compose up -d'

### **Docker Swarm![[Pasted image 20250208175440.png]]

O Docker Swarm é uma ferramenta de orquestração de contêineres que permite gerenciar múltiplos nós Docker como um cluster.

**1. Inicializar um Swarm**

`docker swarm init`  
Cria um nó Swarm no host atual.

 **2. Adicionar nós ao cluster**

- **Gerar token para adicionar um nó como Worker:**  
    `docker swarm join-token worker`
    
- **Gerar token para adicionar um nó como Manager:**  
    `docker swarm join-token manager`
    
- **Ingressar um nó no cluster (substituir `<TOKEN>` e `<IP>`):**  
    `docker swarm join --token <TOKEN> <IP>:2377`
    

 **3. Listar os nós do cluster**

`docker node ls`

 **4. Remover um nó do cluster**

- **Remover o nó atual do Swarm:**  
    `docker swarm leave --force`
    
- **Remover um nó específico do cluster:**  
    `docker node rm <ID ou NOME_DO_NO>`
    

 **5. Criar e gerenciar serviços no Swarm**

- **Criar um serviço replicado:**  
    `docker service create --name meu_servico --replicas 3 -p 80:80 nginx`
    
- **Listar serviços ativos no Swarm:**  
    `docker service ls`
    
- **Ver detalhes de um serviço específico:**  
    `docker service ps meu_servico`
    
- **Atualizar o número de réplicas de um serviço:**  
    `docker service scale meu_servico=5`
    
- **Remover um serviço:**  
    `docker service rm meu_servico`
    

 **6. Stack no Docker Swarm**

- **Criar uma stack a partir de um arquivo `docker-compose.yml`:**  
    `docker stack deploy -c docker-compose.yml minha_stack`
    
- **Listar stacks em execução:**  
    `docker stack ls`
    
- **Ver serviços de uma stack específica:**  
    `docker stack services minha_stack`
    
- **Remover uma stack:**  
    `docker stack rm minha_stack`
    

 **7. Monitoramento do Swarm**

- **Ver logs de um serviço:**  
    `docker service logs -f meu_servico`
    
- **Monitorar o estado do cluster:**  
    `docker info`
    
- **Inspecionar um nó específico:**  
    `docker node inspect <ID ou NOME_DO_NO>`
    
 **8. Remover o Swarm**

`docker swarm leave --force`  
`docker swarm rm`