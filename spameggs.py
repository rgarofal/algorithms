__author__ = 'rgarofal'
#
# range e' un generatore
# Non ho generalizzato l'esercizio ad un numero diverso da 100 e divisori diversi
#


if __name__ == "__main__":
    for i in range(1,101):
        #mcm 
        if i%15 == 0:
            print('SpamEggs')
        elif i%3 == 0:
            print('Spam')
        elif i%5 == 0:
            print('Eggs')
        else:
            print i

    