import time
lyrics=[("Maadi Veetula",1),("Oru pulli maanu da",1),("Kedachu pochuda",1),("Naan ketta piece-u da",1),("Velli kolusula puthu",1),("Satham pottu thaan",1),("Chinna manasa thaan",1),("Ava valachu pottuta",1)]
for line,delay in lyrics:
    for char in line:
        print(char, end="", flush=True)
        time.sleep(0.07)
    print()
    time.sleep(delay)