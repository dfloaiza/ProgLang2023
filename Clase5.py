def mult(n):
    return n*2

def esPrimo(n):
    for i in range(2,n):
        if n%i == 0:
            return False        
    return True

def filterData_Genero(dic):
    return dic["genero"] == "rock"

enteros = list(range(2,101))
#print(enteros)

mult_x_3 = lambda y: y*3 #!!!!!!

primos_100 = list(filter(esPrimo, enteros))
#print(primos_100)
primos_x_2 = list(map(mult, primos_100)) #versión 1: uso función mult, definida arriba
primos_x_2 = list(map(lambda x:x*2, primos_100)) #versión 2: uso una función lambda o anónima
primos_x_3 = list(map(mult_x_3, primos_100))
#print(primos_x_2)
#print(primos_x_3)

playlist = [{"titulo":"far behind", "artista":"candlebox", "genero":"rock"},
            {"titulo":"paranoid", "artista":"black sabbath", "genero":"rock"},
            {"titulo":"el ratón", "artista":"cheo feliciano", "genero":"salsa"},
            {"titulo":"lagrimas negras", "artista":"diego el cigala", "genero":"flamenco"}]

for register in playlist:
    print(register["titulo"])
    print(register["artista"])
    print(register["genero"])
    register["duracion"] = 4.5

print(playlist)
    
 #filtrada con función filtro   
playlist_filtrada = list(filter(filterData_Genero, playlist))
print(playlist_filtrada)

#filtrada con lambda
playlist_filtrada_lambda = list(filter( lambda dic: dic["genero"] == "salsa", playlist))
print(playlist_filtrada_lambda)

#filtrada con list comprehension:
playlist_f_list_comprehension = [  d  for d in playlist if d["genero"] == "flamenco"]
print(playlist_f_list_comprehension) 


