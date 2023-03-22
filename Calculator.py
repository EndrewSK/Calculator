def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('os')
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('time')
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('math')

from os import system
from time import sleep
import math

cmd = 'mode 75, 15'
system(cmd)

print ("\n\n\n\t\t","*"*39)
print ("\t\t *********** CALCULADORA 1.0 ***********")
print ("\t\t ************** DS NOT 23 **************")
print ("\t\t ************** by Endrew **************")
print ("\t\t","*"*39)

name = input ("\n\n\n\n\tQual seu nome?\t")

system('cls')

cmd = 'mode 75, 30'
system(cmd)

def welcome():
    print(f"\n\n\n\n\t  *** Eai {name}! Seja bem-vindo(a) a calculadora :) ***")
welcome()

def calculate():
    response = int (input ("\n\n\n\n\tQual operação deseja fazer?\n\n\t1 - Soma\n\n\t2 - Subtração\n\n\t3 - Multiplicação\n\n\t4 - Divisão\n\n\t5 - Porcentagem\n\n\t6 - Raiz Quadrada\n\n\t===> "))

    def counts():
        
        sleep(1)
        system('cls')
        
        if response == 1:
            
            try:
                n1 = float (input ("\n\n\tDigite um número:\t"))
                n2 = float (input ("\tDigite mais um número:\t"))
            except ValueError as err:
                print ("\n\n\n\tDigite um número válido!")
                return counts()
            
            print ("\n\n\n","*"*74)
            print (f"\n\t\t{n1} + {n2} = {n1 + n2}\n")
            print ("*"*74, "\n\n")
            
        elif response == 2:
            
            try:
                n1 = float (input ("\n\n\tDigite um número:\t"))
                n2 = float (input ("\tDigite mais um número:\t"))
            except ValueError as err:
                print ("\n\n\n\tDigite um número válido!")
                return counts()
            
            print ("\n\n\n","*"*74)
            print (f"\n\t\t{n1} - {n2} = {n1 - n2}\n")
            print ("*"*74, "\n\n")
            
        elif response == 3:
            
            try:
                n1 = float (input ("\n\n\tDigite um número:\t"))
                n2 = float (input ("\tDigite mais um número:\t"))
            except ValueError as err:
                print ("\n\n\n\tDigite um número válido!")
                return counts()
            
            print ("\n\n\n","*"*74)
            print (f"\n\t\t{n1} • {n2} = {n1 * n2}\n")
            print ("*"*74, "\n\n")
            
        elif response == 4:
            
            try:
                n1 = float (input ("\n\n\tDigite um número:\t"))
                n2 = float (input ("\tDigite mais um número:\t"))
            except ValueError as err:
                print ("\n\n\n\tDigite um número válido!")
                return counts()
                        
            if n2!=0:
                print ("\n\n\n","*"*74)
                print (f"\n\t\t{n1} / {n2} = {(n1 / n2):.2f}\n")
                print ("*"*74, "\n\n") 
            else:
                print ("\n\n\n\tNão é possível dividir um número por 0")
                
        elif response == 5:
            
            try:
                n1 = float (input ("\n\n\tDigite um número:\t"))
                n2 = float (input ("\tDigite mais um número:\t"))
            except ValueError as err:
                print ("\n\n\n\tDigite um número válido!")
                return counts()
            porcent = n1 / 100
            
            print ("\n\n\n","*"*74)
            print (f"\n\t\t{n1}% de {n2} = {(porcent * n2):.1f}\n")
            print ("*"*74, "\n\n")

        elif response == 6:
            
            try:
                n1 = float (input ("\n\n\tDigite um número:\t"))
            except ValueError as err:
                print ("\n\n\n\tDigite um número válido!")
                return counts()
            raiz = math.sqrt(n1)
            
            print ("\n\n\n","*"*74)
            print (f"\n\t\t√{n1} = {(raiz):.3f}\n")
            print ("*"*74, "\n\n")

        else:
            print("\n\n\n\n\tA operação que você escolheu não é válida!")
            sleep(2)
            system('cls')
            print(f"\n\n\n\n\t  *** Eai {name}! Seja bem-vindo(a) a calculadora :) ***")
            calculate()
        again()
    counts()
    
def again():
    calc_again = input("\n\tDigite sim ou nao\n\tQuer fazer outra conta?\n\n\t==>\t")

    if calc_again == "sim":
        sleep(1)
        system('cls')
        return calculate()
        
    elif calc_again == "nao":
        print("\n\tTudo bem então, até mais!")
        sleep (1.5)
        system ('cls')
    else:
        sleep(0.5)
        system('cls')
        print("\n\tDesculpe não entendi...")
        return again()
        
calculate()