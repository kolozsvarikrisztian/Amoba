def feltolt(n):
    lista = []
    for i in range(n):
        sor = []
        for j in range(n):
            sor.append('.')
        lista.append(sor)
    return lista

def kirajzol(lista):
  for sor in lista:
    for cella in sor:
        print(cella, end=' ')
    print()

def nyert(lista, jatekos, sor, oszlop):
  if nyert_sor(palya[sor], jatekos, oszlop):
    return True
  if nyert_oszlop(palya, jatekos, sor, oszlop):
    return True
  if lef(palya, jatekos, sor, oszlop):
    return True
  if felf(palya, jatekos, sor, oszlop):
    return True
  return False

def nyert_sor(sorlista, jatekos, oszlop):
  szamol = 1
  col = oszlop - 1
  while col >= 0 and sorlista[col] == jatekos["szimbolum"]:
    szamol += 1
    col -= 1
  col = oszlop + 1
  while col < len(sorlista) and sorlista[col] == jatekos["szimbolum"]:
    szamol += 1
    col += 1
  return szamol == 5

def nyert_oszlop(palya, jatekos, sor, oszlop):
  szamol = 1
  row = sor - 1
  while row >= 0 and palya[row][oszlop] == jatekos["szimbolum"]:
    szamol += 1
    row -= 1
  row = sor + 1
  while row < len(palya) and palya[row][oszlop] == jatekos["szimbolum"]:
    szamol += 1
    row += 1
  return szamol == 5

def lef(palya, jatekos, sor, oszlop):
  szamol = 1
  col = oszlop - 1
  row = sor - 1
  while col >= 0 and row >=0 and palya[row][col] == jatekos["szimbolum"]:
    szamol += 1
    col -= 1
    row -= 1
  col = oszlop + 1
  row = sor + 1
  while col <= 0 and row <=0 and palya[row][col] == jatekos["szimbolum"]:
    szamol += 1
    col += 1
    row += 1
  return szamol == 5

def felf(palya, jatekos, sor, oszlop):
  szamol = 1
  col = oszlop + 1
  row = sor + 1
  while col <= 0 and row <=0 and palya[row][col] == jatekos["szimbolum"]:
    szamol += 1
    col += 1
    row -= 1
  col = oszlop - 1
  row = sor + 1
  while col >= 0 and row >=0 and palya[row][col] == jatekos["szimbolum"]:
    szamol += 1
    col -= 1
    row += 1
  return szamol == 5

def elfogyott(lista):
  for sor in lista:
    if '.' in sor:
      return False
  return True


# palya=[['.','.','.'],['.','.','.'],['.','.','.']]
palya = feltolt(10)

print("Amőba (by:Szeszko egyetem)")
print("A megadott értékek, csak '0' és '2' között érvényesek sorban és oszlopban is")
player_x=input("Add meg az 1. játékos nevét: ")
player_o=input("Add meg a 2. játékos nevét: ")
kirajzol(palya)
print(player_x,", a szimbólumod a(z) 'x'",sep='')
print(player_o,", a szimbólumod a(z) 'o'",sep='')

jatekosok = [{'nev': player_x, "szimbolum": "x"}, {'nev': player_o, "szimbolum": "o"}]
vege=False
while not vege:
  for jatekos in jatekosok:
    print(jatekos["nev"], ", te következel!",sep='')
    beker_sor=int(input('sor: ')) - 1
    beker_oszlop=int(input('oszlop: ')) - 1
    while beker_sor < 0 or beker_sor > len(palya) - 1 or beker_oszlop < 0 or beker_oszlop > len(palya) - 1 or palya[beker_sor][beker_oszlop] != ".":
      print("ervenytelen koordinata")
      beker_sor=int(input('sor: ')) - 1         
      beker_oszlop=int(input('oszlop: ')) - 1
    palya[beker_sor][beker_oszlop]=jatekos["szimbolum"]
    kirajzol(palya)
    if nyert(palya, jatekos,beker_sor, beker_oszlop):
      gyoztes = jatekos
      vege = True
      break
    if elfogyott(palya):
      gyoztes = {}
      vege = True
      break
    # gyoztes = kiertekel(palya, jatekos)
    # if gyoztes:            
    #     vege = True
    #     break
if gyoztes: 
  print(gyoztes["nev"], "nyertél") 
else:
  print("Elfogytak a mezők, döntetlen!")