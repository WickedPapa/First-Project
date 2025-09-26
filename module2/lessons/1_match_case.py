def handle_number() -> None:
    print("I numeri non sono comandi validi")

def start() -> None:
    print("Inizializzo il programma")

def update() -> None:
    print("Aggiorno le informazioni")

def stop() -> None:
    print("Arresto il programma")

def print_available_commands() -> None:
    print("Comandi disponibili: [start, inizio, update, aggiornamento, stop, help]")

def unkown_commands() -> None:
    print("Comando non riconosciuto.")
    print_available_commands()

print("Ciao", end= ". ")
while True:
    #questo controllo con try catch e il case int() |  float() non hanno senso e sono solo a scopo dimostrativo
    #avrei dovuto dichiarare command come str
    command = input("Inserisci un comando (help per vedere i comandi disponibili): ").lower().strip()
    try:
        command = int(command)
    except ValueError:
        pass
    match command :
        case int() | float():
            handle_number()
        case el if el in ["start", "inizio"]:
            start()
        case "update" | "aggiorna":
            update()
        case "stop":
            stop()
            break
        case "help":
            print_available_commands()
        case "do nothing easter egg": #continue
            continue
        case _:
            unkown_commands()

