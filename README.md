# Vehicle Search

## Escolha o Idioma

- [Português](#em-português)
- [English](#in-english)

---

## Em Português

### Visão Geral

Este projeto é a implementação de um programa CLI utilizando protoclo MCP para buscar veículos com base em filtros definidos pelo usuário. Ele utiliza uma arquitetura hexagonal e foi desenvolvido seguindo os princípios de Clean Architecture, SOLID e Clean Code.
O objetivo deste projeto é oferecer uma ferramenta CLI (Interface de Linha de Comando) que permita ao usuário pesquisar veículos com base em vários filtros, como marca, modelo, ano, tipo de combustível, entre outros através de um chat bot. A arquitetura do sistema segue os princípios de **Clean Architecture** para garantir uma estrutura modular, flexível e escalável.

### Regras

- O sistema permite a busca de veículos utilizando filtros como: marca, modelo, ano, tipo de combustível, quilometragem, entre outros.
- O servidor recebe os filtros enviados pelo cliente, consulta o banco de dados e retorna os veículos que atendem aos critérios especificados.
- Caso não existam veículos correspondentes aos filtros fornecidos, o chat bot informará ao cliente que não foi encontrado nenhum veículo e, caso o cliente deseje o bot irá realiar uma nova coleta de filtros para realizar outra busca.
- Você pode realizar quantas pesquisas desejar. Para isso, quando perguntado pelo chat bot se deseja realizar uma nova pesquisa, responda com "Sim" ("S" também é aceito e interpretado como sim).

### Configuração

O programa é desenvolvido em Python. Existem duas formas de configurar o ambiente para executá-lo:

1. **Instalando Python**:
    - Acesse [aqui](https://www.python.org/downloads/) para baixar o Python e siga as instruções de instalação.
    - Abra o terminal na raíz do projeto e instale as dependências do projeto:
        ```bash
        pip install -r requirements.txt
        ```

2. **Usando Docker (recomendado)**:
    - Acesse [aqui](https://www.docker.com/products/docker-desktop/) para baixar o Docker e siga as instruções de instalação.
    - Abra o Docker e o mantenha rodando.

#### Configuração Adicional
##### Windows
O projeto possui Dockerfile para configurações e Makefile para executar os comandos Docker. Se você estiver utilizando **Mac Book**, o Makefile irá funcionar corretamente e você pode pular esta seção.

Para Windows, você deve baixar o [GNU Make for Windows](https://sourceforge.net/projects/gnuwin32/) ou executar diretamente os comandos docker de acordo com a necessidade.

###### build:
``docker build -t $(IMAGE_NAME) .``

###### rodar aplicação:
``docker run -it --rm --name $(CONTAINER_NAME) $(IMAGE_NAME)``

###### rodar testes:
``docker run -it --rm --name $(CONTAINER_NAME) $(IMAGE_NAME) pytest --cov``

*Escolha o nome que quiser para as variáveis de imagem e container docker*

***

### Execução

#### Sem Docker:
- Abra o terminal na raiz do projeto.
- Execute o comando:
    ```bash
    python main.py
    ```
- O chat bot iniciará uma conversa com você.
- Siga as instruções do bot para realizar quantas pesquisas quiser com filtros diferentes.
- Para encerrar, ao ser perguntado se deseja realizar uma nova pesquisa, basta escrever "Não" ou qualquer coisa diferente de "Sim".

#### Usando Docker (recomendado):
- Abra o terminal na raiz do projeto.
- Execute o comando:
    ```bash
    make build
    ```
    Isso irá criar a imagem Docker.
- Para rodar a aplicação, execute:
    ```bash
    make run
    ```
- O chat bot iniciará uma conversa com você.
- Siga as instruções do bot para realizar quantas pesquisas quiser com filtros diferentes.
- Para encerrar, ao ser perguntado se deseja realizar uma nova pesquisa, basta escrever "Não" ou qualquer coisa diferente de "Sim".

### Testes
Você pode visualizar os testes da unidade de testes e executá-los.

#### Sem Docker:
- No terminal, execute o comando:
    ```bash
    python -m pytest --cov
    ```

#### Usando Docker (recomendado):
- Execute o comando:
    ```bash
    make test
    ```

### Arquitetura

O projeto segue os princípios de **Clean Architecture** utilizando **Protocolo MCP**, promovendo uma estrutura modular e flexível que separa as responsabilidades e dependências, tornando mais fácil a inteligibilidade, manutenção do código e realização de testes. A arquitetura heagonal permite fácil integração com APIs e serviços externos e facilita a implementação de novas funcionalidades e atualizações.

#### Componentes

- **Entrypoint**: Responsável por processar a entrada de dados. Esse componente interage diretamente com o cliente, coletando dados do usuário e retornando a resposta e é a única camada acessível ao cliente.
- **Configuração**: Responsável por abrir seções de conexão com o banco de dados e criar as estruturas de dados consumidas pela aplicação.
- **Model**: Contém as representações dos objetos de entrada e saída. Esses objetos definem as estruturas de dados utilizadas no programa.
- **Repositório**: Responsável apenas por executar os comandos de persistência e coleta de dados através da injeção da seção aberta na classe.
- **Server**: Contém as regras de negócio. Esta camada encapsula a lógica central do sistema, de forma independente de tecnologias ou frameworks específicos e processa as solicitações do cliente através do chat bot.
- **Util**: Contém funções utilitárias compartilhadas, usadas por diferentes partes da aplicação para gerar dados de veículos e auxiliar na validadção dos dados de entrada do cliente, por exemplo.
- **Diretório de Testes**: Contém testes unitários e de integração para o projeto, garantindo a cobertura, a veracidade das funcionalidades e a consistência dos dados processados para todas as etapas desde a interação com o cliente até o processamento de dados.

#### Princípios da Clean Architecture Aplicados e MCP

- **Separação de Preocupações**: Cada componente tem uma responsabilidade distinta, o que facilita o desenvolvimento e testes independentes.
- **Regra de Dependência**: As dependências apontam para o interior, com componentes de alto nível dependendo de componentes de baixo nível. Isso garante que a lógica de negócios esteja independente de frameworks externos.
- **Testabilidade**: A estrutura modular facilita a escrita de testes isolados para componentes individuais, promovendo o desenvolvimento orientado a testes e garantindo a confiabilidade do sistema.
- **Flexibilidade e Escalabilidade**: A arquitetura permite a fácil modificação e extensão do sistema, possibilitando a adição de novas funcionalidades sem comprometer a integridade da aplicação.

#### Benefícios da Arquitetura Clean

- **Manutenibilidade**: A clara separação de responsabilidades e a definição de limites entre os componentes tornam o código mais fácil de entender e modificar.
- **Escalabilidade**: A estrutura modular permite a adição gradual de novas funcionalidades sem aumentar a complexidade do sistema.
- **Testabilidade**: A modularidade e a separação de responsabilidades facilitam testes abrangentes, ajudando a identificar bugs e regressões mais cedo.
- **Flexibilidade**: A arquitetura é adaptável a mudanças nos requisitos ou nas escolhas tecnológicas, garantindo que o sistema continue sendo viável a longo prazo.

---

## In English

## Overview

The objective of this project is to provide a CLI (Command Line Interface) tool that allows users to search for vehicles based on various filters such as brand, model, year, fuel type, and more through a chatbot. The system architecture follows **Clean Architecture** principles to ensure a modular, flexible, and scalable structure.

### Rules

- The system allows vehicle searches using filters such as brand, model, year, fuel type, mileage, and more.
- The server receives the filters sent by the client, queries the database, and returns the vehicles that meet the specified criteria.
- If no vehicles match the provided filters, the chatbot will inform the client that no vehicles were found. If the client wishes, the bot will collect new filters to perform another search.
-- You can perform as many searches as you want. To do this, when asked by the chat bot if you want to perform a new search, answer with "Yes" ("Y" is also accepted and interpreted as yes).

## Setup

The program is developed in Python. There are two ways to set up the environment to run it:

### 1. Installing Python

1. Download Python from [here](https://www.python.org/downloads/) and follow the installation instructions.
2. Open the terminal in the project root and install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Using Docker (Recommended)

1. Download Docker from [here](https://www.docker.com/products/docker-desktop/) and follow the installation instructions.
2. Open Docker and keep it running.

### Additional Setup
#### Windows
The project includes a Dockerfile for setup and a Makefile for executing Docker commands. If you are using **MacBook**, the Makefile will work correctly, and you can skip this section.

For Windows, you need to download [GNU Make for Windows](https://sourceforge.net/projects/gnuwin32/) or run the Docker commands manually as needed.

###### Build:
``docker build -t $(IMAGE_NAME) .``

###### Run the application:
``docker run -it --rm --name $(CONTAINER_NAME) $(IMAGE_NAME)``

###### Run tests:
``docker run -it --rm --name $(CONTAINER_NAME) $(IMAGE_NAME) pytest --cov``

*Choose any name for the Docker image and container variables.*

---

## Execution

### Without Docker:

- Open the terminal in the project root.
- Run the command:
   ```bash
   python main.py
   ```
- The chatbot will start a conversation with you.
- Follow the bot's instructions to perform as many searches as you want with different filters.
- To exit, when asked if you want to perform a new search, simply type "No" or anything other than "Yes."

### Using Docker (Recommended):

- Open the terminal in the project root.
- Run the command:
   ```bash
   make build
   ```
   This will create the Docker image.
- To run the application, execute:
   ```bash
   make run
   ```
- The chatbot will start a conversation with you.
- Follow the bot's instructions to perform as many searches as you want with different filters.
- To exit, when asked if you want to perform a new search, simply type "No" or anything other than "Yes."

## Tests

You can view the test cases and execute them.

### Without Docker:

- In the terminal, run the command:
   ```bash
   python -m pytest --cov
   ```

### Using Docker (Recommended):

- Run the command:
   ```bash
   make test
   ```

## Architecture

The project follows **Clean Architecture** principles using the **MCP Protocol**, promoting a modular and flexible structure that separates responsibilities and dependencies, making the code easier to understand, maintain, and test. The hexagonal architecture allows easy integration with APIs and external services, facilitating the implementation of new features and updates.

### Components

- **Entrypoint**: Responsible for processing data input. This component interacts directly with the client, collecting user data and returning responses. It is the only layer accessible to the client.
- **Configuration**: Responsible for opening database connection sessions and creating the data structures used by the application.
- **Model**: Contains representations of input and output objects. These objects define the data structures used in the program.
- **Repository**: Solely responsible for executing persistence commands and data retrieval by injecting the open session into the class.
- **Server**: Contains business rules. This layer encapsulates the system's core logic, independently of specific technologies or frameworks, and processes client requests via the chatbot.
- **Util**: Contains shared utility functions used across different parts of the application to generate vehicle data and assist in validating client input, for example.
- **Test Directory**: Contains unit and integration tests for the project, ensuring coverage, feature accuracy, and data consistency from client interaction to data processing.

### Applied Clean Architecture and MCP Principles

- **Separation of Concerns**: Each component has a distinct responsibility, making development and testing easier.
- **Dependency Rule**: Dependencies point inward, with high-level components depending on lower-level components. This ensures that business logic remains independent of external frameworks.
- **Testability**: The modular structure facilitates writing isolated tests for individual components, promoting test-driven development and ensuring system reliability.
- **Flexibility and Scalability**: The architecture allows for easy modifications and extensions, enabling the addition of new features without compromising application integrity.

### Benefits of Clean Architecture

- **Maintainability**: Clear separation of responsibilities and well-defined boundaries between components make the code easier to understand and modify.
- **Scalability**: The modular structure allows for the gradual addition of new features without increasing system complexity.
- **Testability**: Modularity and separation of concerns facilitate comprehensive testing, helping to identify bugs and regressions early.
- **Flexibility**: The architecture adapts to changing requirements or technology choices, ensuring the system remains viable in the long term.

---
