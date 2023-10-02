import tkinter as tk
from tkinter.constants import END, INSERT
import tkinter.font as font
from tkinter import filedialog as fd

class PlacaAutomovilAFD:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 
                        'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19',
                        'q20', 'q21', 'q22'}
        self.alfabeto = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-")
        self.delta = {
            ('q0', '6'):'q1',

            ('q0', '7'):'q11',
            ('q11', '-'):'q12',
            ('q12', 'A'):'q10',
            ('q12', 'B'):'q10',
            ('q12', 'C'):'q10',
            ('q12', 'D'):'q10',
            ('q12', 'E'):'q10',
            ('q12', 'F'):'q10',
            ('q12', 'G'):'q10',
            ('q12', 'H'):'q10',
            ('q12', 'I'):'q10',
            ('q12', 'J'):'q10',
            ('q12', 'K'):'q10',
            ('q12', 'L'):'q10',
            ('q12', 'M'):'q10',
            ('q12', 'N'):'q10',
            ('q12', 'O'):'q10',
            ('q12', 'P'):'q10',
            ('q12', 'Q'):'q10',

            ('q12', 'R'):'q13',

            ('q13', 'A'):'q4',
            ('q13', 'B'):'q4',
            ('q13', 'C'):'q4',
            ('q13', 'D'):'q4',
            ('q13', 'E'):'q4',
            ('q13', 'F'):'q4',
            ('q13', 'G'):'q4',
            ('q13', 'H'):'q4',
            ('q13', 'I'):'q4',
            ('q13', 'J'):'q4',
            ('q13', 'K'):'q4',
            ('q13', 'L'):'q4',
            ('q13', 'M'):'q4',
            ('q13', 'N'):'q4',
            ('q13', 'Ñ'):'q4',
            ('q13', 'O'):'q4',
            ('q13', 'P'):'q4',
            ('q13', 'Q'):'q4',
            ('q13', 'R'):'q4',
            ('q13', 'S'):'q4',
            ('q13', 'T'):'q4',
            ('q13', 'U'):'q4',

            ('q13', 'V'):'q14',
            ('q14', '-'):'q15',

            ('q1', '-'):'q2',
            ('q2', 'R'):'q3',

            ('q2', 'S'):'q10',
            ('q2', 'T'):'q10',
            ('q2', 'U'):'q10',
            ('q2', 'V'):'q10',
            ('q2', 'X'):'q10',
            ('q2', 'Y'):'q10',
            ('q2', 'Z'):'q10',

            ('q10', 'A'):'q4',
            ('q10', 'B'):'q4',
            ('q10', 'C'):'q4',
            ('q10', 'D'):'q4',
            ('q10', 'E'):'q4',
            ('q10', 'F'):'q4',
            ('q10', 'G'):'q4',
            ('q10', 'H'):'q4',
            ('q10', 'I'):'q4',
            ('q10', 'J'):'q4',
            ('q10', 'K'):'q4',
            ('q10', 'L'):'q4',
            ('q10', 'M'):'q4',
            ('q10', 'N'):'q4',
            ('q10', 'Ñ'):'q4',
            ('q10', 'O'):'q4',
            ('q10', 'P'):'q4',
            ('q10', 'Q'):'q4',
            ('q10', 'R'):'q4',
            ('q10', 'S'):'q4',
            ('q10', 'T'):'q4',
            ('q10', 'U'):'q4',
            ('q10', 'V'):'q4',
            ('q10', 'W'):'q4',
            ('q10', 'X'):'q4',
            ('q10', 'Y'):'q4',
            ('q10', 'Z'):'q4',

            ('q3', 'R'):'q4',
            ('q3', 'S'):'q4',
            ('q3', 'T'):'q4',
            ('q3', 'U'):'q4',
            ('q3', 'V'):'q4',
            ('q3', 'X'):'q4',
            ('q3', 'Y'):'q4',
            ('q3', 'Z'):'q4',
            ('q4', '-'):'q5',

            ('q5', '0'):'q6',
            
            
            ('q5', '1'):'q9',
            ('q5', '2'):'q9',
            ('q5', '3'):'q9',
            ('q5', '4'):'q9',
            ('q5', '5'):'q9',
            ('q5', '6'):'q9',
            ('q5', '7'):'q9',
            ('q5', '8'):'q9',
            ('q5', '9'):'q9',

            ('q9', '0'):'q7',
            ('q9', '1'):'q7',
            ('q9', '2'):'q7',
            ('q9', '3'):'q7',
            ('q9', '4'):'q7',
            ('q9', '5'):'q7',
            ('q9', '6'):'q7',
            ('q9', '7'):'q7',
            ('q9', '8'):'q7',
            ('q9', '9'):'q7',
            ('q6', '1'):'q7',
            ('q6', '2'):'q7',
            ('q6', '3'):'q7',
            ('q6', '4'):'q7',
            ('q6', '5'):'q7',
            ('q6', '6'):'q7',
            ('q6', '7'):'q7',
            ('q6', '8'):'q7',
            ('q6', '9'):'q7',
            ('q7', 'A'):'q8',
            ('q7', 'B'):'q8',
            ('q7', 'C'):'q8',
            ('q7', 'D'):'q8',
            ('q7', 'E'):'q8',
            ('q7', 'F'):'q8',
            ('q7', 'G'):'q8',
            ('q7', 'H'):'q8',
            ('q7', 'I'):'q8',
            ('q7', 'J'):'q8',
            ('q7', 'K'):'q8',
            ('q7', 'L'):'q8',
            ('q7', 'M'):'q8',
            ('q7', 'N'):'q8',
            ('q7', 'Ñ'):'q8',
            ('q7', 'O'):'q8',
            ('q7', 'P'):'q8',
            ('q7', 'Q'):'q8',
            ('q7', 'R'):'q8',
            ('q7', 'S'):'q8',
            ('q7', 'T'):'q8',
            ('q7', 'U'):'q8',
            ('q7', 'V'):'q8',
            ('q7', 'W'):'q8',
            ('q7', 'X'):'q8',
            ('q7', 'Y'):'q8',
            ('q7', 'Z'):'q8',

            ('q15', '0'):'q16',

            ('q15', '1'):'q19',
            ('q15', '2'):'q19',
            ('q15', '3'):'q19',
            ('q15', '4'):'q19',
            ('q15', '5'):'q19',
            ('q15', '6'):'q19',
            ('q15', '7'):'q19',
            ('q15', '8'):'q19',

            ('q15', '9'):'q20',

            ('q16', '1'):'q17',
            ('q16', '2'):'q17',
            ('q16', '3'):'q17',
            ('q16', '4'):'q17',
            ('q16', '5'):'q17',
            ('q16', '6'):'q17',
            ('q16', '7'):'q17',
            ('q16', '8'):'q17',
            ('q16', '9'):'q17',

            ('q19', '0'):'q17',
            ('q19', '1'):'q17',
            ('q19', '2'):'q17',
            ('q19', '3'):'q17',
            ('q19', '4'):'q17',
            ('q19', '5'):'q17',
            ('q19', '6'):'q17',
            ('q19', '7'):'q17',
            ('q19', '8'):'q17',
            ('q19', '9'):'q17',

            ('q20', '0'):'q17',
            ('q20', '1'):'q17',
            ('q20', '2'):'q17',
            ('q20', '3'):'q17',
            ('q20', '4'):'q17',
            ('q20', '5'):'q17',
            ('q20', '6'):'q17',
            ('q20', '7'):'q17',
            ('q20', '8'):'q17',

            ('q17', 'A'):'q18',
            ('q17', 'B'):'q18',
            ('q17', 'C'):'q18',
            ('q17', 'D'):'q18',
            ('q17', 'E'):'q18',
            ('q17', 'F'):'q18',
            ('q17', 'G'):'q18',
            ('q17', 'H'):'q18',
            ('q17', 'I'):'q18',
            ('q17', 'J'):'q18',
            ('q17', 'K'):'q18',
            ('q17', 'L'):'q18',
            ('q17', 'M'):'q18',
            ('q17', 'N'):'q18',
            ('q17', 'Ñ'):'q18',
            ('q17', 'O'):'q18',
            ('q17', 'P'):'q18',
            ('q17', 'Q'):'q18',
            ('q17', 'R'):'q18',
            ('q17', 'S'):'q18',
            ('q17', 'T'):'q18',
            ('q17', 'U'):'q18',
            ('q17', 'V'):'q18',
            ('q17', 'W'):'q18',
            ('q17', 'X'):'q18',
            ('q17', 'Y'):'q18',
            ('q17', 'Z'):'q18',

            ('q20', '9'):'q21',

            ('q21', 'A'):'q22',
            ('q21', 'B'):'q22',
            ('q21', 'C'):'q22',
            ('q21', 'D'):'q22',
            ('q21', 'E'):'q22',
            ('q21', 'F'):'q22',
            ('q21', 'G'):'q22',
            ('q21', 'H'):'q22',
            ('q21', 'I'):'q22',
            ('q21', 'J'):'q22',
            ('q21', 'K'):'q22',
            ('q21', 'L'):'q22',
            ('q21', 'M'):'q22',
            ('q21', 'N'):'q22',
            ('q21', 'Ñ'):'q22',
            ('q21', 'O'):'q22',
            ('q21', 'P'):'q22',
            ('q21', 'Q'):'q22',
            ('q21', 'R'):'q22',
            ('q21', 'S'):'q22',
            ('q21', 'T'):'q22',
        }
        self.estado_inicial = 'q0'
        self.estados_aceptacion = {'q8', 'q18', 'q22'}

    def transicion(self, simbolo):
        try:
            if simbolo not in self.alfabeto:
                raise ValueError("El símbolo no está en el alfabeto")
            if self.estado_actual not in self.estados:
                raise ValueError("El estado actual no está en el conjunto de estados")
        except: pass

        self.estado_actual = self.delta.get((self.estado_actual, simbolo), None)

    def evaluar_placa(self, placa):
        self.estado_actual = self.estado_inicial
        recorrido = []

        for simbolo in placa:
            transicion = (self.estado_actual, simbolo)
            self.transicion(simbolo)
            recorrido.append(transicion)

        es_aceptada = self.estado_actual in self.estados_aceptacion

        return es_aceptada, recorrido

