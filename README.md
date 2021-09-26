# tcc-blender-addons

Instalando Addons:

1. Entre em https://www.blender.org/ e baixe o Blender (o installer Blender 2.93.3 ou mais atual) na seção Download para seu sistema operacional. Depois de baixar o Blender e descompactá-lo num local de sua preferência, entre na pasta descompactada e carregue o aplicativo Blender. Quando abrir a tela de apresentação do Blender, escolha na coluna New File a opção General.
2. Para carregar os Addons da pasta do Google Drive, copie os seguintes arquivos para uma pasta de sua preferência no seu computador: bouncing_ball.py, add_x_axis.py, add_y_axis.py, add_z_axis.py e add_base.py. São cinco arquivos .py.
3. Com o Blender aberto vá em Edit > Preferences. Na janela Blender Preferences clique no botão Install... Carregue um a um os arquivos copiados: bouncing_ball.py, add_x_axis.py, add_y_axis.py, add_z_axis.py e add_base.py e habilite a marcação (✓ check mark) de cada arquivo carregado.
4. Ainda na janela Blender Preferences você deve adicionar um outro Addon chamado Measureit, criado por Antonio Vazquez (antonioya) que permitirá visualizar marcações, setas, medidas etc. Para instalar esse Addon vá no campo de busca Search indicado pela lupa e digite: measureit. Certifique-se que a opção Community esteja habilitada em azul.
5.  Para ver os Addons como mostrado na figura abaixo, deixe desabilitado (cinza) os botões Official e Testing e deixe habilitada (em azul) apenas a opção Community. Habilite (check mark) a opção Enabled Add-ons Only para ver os Addons que estão instalados e habilitados. Se todos os Addons sublinhados por mim, em vermelho, da figura aparecerem na janela Blender Preferences, então a simulação deve funcionar. Se faltar algum, desligue a opção Enabled Add-ons Only para poder ver se você não esqueceu de habilitar algum, se for o caso, busque pelo nome AddBase, Add X Axis,  Add X Axis, etc.

6. Feche a janela  Blender Preferences e aperte a tecla N, isso fará aparecer uma  guia lateral à direita. Escolha a quarta aba de cima para baixo na lateral, a aba Simulação Física, e aperte o botão Simular. Irá abrir uma caixa minimizada com o título Bola Quicando. Clique na seta ao lado do título para expandir a caixa de pop-up. Aparecerá diversas opções. Para ver a trajetória da bola, vá na opção Tempo Final, escolha um tempo maior que zero, 1 ou 2 segundos, por exemplo. Você pode ir aumentando na seta da direita desse campo Tempo Final. Se por acaso a pop-up fechar automaticamente, aperte F9 para que ela apareça novamente. Nesse caso, o cursor do mouse deve permanecer na região da caixa pop-up para que ela não feche automaticamente. Se por acaso fechar a janela novamente, aperte F9 outra vez, ou, clique no botão Painel na aba lateral à direita da Simulação Física. A pop-up voltará aparecer e ela só irá voltar a desaparecer se você clicar num objeto da cena.
![alt text](https://github.com/jamesrtorres/tcc-blender-addons/blob/master/Images/screen01.png)
Menu propriedades.

7. Para ver os vetores, no menu Lançamento de Projétil, na aba da direita, clique no botão Régua para habilitar as anotações de medidas, setas de vetores, etc. No menu pop-up Bola Quicando habilite as opções Mostrar Vetores e Mostrar Anotações. Para mostrar distâncias habilite a opção Mostrar Distâncias. Os vetores e as distâncias são anotações, certifique-se que a opção Mostrar Anotações esteja ligada, se não aparecer as setas e as distâncias, aperte o botão Régua no menu lateral  Lançamento de Projétil até aparecer as anotações.

Screenshots:

![alt text](https://github.com/jamesrtorres/tcc-blender-addons/blob/master/Images/screen02.png)

Tela do blender com addon lançamento de projétil.

![alt text](https://github.com/jamesrtorres/tcc-blender-addons/blob/master/Images/screen03.png)

Tela do blender com menu do addon lançamento de projétil

Dicas de Blender:

1.  Para mover a perspectiva use o mouse:
 Aperte o botão do meio (pressione a roda do mouse, não gire ela) para girar a perspectiva. Aperte o botão do meio (pressione a roda do mouse, não gire ela) segurando a tecla Ctrl para fazer aproximação e afastamento  (Zoom in e out). Aperte o botão do meio (pressione a roda do mouse, não gire ela) segurando a tecla Shift para fazer movimentos laterais panorâmicos (Pan). Aperte Crtl + Alt + Q para ver 4 pontos de vistas diferentes ao mesmo tempo, aperte novamente  Crtl + Alt + Q para voltar para um único ponto de vista. Recomendo utilizar apenas um ponto de vista maximizado. Para se acostumar a alterar a perspectiva movendo e girando, tenha em mente que você deve fazer isso sempre apertando a “roda ou bola” do meio do mouse e o que você deve alternar é a tecla do teclado, isto é, se é Ctrl é para Zoom, se é Shift é para a Pan ou se não aperta nada no teclado é para girar a perspectiva. Se você for acidentalmente parar nas visões ortográficas (sem perspectiva) Top, Left, Bottom, Front etc. aperte o botão do meio do mouse para fazer girar a viewport. Para aprender a navegar na Viewport do Blender vá em View>Viewpoint ou explore o teclado numérico na tentativa e erro, Numpad 1, Numpad 3, Numpad 5, etc.
2. Para mover a Timeline observe a barra inferior do Blender. Procure um ícone pequeno retangular azul claro com um  número anotado (o quadro atual), clique nesse objeto e mova-o lateralmente, essa é a linha do tempo do Blender. Se você apertar o botão Play Animation, você observará esse ícone azul se mover. 
