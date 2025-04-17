# MailSender - Sistema de Envio Automatizado de E-mails com Integração ao Google Sheets

**Autor**: Pablo Víctor  
**Data**: Abril de 2025

---

## 1. **Visão Geral**

O **MailSender** é um sistema desenvolvido em Python para automação de envio de e-mails personalizados, integrado diretamente ao Google Sheets. Este sistema visa otimizar a comunicação interna de organizações, enviando e-mails personalizados com base em dados extraídos de uma planilha hospedada no Google Sheets. A solução foi projetada para facilitar o processo de envio de mensagens para os colaboradores de diferentes departamentos, oferecendo uma maneira eficiente e automatizada de comunicação.

---

## 2. **Objetivo**

O principal objetivo deste sistema é automatizar o envio de e-mails personalizados para os colaboradores de uma organização. Utilizando dados como nome, e-mail e departamento, que são extraídos de uma planilha do Google Sheets, o sistema envia e-mails personalizados para cada destinatário, garantindo que a comunicação seja eficiente e sem a necessidade de interação manual.

---

## 3. **Funcionalidades**

- **Autenticação OAuth2 com Google**: Autentica o acesso à API do Google Sheets usando o protocolo OAuth2.
- **Leitura de Dados do Google Sheets**: O sistema lê dados de uma planilha do Google Sheets, como nome, e-mail e departamento dos colaboradores.
- **Envio Personalizado de E-mails**: Monta e envia e-mails personalizados para cada colaborador com base nos dados da planilha.
- **Registro de Logs**: Mantém um log dos e-mails enviados, com informações sobre o sucesso ou falha de cada envio.
- **Integração SMTP**: Utiliza o protocolo SMTP para enviar os e-mails de maneira segura.

---

## 4. **Tecnologias Utilizadas**

- **Python 3.x**: Linguagem de programação principal utilizada.
- **Biblioteca smtplib**: Para envio de e-mails via protocolo SMTP.
- **Bibliotecas do Google**:
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-auth-httplib2`
  - `google-api-python-client`
- **Google Sheets API**: Para interação com planilhas Google.
- **Conta de e-mail Gmail**: Para o envio dos e-mails.

---

## 5. **Estrutura do Código**

### 5.1 **Bibliotecas Importadas**

O código utiliza diversas bibliotecas para autenticação com o Google, leitura de dados da planilha, envio de e-mails e manipulação de arquivos.

### 5.2 **Função `enviar_email`**

- **Parâmetros**:
  - `destinatario`: E-mail do colaborador.
  - `nome`: Nome do colaborador.
  - `departamento`: Departamento do colaborador.
- **Objetivo**: Enviar um e-mail personalizado para o colaborador. O sistema registra o status de cada envio (sucesso ou erro) em um arquivo de log.

### 5.3 **Função `main`**

- **Objetivo**: Gerencia a autenticação com a Google API, conecta-se à planilha do Google Sheets, recupera os dados e envia os e-mails para os destinatários. A função itera sobre os dados da planilha (ignorando a primeira linha, que é o cabeçalho) e chama a função `enviar_email` para cada linha válida.

### 5.4 **Execução do Script**

O sistema é iniciado pela execução da função `main` no final do script, que orquestra o fluxo completo de leitura da planilha e envio dos e-mails.

---

## 6. **Formato da Planilha Google Sheets**

A planilha do Google Sheets esta estruturada da seguinte forma:


| Nome do colaborador  | (Opcional) | Departamento | E-mail |
|----------------------|------------|--------------|--------|
| A                    | B          | C            | D      | 

A primeira linha da planilha deve ser um cabeçalho e será ignorada durante a execução do script.

---

## 7. **Considerações de Segurança**

É importante observar que o uso de senhas ou credenciais sensíveis diretamente no código não é recomendado. Para maior segurança, considere utilizar variáveis de ambiente ou arquivos `.env` para armazenar as credenciais de maneira segura.

---

## 8. **Como Usar**

### 8.1 **Pré-requisitos**

- **Python 3.x** instalado.
- **Conta no Google** com acesso ao Google Sheets e Gmail.
- **Bibliotecas do Google** instaladas. Você pode instalar as dependências com o seguinte comando:

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
