#!/bin/bash
# fatora_tudp.sh Este programa executa a resolucao de uma equacao
# de segundo grau por meio da fatoracao. 
# Teste como entrada a equacao: x^2+10x+16=0. O resultado devera ser -8 e -2.
#
# Mateus-n00b, Setembro 2016
#
# Versao 1.0
#
#Licenca GPL
#
# TODO: Adicionar suporte a numeros negativos tanto na entrada como na descoberta de na e nb.
#-==========================================================================================

maior=0

read -p "Isira o termo a (ex: x^2)>> " a
read -p "Isira o termo b (ex: 10x ou -16x)>> " b
read -p "Isira o termo c (ex: 16)>> " c
echo  "Assumindo que $a+$b+$c = 0 " 
b=$(cut -d'x' -f1 <<< $b)

if [ $b -gt $c ]
then
    maior=$b
else
    maior=$c
fi

tam=$(wc -c <<< $maior)
while :
do
    na=$(cut -c $tam <<< $RANDOM)
    nb=$(cut -c $tam <<< $RANDOM)
    if [ $[$na+$nb] -eq $b -a $[$na*nb] -eq $c ]
    then
        xUm=$[ $d - $na]
        xDois=$[ $d - $nb]
        break
    fi
done
echo -e "Achei!!!\nX = $xUm\nX = $xDois"
