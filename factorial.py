#!/usr/bin/python
import argparse

__author__ = 'rgarofal'
#
# versione ricorsiva
#
#

def fact(n):
    if n == 0:
        return 1
    else:
        #print 'Chiamata ricorsiva originale'
        return n*fact(n-1)

#
# versione con meomization
# Siccome potrebbe essere un numero altissimo si potrebbe andare in stack overflow
# per limitare la profondita' delle chiamate ricorsive si puo' usare la tecnica della
# meomizzazione cioe' memorizzare i risultati intermedi in una cache interna e usarli
# invece id invocare la funzione nel caso fosse riusata piu' volte.
#
# ATTENZIONE HO SEMPLIFICATO LA COSA
# Si puo' fare qualcosa di piu' raffinato andando a memorizzare in cache la signature della funzione e il valore
# computato in modo tale da applicare il decoratore a tutte le funzioni che richiedono la memoizzazione
#



def memoization(func):
    cache = dict()
    def func_memoiz(*args):
        if not args[0] in cache:
           #print "Chiamata funzione ricorsiva in memoizazione"
           cache[args[0]] = func(*args)
        #else:
            #print "Valore in cache"
        return cache[args[0]]
    return func_memoiz

#
# Usando il decoratore potevo evitare di ridefinire la fact
# e usare quella originale. l'ho fatto solo per tenere nello stesso modulo
# le due versioni e fare dei confronti sulle chiamate.
# L'effetto positivo e' se la stessa funzione venisse chiamata piu' volte
# con un numero crescente di N
#
# Quindi avrei potuto scrivere semplicemente
#
#@memoization
#def fact(n):
#     if n == 0:
#        return 1
#     else:
#        return n*fact_new(n-1)
#
# senza toccare la funzione originale
#


@memoization
def fact_new(n):
     if n == 0:
        return 1
     else:
        return n*fact_new(n-1)



if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument("N", help="calcola il fattoriale di un numero N",
                    type=int)
  args = parser.parse_args()

  print 'Chiamata classica fact ricorsiva'
  print fact(args.N)

  print 'Chiamata fact memoizata ricorsiva'
  print fact_new(args.N)

  print 'Chiamata classica fact ricorsiva su un N+1'
  print fact((args.N)+1)
  print 'Chiamata fact memoizata su un N+1'
  print fact_new((args.N)+1)

  print 'Chiamata classica fact ricorsiva su un N+2'
  print fact((args.N)+2)
  print 'Chiamata fact memoizata su un N+2'
  print fact_new((args.N)+2)

