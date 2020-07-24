<<<<<<< HEAD
function validacao(){
    var imagem = document.getElementById('foto').value

    var email = document.getElementById('email').value
    var nome = document.getElementById('nome').value
    var username = document.getElementById('username').value

    var novoEmail = document.getElementById('novoEmail').value
    var confirmEmail = document.getElementById('confirmEmail').value

    var novaSenha = document.getElementById('novaSenha').value
    var confirmSenha = document.getElementById('confirmSenha').value

    var res = document.querySelector('div#res')

    var campo = ''
    var valor = ''
    var id = 1


    //validação do Novo Email
    if (novoEmail == confirmEmail){
        campo = 'email'
        valor = 'mcihael3108@gmail.com'
        updata(id,campo,valor)
        res.innerHTML = "Dados do cadastro atualizado"
    }else{
        res.innerHTML = "Verifique os valores digitados"
    }

    //Validação da Nova Senha
    if(novaSenha == confirmSenha){
        campo = 'senha'
        valor = novaSenha
        res.innerHTML = "Dados do cadastro atualizado"
    }else{
        res.innerHTML = "Verifique os valores digitados"
    }

    //Novo Nome
    if(nome){
        campo = 'nome'
        valor = nome
        res.innerHTML = "Dados do cadastro atualizado"
    }else{
        res.innerHTML = "Verifique os valores digitados"
    }

    //Novo Username
    if(username){
        campo = 'username'
        valor = username
        res.innerHTML = "Dados do cadastro atualizado"
    }else{
        res.innerHTML = "Verifique os valores digitados"
    }
        
}
    

    

function updata(id,campo,valor){
    //Importando a biblioteca
    const Sequelize = require('sequelize');

    //Conexãpo com o banco de dados.
    const sequelize = new Sequelize({
    host: 'localhost',
    database: 'postgres',
    username: 'postgres',
    password: '1112',
    dialect: 'postgres',
    port: 5432,
    logging: true
    });

    sequelize.query(`UPDATE usuarios SET ${campo}='${valor}' where id=${id}`),(err,res)=>{
        console.log(err,res)
        sequelize.end()
    }
}
