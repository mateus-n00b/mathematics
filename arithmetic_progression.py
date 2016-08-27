#!/usr/bin/python
'''
Simples script para ensino de Progressao Aritmetica

Mateus Sousa, Agosto 2016

Versao 1.0

Licenca GPL

TODO
Acrescentar mais operacoes, em suma, aumentar o escopo do programa.
 
'''
opt = raw_input("Escolha uma opcao:\n[1] Soma dos termos de uma PA finita\n[2] Encontrar o termo geral\n[3] Sair\n> ")

if opt == "1":
    PA = raw_input ("Insira os termos iniciais da PA separados por espacos: ")
    an = raw_input("Insira o n-esimo termo a ser somado: ")
    
    a1 = PA.split(' ')[0]
    a2 = PA.split(' ')[1]
    r  = int(a2) - int(a1)

    print "O termo geral e ",r
    print "Procurando valor de ",an
    n = (int(a1)+(int(an)-1)*r)
    print "O valor de ",an," e",n
    Sn = (((int(a1)+n)*int(an)/2))
    print "A soma dos termos e igual a ",Sn

elif opt == "2":
    PA = raw_input ("Insira os termos iniciais da PA separados por espacos: ")
    a1 = PA.split(' ')[0]
    a2 = PA.split(' ')[1]
    r  = int(a2) - int(a1)

    print "O termo geral e ",r
else:
    print "Entrada invalida! Saindo..."
