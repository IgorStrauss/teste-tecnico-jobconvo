## Teste técnico JobConvo 07-2023
Neste teste, será simulado uma página web onde uma empresa X tem 
a área para poder cadastrar, atualizar e deletar vagas. Teremos também
a área destinada aos candidatos, onde os mesmos poderão se inscrever
e se candidatarem às vagas mediante login.

### Start projeto
#### Make start
Com o comando 'Make start' a aplicação irá criar as migrações e inicializar o servidor django na porta 8000

Com o comando 'Make run' a aplicação será inicializada sem realizar migrações.

Tecnologias utilizadas:
 - Python3.8
 - Django4.2
 - Sqlite
 - Pytest
 - Poetry
 - HTML
 - CSS
 
Rota candidato:
    - Candidatos:
     - localhost/   -> Acesso para candidatos

 
Rota companhia: 
    - Companhia:
     - localhost:8000/company/17arcyiekk/marques/96a014o8n8/igor/2023/   -> Acesso para companhia

#### Módulo companhia
localhost:8000/company/17arcyiekk/marques/96a014o8n8/igor/2023/

    Acessar este link inicial, e sendo a primeira vez, como empresa administradora
    clicar em cadastrar.

    Após cadastro, fazer login para ser direcionado à tela onde renderiza as
    vagas com candidatos inscritos. Nesta tela podemos ver a quantidade de
    candidatos por vaga, acessar cada vaga individual, e em seguida, 
    temos a lista com todos os candidatos inscritos nesta vaga, tambem contando
    com link em cada usuário, para visualizar o perfil de cada um, assim como
    as suas expêriencias.

    Na tela principal, temos a barra de navegação com links para acessar as 
    funcionalidades da aplicação

    Para cadastrar uma vaga, primeiro temos que ter uma empresa cadastrada, 
    que sera a ofertante da vaga. Em seguida, basta acessar a empresa, e clicar
    em cadastrar vaga.

#### Módulo candidato
localhost:8000/

    Acessar este link inicial, e sendo a primeira vez, como candidato, clicar em
    cadastrar

    Após cadastro, realizar login utilizando email e senha. Na tela inicial já
    terá disponível todas as vagas que estão abertas, bastando clicar nelas, e
    em seguida clicar em se candidatar, selecionar escolaridade e pretensão
    salarial. Na barra de navegação ainda tem a opção para inserir as experiências.

