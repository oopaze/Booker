var frases = ["A leitura é uma fonte inesgotável de prazer mas por incrível que pareça, a quase totalidade, não sente esta sede.", 
			  "A leitura de todos os bons livros é uma conversação com as mais honestas pessoas dos séculos passados.",  
			  "A leitura de um bom livro é um diálogo incessante: o livro fala e a alma responde.", 
			  "Qual Ioga, qual nada! A melhor ginástica respiratória que existe é a leitura, em voz alta, dos Lusíadas.", 
			  "A leitura traz ao homem plenitude; o discurso, segurança; e a escrita, precisão.", 
			  "Muitos homens iniciaram uma nova era na sua vida a partir da leitura de um livro.", 
			  "A leitura é para o intelecto o que o exercício é para o corpo.", 
			  "Às vezes a leitura é um modo engenhoso de evitar o pensamento.", 
			  "A paixão da leitura é a mais inocente, aprazível e a menos dispendiosa.", 
			  "Leitura, antes de mais nada é estímulo, é exemplo."];

var p_mensagem = document.getElementById('mensagem')
function showmessage(){
    frase = Math.floor(Math.random()*10);
	p_mensagem.innerHTML = "" + frases[frase];
};

