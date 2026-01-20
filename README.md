# Python_using_Stm32Prog

## 📌 Visão Geral

**Python_using_Stm32Prog** é um projeto que utiliza a linguagem **Python** para automatizar e controlar o **STM32CubeProgrammer (STM32Prog)** por meio de sua interface de linha de comando (CLI). O objetivo é simplificar tarefas comuns no desenvolvimento com microcontroladores **STM32**, como detecção de programadores, apagamento de memória e gravação de firmware.

O projeto é especialmente útil em cenários de **desenvolvimento embarcado**, **testes automatizados**, **linhas de produção** e **ambientes educacionais**, onde a repetição e a confiabilidade do processo de programação são essenciais.

---

## 🚀 Funcionalidades

* Detecção automática de programadores **ST-LINK** conectados
* Apagamento da memória Flash do microcontrolador
* Gravação de firmware a partir de arquivos **.elf**
* Integração direta com o **STM32CubeProgrammer CLI**
* Automação completa via scripts Python

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **STM32CubeProgrammer (STM32Prog)**
* Microcontroladores **STM32**
* Interface **ST-LINK (USB)**
* Sistema operacional Linux

---

## 📂 Estrutura do Projeto

```
Python_using_Stm32Prog/
│
├── codigos/                # Scripts principais em Python
├── elfs_tests/           # Arquivos .elf para gravação
├── README.md           # Documentação do projeto
```

---

## ▶️ Como Utilizar

1. Instale o **STM32CubeProgrammer** e garanta que o comando `STM32_Programmer_CLI` esteja no `PATH` do sistema.
2. Clone este repositório:

```bash
git clone https://github.com/Leandruvisk/Python_using_Stm32Prog.git
cd Python_using_Stm32Prog
```

3. Execute o script principal em Python:

```bash
python3 main.py
```

4. Conecte o microcontrolador STM32 via **ST-LINK** e acompanhe o processo pelo terminal.

---

## 📄 Exemplo de Operações Automatizadas

* Identificar automaticamente o ST-LINK conectado
* Apagar toda a Flash do dispositivo
* Programar o firmware `.elf`
* Validar a gravação

---

## 🎯 Aplicações

* Desenvolvimento de firmware STM32
* Automação de testes em sistemas embarcados
* Programação em massa (produção)
* Projetos acadêmicos e didáticos
* Integração com pipelines de CI/CD para firmware

---

## 📌 Observações

* Certifique-se de ter permissões adequadas para acessar dispositivos USB.
* O projeto pode ser facilmente estendido para suportar **.bin** ou **.hex**.
* Compatível com múltiplas famílias STM32 (dependendo do suporte do STM32CubeProgrammer).

---

## 📜 Licença

Este projeto é distribuído sob a licença **MIT**. Sinta-se à vontade para usar, modificar e contribuir.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Abra uma *issue* ou envie um *pull request* com melhorias, correções ou novas funcionalidades.

