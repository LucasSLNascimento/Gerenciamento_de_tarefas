# Gerenciamento_de_tarefas
 
INSTALAÇÃO:

main.py: pip install Flask Flask-Login Flask-WTF Flask-SQLAlchemy

config.py: pip install Flask Flask-Login Flask-SQLAlchemy

criarbanco: pip install Flask-SQLAlchemy

forms: pip install Flask-WTF

models: pip install Flask-SQLAlchemy Flask-Login

USO:

Após realizar as instalações e criar e rodar "python criarbanco.py" para criar o banco execute "python main.py" para ter 
acesso ao sistema.

Registro e login (Tela inicial):
Caso não existam cadastros, clique em registrar para criação de um usuário. 
Caso já tenha um cadastro, clique em login. 

Dashboard (Tela principal):
No dashboard serão mostradas todas as tarefas de todos os usuários, separadas por Pendente, Em Andamento 
e Concluída.

Tarefas pessoais:
Localizada no canto superior direito, esta página tem o objetivo de mostrar, criar, editar e excluir tarefas.
    
    . Visualizar tarefas: Apenas as tarefas atribuídas ao usuário logado serão mostradas aqui, com um filtro para melhor
    organização. É possível escolher entre ver apenas as tarefas Pendentes, Em Andamento, Concluídas ou ver todas as 
    tarefas independente do status.
    
    . Criar tarefa: Para criação de uma nova tarefa, serão necessários o nome da tarefa, descrição, status e o responsável
    pela tarefa. O responsável pode ser qualquer usuário cadastrado no sistema.

    . Editar: Para edição da tarefa, serão solicitadas as mesmas informações da criação de uma nova tarefa.

    . Excluir: Exclui a tarefa do banco de dados.

Lougout: Desloga o usuário, retornando para a tela de login.


