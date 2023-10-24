import os
import random

class Memory:
    def __init__(self, size):
        self.size = size
        print(f"Memory iniciada: {self.size}")
        self.used = 0

    def allocate_memory(self, size):
        if self.used + size <= self.size:
            self.used += size
            print(f"Memory alocada: {self.used}")
            return True
        else:
            return False

    def deallocate_memory(self, size):
        if self.used >= size:
            self.used -= size
            print(f"Memory foi liberada, uso de memoria atual: {self.used}")
            return True
        else:
            return False
        
class DiskSimulator:
    def __init__(self):
        self.disk_directory = "./disco/"
        if not os.path.exists(self.disk_directory):
            os.makedirs(self.disk_directory)
        self.opened_file = None

    def format_disk(self):
        files = os.listdir(self.disk_directory)
        return "Arquivos no disco: " + ", ".join(files)

    def create(self, name):
        file_path = os.path.join(self.disk_directory, name)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()
            return f"Arquivo '{name}' criado com sucesso."
        else:
            return f"O arquivo '{name}' já existe."

    def delete(self, name):
        file_path = os.path.join(self.disk_directory, name)
        if os.path.exists(file_path):
            os.remove(file_path)
            return f"Arquivo '{name}' deletado com sucesso."
        else:
            return f"O arquivo '{name}' não foi encontrado."

    def open(self, name):
        if self.opened_file is None:
            file_path = os.path.join(self.disk_directory, name)
            if os.path.exists(file_path):
                self.opened_file = open(file_path, 'r+')
                return f"Arquivo '{name}' aberto."
            else:
                return f"O arquivo '{name}' não foi encontrado."
        else:
            return "Um arquivo já está aberto. Feche-o antes de abrir outro."

    def close(self):
        if self.opened_file is not None:
            self.opened_file.close()
            self.opened_file = None
            return "Arquivo fechado com sucesso."
        else:
            return "Nenhum arquivo está aberto no momento."

    def read(self):
        if self.opened_file is not None:
            return self.opened_file.read()
        else:
            return "Nenhum arquivo aberto no momento."

    def write(self, to_write):
        if self.opened_file is not None:
            self.opened_file.write(to_write)
            return "Texto escrito com sucesso no arquivo."
        else:
            return "Nenhum arquivo aberto para escrita."

class Event:
    def __init__(self, time, action, memory_size, priority):
        self.time = time
        self.action = action
        self.memory_size = memory_size
        self.priority = priority

class EventSimulator:
    def __init__(self):
        self.event_queue = []
        self.current_time = 0  # rastrear o tempo atual
        print(f"Tempo inicial: {self.current_time}")
        
    def schedule_event(self, event):
        self.event_queue.append(event)

    def run(self, end_time):
        while self.event_queue:
            self.event_queue.sort(key=lambda x: x.priority)
            event = self.event_queue[0]
            if self.current_time < event.priority:
                self.current_time = event.priority # Ajusta chegada do evento
                print(f"Iniciando proxima tarefa no tempo: {self.current_time}")

            if memory.allocate_memory(event.memory_size):
                self.current_time += event.time  # Atualize do simulador + tempo do evento
                print(f"Tempo da tarefa: {event.time}")

                self.event_queue.remove(event)
                event.action()
                memory.deallocate_memory(event.memory_size)
                print(f"Tempo: {self.current_time}")
                print("=" * 20)
            else:
                self.event_queue.remove(event)
                print("evento nao tem memoria para ser alocado")
                
            if self.current_time > end_time:
                break
# Funções de exemplo a serem executadas como eventos
def evento1():
    print("Evento 1 ocorreu")

def evento2():
    print("Evento 2 ocorreu")
    
def generate_random_event(): #  Funçao para randomizar eventos 
    time = random.randint(10, 120)

    action = random.choice([evento1, evento2])

    memory_size = random.randint(10, 200)

    priority = random.randint(10, 1000)

    return Event(time, action, memory_size, priority)

# Inicialize o simulador de eventos e a memória
simulator = EventSimulator()
memory = Memory(size=130)# Tamanho total da memória


# Agende os eventos com prioridades e tamanhos de memória
#simulator.schedule_event(Event(60, evento1, memory_size=30, priority=20))
#simulator.schedule_event(Event(120, evento1, memory_size=100, priority=20))
#simulator.schedule_event(Event(80, evento2, memory_size=80, priority=220))
#simulator.schedule_event(Event(40, evento2, memory_size=40, priority=240))

for _ in range(8):
    random_event = generate_random_event()
    simulator.schedule_event(random_event)


# Execute o simulador até o tempo final
simulator.run(999)

# Inicialize o simulador de disko
disk = DiskSimulator()

# Exemplo de uso do simulador de disco

# Crie um arquivo no disco
print(disk.create("meuarquivo.txt"))

# Abra o arquivo recém-criado
print(disk.open("meuarquivo.txt"))

# Escreva no arquivo aberto
conteudo = "Este é o conteúdo do arquivo."
print(disk.write(conteudo))

# Leia o conteúdo do arquivo
print("Conteúdo do arquivo:")
print(disk.read())

# Feche o arquivo
print(disk.close())

# Tente abrir um arquivo que não existe
print(disk.open("nao_existe.txt"))

# Tente criar um arquivo com o mesmo nome de um existente
print(disk.create("meuarquivo.txt"))

# Exclua o arquivo criado
print(disk.delete("meuarquivo.txt"))
