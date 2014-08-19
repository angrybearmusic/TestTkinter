import tkinter
import random

tk = tkinter

def main():
    root = tk.Tk()
    global value2
    
    def randomnum():
        global value2
        choice = random.randint(1,3)
        print (choice)
        if choice == 1:
            value2 = str('rock')
        elif choice == 2:
            value2 = str('paper')
        elif choice == 3:
            value2 = str('scissors')
        print (value2)
    
    randomnum()


    def sel_rock():
        global value1
        value1 = 'rock'
        print (value1)
        compare()

    def sel_paper():
        global value1
        value1 = 'paper'
        print (value1)
        compare()

    def sel_scissors():
        global value1
        value1 = 'scissors'
        print (value1)
        compare()

    def compare():
        winner = tk.Tk()
        
        
        if value1 == 'rock':
            if value2 == 'paper':
                result = tk.Label(winner, text = value2 + ' beats ' + value1).pack()
                randomnum()
            elif value2 == 'scissors':
                result = tk.Label(winner, text = value1 + ' beats ' + value2).pack()
                randomnum()
            else:
                result = tk.Label(winner, text = 'tie').pack()
                randomnum()
        elif value1 == 'paper':
            if value2 == 'scissors':
                result = tk.Label(winner, text = value2 + ' beats ' + value1).pack()
                randomnum()
            elif value2 == 'rock':
                result = tk.Label(winner, text = value1 + ' beats ' + value2).pack()
                randomnum()
            else:
                result = tk.Label(winner, text = 'tie').pack()
                randomnum()
        else:
            if value2 == 'rock':
                result = tk.Label(winner, text = value2 + ' beats ' + value1).pack()
                randomnum()
            elif value2 == 'paper':
                result = tk.Label(winner, text = value1 + ' beats ' + value2).pack()
                randomnum()
            else:
                result = tk.Label(winner, text = 'tie').pack()
                randomnum()
        tk.mainloop()
    
        
    label = tk.Label(root, text = "Please select your weapon").grid(row = 0)
    rock = tk.Button(root, text = 'rock', command = sel_rock).grid(row = 1)
    paper = tk.Button(root, text = 'paper', command = sel_paper).grid(row = 2)
    scissors = tk.Button(root, text = 'scissors', command = sel_scissors).grid(row = 3)    
            
    tk.mainloop()



    
if __name__ == "__main__":
    main()    
    