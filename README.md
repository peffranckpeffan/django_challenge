# Desafio Agriness

Para o construção do desafio optei por utilizar a linguagem Python, empregando os frameworks Django e Django Rest, como banco de dados usei o Postgres e empreguei o Docker para empacotar o programa. Esse foi o primeiro projeto no qual usei os frameworks mencionados, portanto certos aspectos podem não estar adequados a um ambiente de produção, mas acredito que com o tempo e mais prática, terei uma melhor compreensão e poderei aplica-los de uma forma mais adequada.

Quanto ao desenvolvimento, a parte em que mais desprendi tempo foi em compreender o processo de query no banco e a serialização dos dados. Nos demais aspectos técnicos só pude perceber em como o Django facilita diversas etapas do desenvolvimento para web. Quanto a estruturação do banco, tentei mante-la da forma mais simples possivel, desenvolvendo o necessário para a realização do desafio. Um aspecto em que refleti bastante é em onde colocar a regras e o acesso aos dados no sistema, ao final, acabei optando por adicionar uma camada "controller", onde esses dois pontos são trabalhados, assim deixando a camada view o mais simples possível. Fico aberto a sugestões quanto a essa questão. No final acabei não implementando nenhum teste automatizado no sistema, mas com certeza é uma aspecto pretendo desenvolver.

Durante a elaboração do projeto dois tópicos me deixaram com dúvidas, no ambiente da empresa, certamente elas levariam a uma conversa com o cliente para o esclarecimento das regras, assim evitando qualquer retrabalho. O primeiro diz respeito a multa pelo atraso, elas foram dadas em porcentagem e não ficou claro para mim em relação a que elas deveriam ser calculadas, optei então por calcular em cima do valor do empréstimo do livro, o qual fixei em 10 reais. Outro tópico fora a reserva do livro, no esquema que contrui para o banco de dados, uma reserva só pode ser feita indicando o cliente que deseja realiza-la, assim acabei alterando um pouco a url de acesso a funcionalidade.

Qualquer dúvida, fico a disposição.

## Pré-requisitos

- Docker: https://docs.docker.com/engine/install/
- Docker Compose: https://docs.docker.com/compose/install/

## Execução

Com as ferramentas instaladas, basta executar o comando (no Linux talvez seja necessário usar o sudo para executar os comandos docker) dentro do diretorio do projeto, para rodar a aplicação:
```bash
docker-compose up
```
A seguir executamos o comando migrate para realizar alterações nos modelos e o comando loaddata, para prover os dados iniciais ao sistema, também na raiz do projeto:
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py loaddata initial_data.json
```
Assim, já teremos a aplicação rodando e com dados para realizar as requisições.

As funcionalidades podem ser acessadas pelo browser de preferencia, através da url:
```bash
http://localhost:8000/api/<funcionalidade>/
```
No linux, também pode se usar o comando curl:
```bash
curl http://localhost:8000/api/<funcionalidade>/
```
Para listar todos os livros, temos:
```bash
curl http://localhost:8000/api/books/
```

No caso para realizar uma reserva, como mencionado, alterei um pouco a url, ficando:
```bash
http://localhost:8000/api/book/<id_do_livro>/reserve/client/<id_do_cliente>/
http://localhost:8000/api/book/1/reserve/client/2/
```

A listagem dos empréstimos ativos do cliente pode ser acessada:
```bash
http://localhost:8000/api/client/<id_do_cliente>/books/
http://localhost:8000/api/client/1/books/
```

Caso queira acessar o painel admin para alterar os dados ou cadastrar novos, basta executar o comando:
```bash
docker-compose exec web python manage.py createsuperuser
```