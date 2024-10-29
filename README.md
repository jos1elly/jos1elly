programa {

//banco de informações
inteiro bag= 1, bcc= 1, bsn= 123, i
caracter voltar, deposito
real saldo = 1000, limite = 1500, total = limite + saldo, deposito, saque
real credito[1000], debito[1000]

  funcao vetor (){
  
  para(i=1; i<1000; i++){
    credito [i] = 0.0
  }
  para (i=1; i<1000; i++){
    debito [i] = 0.0

  }
  }


  funcao inicio(){


 inteiro ag, cc, sn
faca{

escreva("\nInforme o número da agência:\n")
leia (ag)
escreva ("\nInforme o número da conta:\n")
leia(cc)
escreva ("\nInforme a senha:\n")
leia(sn)
limpa()
}enquanto ( bag != ag ou bcc != cc ou bsn != sn)


menu()

  }





  funcao menu() {
    inteiro esc
    escreva("\nEscolha uma operação abaixo\n")
    escreva("\n1- Saldo   | 2- Extrato   | 3- Saque    |4- Depósito    | 5- Sair \n")
    escreva("\nOpção:")
    leia (esc)
    limpa(esc)
    
      escolha (esc){
    
    caso 1:
    saldo ()
    pare

    caso 2: 
    extrato ()
    pare

    caso 3:
    saque ()
    pare

    caso 4:
    deposito()
    pare

    caso 5:
    pare

    caso contrario: escreva ("Opção inválida, tente novamente!\n")



      }

  }

  funcao saldo(){
    faca {
    
  escreva("\nSALDO: \n", saldo)
  escreva("\nLIMITE:\n", limite)
  escreva("\nTOTAL:\n", total)
"\n"
  escreva("\ndeseja voltar ao menu principal s|n\n")
  leia(voltar)


  }
  enquanto (voltar != 's')
  menu()
  }

  funcao extrato(){
    faca {
      escreva(saldo + deposito,"\n\n")
      escreva("---------------------\n\n")


 escreva ("deseja voltar ao menu principal\n")
  leia(voltar)
 
    }
  enquanto (voltar != 's')
  menu()
  }
  

  funcao saque(){
    faca{

escreva("Qual valor voce deseja sacar?\n")
leia(saque)
escreva("------------------------\n")
escreva ("deseja voltar ao menu principal s|n\n")

leia(voltar)
  }
 
  enquanto (voltar != 's')
  menu()
  }
  
  funcao deposito (){

    faca{
      escreva("qual valor deseja depositar?\n")
      leia(deposito)
    
    para (inteiro i= 0; i < 1000; i++){
   se(credito[i] == 0){

    credito [i] = deposito
    pare
   }

    }

      escreva ("Deseja voltar ao menu principal s|n\n")
      leia(voltar)
  }
   
  enquanto (voltar != 's')
  menu()

  }

}


