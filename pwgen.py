import random

groß_abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abc1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abc2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abc3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

sonderzeichen = ["@", "#", "$", "%", "&"]

wörter = ["Wolke", "Berg", "Haus", "Fenster", "Tisch", "Stuhl", "Lampe", "Kühlschrank", "Computer", "Buch", "Blume", "Wasser", "Himmel", "Gras", "Stein", "Weg", "Uhr", "Schlüssel", "Tür", "Auto", "Straße", "Brücke", "Fluss", "See", "Meer", "Insel", "Baum", "Blatt", "Vogel", "Fisch", "Katze", "Hund", "Maus", "Löwe", "Affe", "Elefant", "Giraffe", "Zebra", "Apfel", "Banane", "Orange", "Erdbeere", "Tomate", "Kaffee", "Tee", "Milch", "Zucker"]

pass0 = random.choice(groß_abc)
pass1 = random.choice(abc)
pass2 = random.choice(abc1)
pass69 = random.choice(groß_abc)
pass_wort = random.choice(wörter)
pass3 = random.choice(abc2)
pass4 = random.choice(abc3)
num1 = random.choice(num)

sonderzeichen1 = random.choice(sonderzeichen)

password = pass0+pass1+pass2+pass69+pass_wort+pass3+pass4+num1+sonderzeichen1

print(f"Your Password is: {password}")