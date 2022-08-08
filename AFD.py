from tokenize import String


class AFD:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.initial_state = String
        self.transition_function = [[]]
        self.end_states = []
        
    def input_states(self):
        print("Defina os estados")
        num = 1;
        state = None
        while(state != ''): 
            state = input(str(num) +" estado: ") 
            if(state != ''):
                self.states.append(state)
            num = num + 1
        print(self.states)

    def input_alphabet(self):
        print("Defina o alfabeto de entrada")
        num = 1;
        string = None
        while(string != ''): 
            string = input(str(num) +" simbolo: ")
            if (string != ''):
                self.alphabet.append(string)
            num = num + 1
            print(self.alphabet)
    
    def select_initial_state(self):
        print("Defina o estado inicial")
        self.initial_state = input("estado incial: ")
        if self.initial_state not in self.states:
            print("estado invalido!")
            self.select_initial_state()

    def define_transition_function(self):
        self.transition_function = [[0 for x in range(len(self.alphabet))] for y in range(len(self.states))]
        print("Defina a função de transição")
        print("Se não houver transição use 0")
        for i in range(len(self.states)):
            for j in range(len(self.alphabet)):
                new_state = input("T"+"("+self.states[i]+","+self.alphabet[j]+"): ")
                self.transition_function[i][j] = new_state

    def select_end_states(self):
        print("Defina os estados finais")
        num = 1;
        end_state = None
        while(end_state != ''): 
            end_state = input(str(num) +" estado final: ")
            if (end_state in self.states):
                if (end_state != ''):
                    self.end_states.append(end_state)
                num = num + 1
            elif(end_state not in self.states and end_state != ''):
                input("Não é um estado valido, os estados de finais tem que estar contido nos estados do automato.")
            print(self.end_states)


afd = AFD()

afd.input_states()
afd.input_alphabet()
afd.select_initial_state()
afd.define_transition_function()
afd.select_end_states()