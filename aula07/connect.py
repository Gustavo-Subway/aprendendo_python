# Importar o modulo de mysql  "pip install mysql-connector-python"

import mysql.connector

connection = mysql.connector.connect(host='localhost',database='db_nota',user='root',password='root')

#verificação de conexão

# if connect.is_connected():
#     db_info = connect.get_server_info()
#     print('Conectado no servidor msql ', db_info)

#     #Criando cursor para  manipular o banco de dados
#     cursor = connect.cursor()
#     cursor.execute('select database();')
#     linha = cursor.fetchone()
#     print('Connectado ao banco de dados ', linha)

create_table = """create table tb_cliente(
                    nr_cnpj char(14) primary key,
                    nm_razao_social varchar(30) not null,
                    nm_pais varchar(20),
                    nm_email varchar(40) not null
                );
               """
cursor = connection.cursor()
cursor.execute(create_table)
print('tabela criada com sucesso')

create_table = """create table tb_produto(
	    cd_produto int primary key auto_increment,
        nm_produto varchar(25) not null,
        vl_unitario decimal(5,2) not null
        );
        """