class Application(tk.Frame):
    automata = None

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.set_window_format()
        self.create_stage()
        self.automata = PlacaAutomovilAFD()

    def set_window_format(self):
        self.master.title("Automata Yumari 211225")
        self.master.attributes('-fullscreen', True)
        self.master.resizable(0, 0)
        self.master.configure(background='red')
        self.place(relwidth=1, relheight=1)

    def create_stage(self):
        self.alerta = tk.Label(self, text='', font='Helvetica 18', fg="#FFB63E")
        self.resultado = tk.Label(self, text='', font='Helvetica 18', fg="#FFB63E")
        self.fuente = font.Font(family='Poppins', size=12)
        self.bienvenida = tk.Label(self, text="Bienvenido", font="Helvetica 20", fg="#FFB63E")
        self.bienvenida.place(x=333, y=45)
        self.datos = tk.Text(self, width=52, height=20, font='Helvetica 12', bg='#FFD83C')
        self.cargar_opciones()

    def cargar_opciones(self):
        self.resultado['text'] = ''
        self.cadena_lbl = tk.Label(self, text="Validar Cadena", font='Helvetica 18', fg='#FFB63E')
        self.cadena_lbl.place(x=318, y=130)
        self.cadena = tk.Entry(self, borderwidth=4, font='Helvetica 16', width=30, bg='#AFF4F9')
        self.cadena.place(x=210, y=180)
        self.validacion = tk.Button(self, font=self.fuente, text='Validar', width=15, height=1, bg="#FF5656",
                                    command=self.iniciar)
        self.validacion.place(x=330, y=250)

    def iniciar(self):
        cadena = self.cadena.get()
        es_aceptada, recorrido = self.automata.evaluar_placa(cadena)
        if es_aceptada:
            self.resultado['text'] = f"La cadena \n {cadena} \n es una  cadena valida"
            self.resultado['fg'] = "#239A10"
            self.resultado.place(x=275, y=300)
            self.datos.delete("1.0","end")
            for i, (estado, simbolo) in enumerate(recorrido):
                self.datos.insert(INSERT, f"Paso {i}: Estado {estado}, Símbolo {simbolo}")
                self.datos.insert(INSERT, '\n')
            self.datos.insert(INSERT, "Llego al estado final (q8)")
            self.datos.place(x=700, y=150)
        else:
            self.resultado[
                'text'] = f"Algunos símbolos de la cadena introducida \n no son válidos en la configuración del Automata"
            self.resultado['fg'] = "#FF5656"
            self.resultado.place(x=200, y=300)
            

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()



