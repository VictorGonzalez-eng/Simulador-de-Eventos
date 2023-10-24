# Simulador de Eventos com Alocação de Memória e Disco

Este projeto consiste em um simulador de sistema operacional baseado em eventos. O simulador é implementado em Python e é capaz de criar, agendar e executar eventos com diferentes prioridades e requisitos de alocação de memória. Além disso, ele simula operações de entrada e saída em um disco virtual.

## Funcionalidades Principais

- **Simulação de Eventos**: O simulador permite a criação de eventos com diferentes atributos, como tempo de execução, ação, tamanho de memória e prioridade. Isso possibilita a modelagem de cenários diversos e a avaliação do comportamento do sistema em situações variadas.

- **Alocação de Memória**: O gerenciamento de memória é essencial em sistemas operacionais. A classe `Memory` permite a alocação e desalocação de memória de forma eficaz, garantindo que os eventos utilizem os recursos de memória de maneira apropriada.

- **Simulador de Disco**: A simulação de operações de entrada e saída em um disco virtual é uma adição valiosa para a modelagem de sistemas operacionais. O `DiskSimulator` oferece operações de criação, abertura, escrita, leitura, fechamento e exclusão de arquivos no disco simulado.

- **Geração de Eventos Aleatórios**: A capacidade de gerar eventos aleatórios é especialmente útil para testes de robustez e experimentações. Isso permite explorar cenários variados e avaliar o desempenho do sistema em condições diversas.

## Como Usar

1. Clone o repositório ou incorpore o código em seu projeto.
2. Certifique-se de ter o Python instalado em seu sistema.
3. Execute o simulador para criar e agendar eventos. Você pode adicionar eventos manualmente ou usar a função `generate_random_event` para criar eventos aleatórios.
4. O simulador executará os eventos com base em suas prioridades e requisitos de memória, simulando o comportamento de um sistema operacional.
5. As operações de entrada e saída no disco simulado também podem ser testadas e exploradas.

## Exemplo de Uso

```python
# Exemplo de uso do simulador de disco
disk = DiskSimulator()
print(disk.create("meuarquivo.txt"))
print(disk.open("meuarquivo.txt"))
print(disk.write("Este é o conteúdo do arquivo."))
print("Conteúdo do arquivo:")
print(disk.read())
print(disk.close())
print(disk.open("nao_existe.txt"))
print(disk.create("meuarquivo.txt"))
print(disk.delete("meuarquivo.txt"))

# Agende eventos aleatórios
for _ in range(4):
    random_event = generate_random_event()
    simulator.schedule_event(random_event)
```    
Contribuições
Contribuições são bem-vindas. Sinta-se à vontade para abrir problemas ou propor melhorias.

### Licença
Este projeto é licenciado sob a Licença MIT.

Este simulador é uma ferramenta versátil para experimentações e testes no contexto de sistemas operacionais, permitindo a modelagem e simulação de eventos e operações de memória e disco. A geração de eventos aleatórios também facilita a exploração de cenários diversos.
