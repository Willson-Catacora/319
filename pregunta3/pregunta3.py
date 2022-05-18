from pyswip import Prolog
prolog = Prolog()

prolog.assertz("padre(juan, julio)")
prolog.assertz("padre(juan, karmen)")
prolog.assertz("padre(julio, jose)")
prolog.assertz("padre(julio, maria)")
prolog.assertz("padre(alan, jesus)")
prolog.assertz("padre(alan, carla)")
prolog.assertz("madre(rosa, julio)") 
prolog.assertz("madre(rosa, karmen)")
prolog.assertz("madre(veronica, jose)")
prolog.assertz("madre(veronica, maria)")
prolog.assertz("madre(karmen, jesus)")
prolog.assertz("madre(karmen, carla)")
prolog.assertz("abuelos(X,Y,Z) :- (padre(A,Z); madre(A,Z)), (padre(X,A), madre(Y,A))")
prolog.assertz("nietos(X,Y,Z) :- (padre(A,X); madre(A,X)), (padre(Y,A), madre(Z,A))")
prolog.assertz("primos(X,Y) :- (padre(A1,X); madre(A1,X)),(padre(A2,Y); madre(A2,Y)),(padre(P,A1), padre(P,A2), madre(M,A1), madre(M,A2)), X\=Y, A1\=A2")


for elementos in prolog.query("abuelos(X, Y, Z)"):
	print(elementos["X"]," y ", elementos["Y"] ," son los abuelos de ",elementos["Z"])

print("\n")
for elementos in prolog.query("nietos(X, Y, Z)"):
	print(elementos["X"]," es nieto de ", elementos["Y"] ," y ",elementos["Z"])

print("\n")
for elementos in prolog.query("primos(X, Y)"):
	print(elementos["X"]," es primo de ", elementos["Y"])
