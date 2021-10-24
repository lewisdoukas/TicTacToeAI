import tkinter as tk
import random, timeit

start = timeit.default_timer()

info = '''
                              
#######################################################################
                            ΕΡΓΑΣΙΑ BONUS                         
#######################################################################
    ΗΛΙΑΣ ΔΟΥΚΑΣ
    hliasduke@gmail.com
#######################################################################
#######################################################################
#          ΤΟ ΠΑΙΧΝΙΔΙ ΤΗΣ ΤΡΙΛΙΖΑΣ ΜΕ ΤΕΧΝΗΤΗ ΝΟΗΜΟΣΥΝΗ              #
#######################################################################
ΛΕΠΤΟΜΕΡΕΙΕΣ ΠΡΟΓΡΑΜΜΑΤΟΣ:
    1. ΤΑ ΓΡΑΦΙΚΑ ΔΗΜΙΟΥΡΓΗΘΗΚΑΝ ΜΕ ΤΗ ΒΙΒΛΙΟΘΗΚΗ tkinter ΚΑΙ ΑΠΟΤΕΛΟΥ-
    ΝΤΑΙ ΑΠΟ ΤΟ ΚΥΡΙΩΣ ΠΑΡΑΘΥΡΟ ΚΑΙ ΔΕΚΑ buttons
    2. Ο ΠΑΙΚΤΗΣ ΠΑΤΑΕΙ ΤΑ ΚΟΥΜΠΙΑ ΑΝΑΛΟΓΑ ΜΕ ΤΟ ΠΟΥ ΘΕΛΕΙ ΝΑ ΤΟΠΟΘΕ- 
    ΤΗΣΕΙ ΤΟ 'Χ' ΚΑΙ ΑΝΤΙΣΤΟΙΧΑ Ο ΥΠΟΛΟΓΙΣΤΗΣ ΠΑΙΖΕΙ 'Ο' ΣΤΗ ΒΕΛΤΙΣΤΗ
    ΓΙΑ ΚΑΘΕ ΓΥΡΟ ΘΕΣΗ    
    3. ΜΕΤΑ ΤΗΝ ΕΠΙΛΟΓΗ ΤΗΣ ΘΕΣΗ ΑΠΟ ΤΟΝ ΧΡΗΣΤΗ Η ΤΟΝ ΥΠΟΛΟΓΙΣΤΗ ΤΟ
    ΑΝΤΙΣΤΟΙΧΟ ΚΟΥΜΠΙ ΚΛΕΙΔΩΝΕΙ ΚΑΙ ΔΕΝ ΜΠΟΡΕΙ ΝΑ ΞΑΝΑ ΧΡΗΣΙΜΟΠΟΙΗΘΕΙ
    4. ΚΑΤΑ ΤΗ ΣΥΜΠΛΗΡΩΣΗ ΤΡΙΑΔΑΣ ΑΠΟ ΤΟΝ ΧΡΗΣΤΗ ΤΑ ΑΝΤΙΣΤΟΙΧΑ ΚΟΥΜΠΙΑ 
    ΓΙΝΟΝΤΑΙ ΠΡΑΣΙΝΑ, ΕΝΩ ΣΤΗΝ ΠΕΡΙΠΤΩΣΗ ΤΟΥ ΥΠΟΛΟΓΙΣΤΗ ΚΟΚΚΙΝΑ, ΔΗ-
    ΛΩΝΩΝΤΑΣ ΕΤΣΙ ΤΗΝ ΤΡΙΑΔΑ
    5. Η ΔΙΑΔΙΚΑΣΙΑ ΒΕΛΤΙΣΤΗΣ ΕΠΙΛΟΓΗΣ ΑΠΟ ΤΟΝ ΥΠΟΛΟΓΙΣΤΗ ΕΧΕΙ ΩΣ ΕΞΗΣ:
     α. ΥΠΟΛΟΓΙΖΟΝΤΑΙ ΟΛΕΣ ΟΙ ΔΙΑΘΕΣΙΜΕΣ ΚΙΝΗΣΕΙΣ
     β. ΓΙΑ ΤΙΣ ΔΙΑΘΕΣΙΜΕΣ ΚΙΝΗΣΕΙΣ, ΥΠΟΛΟΓΙΖΕΙ ΠΟΥ ΤΟ ΒΟΛΕΥΕΙ ΝΑ ΣΧΗ-
     ΜΑΤΙΣΕΙ ΤΡΙΑΔΑ
     γ. ΑΝ ΔΕ ΣΧΗΜΑΤΙΖΕΙ ΤΡΙΑΔΑ ΤΟΤΕ ΥΠΟΛΟΓΙΖΕΙ ΠΟΙΑ ΘΑ ΕΙΝΑΙ Η ΕΠΟΜΕΝΗ
     ΚΙΝΗΣΗ ΤΟΥ ΧΡΗΣΤΗ ΓΙΑ ΝΑ ΣΧΗΜΑΤΙΣΕΙ ΤΡΙΑΔΑ
     δ. ΑΝ ΟΥΤΕ Ο ΧΡΗΣΤΗΣ ΣΤΗΝ ΕΠΟΜΕΝΗ ΚΙΝΗΣΗ ΤΟΥ ΠΡΟΚΕΙΤΑΙ ΝΑ ΣΧΗΜΑΤΙ-
     ΣΕΙ ΤΡΙΑΔΑ ΤΟΤΕ ΕΛΕΓΧΕΙ ΑΝ ΕΙΝΑΙ ΚΕΝΗ Η ΚΕΝΤΡΙΚΗ ΘΕΣΗ ΑΛΛΙΩΣ ΜΙΑ
     ΑΠΟ ΤΙΣ ΓΩΝΙΕΣ, ΕΙΔΑΛΛΩΣ ΠΑΙΖΕΙ ΣΕ ΜΙΑ ΤΥΧΑΙΑ ΑΠΟ ΤΙΣ ΔΙΑΘΕΣΙΜΕΣ
     ΘΕΣΗ
     ε. ΟΥΣΙΑΣΤΙΚΑ ΤΡΕΧΕΙ ΕΝΑΝ ΓΥΡΟ ΣΤΟ ΠΑΡΑΣΚΗΝΙΟ ΧΩΡΙΣ ΝΑ ΕΜΦΑΝΙΣΤΕΙ
     ΣΤΗΝ ΟΘΟΝΗ ΤΟΥ ΧΡΗΣΤΗ, ΠΡΟΚΕΙΜΕΝΟΥ ΝΑ ΠΑΙΞΕΙ ΟΛΑ ΤΑ ΠΙΘΑΝΑ ΣΕΝΑΡΙΑ
     ΣΕ ΑΥΤΟ ΒΟΗΘΑΝΕ ΟΙ ΣΥΝΑΡΤΗΣΕΙΣ testButton ΚΑΙ unButton ΜΕ ΤΙΣ ΟΠΟΙ-
     ΕΣ ΠΑΙΖΕΙ ΣΕ ΕΝΑ ΚΟΥΜΠΙ, ΕΛΕΓΧΕΙ ΓΙΑ ΤΡΙΑΔΑ ΚΑΙ ΤΟ ΑΝΑΙΡΕΙ
    6. Ο ΕΛΕΓΧΟΣ ΓΙΑ ΣΥΜΠΛΗΡΩΣΗ ΤΡΙΑΔΑΣ ΓΙΝΕΤΑΙ ΣΥΓΚΡΙΝΟΝΤΑΣ ΤΟ ΚΕΙΜΕ-
    ΝΟ ΠΟΥ ΕΧΟΥΝ ΣΕ ΚΑΘΕ ΓΥΡΟ ΤΑ ΚΟΥΜΠΙΑ ΜΕ ΤΙΣ winnerX, winnerO
    7. Η ButtonClick ΕΙΝΑΙ Η ΚΥΡΙΑ ΣΥΝΑΡΤΗΣΗ ΠΟΥ ΣΗΜΕΙΩΝΕΙ ΤΟ ΣΥΜΒΟΛΟ
    ΣΤΟ ΑΝΤΙΣΤΟΙΧΟ ΚΟΥΜΠΙ ΜΕΣΩ ΤΗΣ SetSymbol (Η ΟΠΟΙΑ ΚΑΙ ΤΟ ΚΛΕΙΔΩΝΕΙ)
    ΕΛΕΓΧΕΙ ΓΙΑ ΤΡΙΑΔΑ, ΧΡΩΜΑΤΙΖΕΙ ΤΑ ΚΟΥΜΠΙΑ, ΠΑΙΖΕΙ ΓΙΑ ΤΟΝ ΥΠΟΛΟΓΙ-
    ΣΤΗ ΚΑΙ ΚΛΕΙΔΩΝΕΙ ΤΟ ΠΑΡΑΘΥΡΟ ΣΕ ΠΕΡΙΠΤΩΣΗ ΝΙΚΗΣ
    8. ΜΕΤΑ ΑΠΟ ΚΑΘΕ ΙΣΟΠΑΛΙΑ Η ΝΙΚΗ ΤΟΥ ΥΠΟΛΟΓΙΣΤΗ, Ο ΧΡΗΣΤΗΣ ΕΧΕΙ ΤΗ
    ΔΥΝΑΤΟΤΗΤΑ ΜΕ ΤΟ ΚΟΥΜΠΙ RESET ΝΑ ΦΕΡΕΙ ΤΟ ΠΑΡΑΘΥΡΟ ΣΤΗΝ ΑΡΧΙΚΗ ΤΟΥ
    ΜΟΡΦΗ ΚΑΙ ΝΑ ΞΑΝΑ ΠΑΙΞΕΙ, ΔΙΑΔΙΚΑΣΙΕΣ ΠΟΥ ΥΛΟΠΟΙΟΥΝΤΑΙ ΜΕΣΩ ΤΗΣ 
    Reset
***********************************************************************
++++++++++++++++++++++++++++ ΕΥΧΑΡΙΣΤΩ ++++++++++++++++++++++++++++++++
***********************************************************************
'''
print(info)

Player = random.randint(1,2)

PlayerX = []
PlayerO = []
tries = 1

def winnerX():
    if but1['text']== 'X' and but4['text']== 'X' and but7['text']== 'X':
        win = 1
    elif but2['text']== 'X' and but5['text']== 'X' and but8['text']== 'X':
        win = 1
    elif but3['text']== 'X' and but6['text']== 'X' and but9['text']== 'X':
        win = 1
    elif but1['text']== 'X' and but2['text']== 'X' and but3['text']== 'X':
        win = 1
    elif but4['text']== 'X' and but5['text']== 'X' and but6['text']== 'X': 
        win = 1
    elif but7['text']== 'X' and but8['text']== 'X' and but9['text']== 'X':
        win = 1
    elif but1['text']== 'X' and but5['text']== 'X' and but9['text']== 'X':
        win = 1
    elif but3['text']== 'X' and but5['text']== 'X' and but7['text']== 'X':   
        win = 1  
    else:
        win = 0
    return(win)
    
def winnerO():
    if but1['text']== 'O' and but4['text']== 'O' and but7['text']== 'O':
        win = 2
    elif but2['text']== 'O' and but5['text']== 'O' and but8['text']== 'O':
        win = 2
    elif but3['text']== 'O' and but6['text']== 'O' and but9['text']== 'O':
        win = 2
    elif but1['text']== 'O' and but2['text']== 'O' and but3['text']== 'O':
        win = 2
    elif but4['text']== 'O' and but5['text']== 'O' and but6['text']== 'O':
        win = 2
    elif but7['text']== 'O' and but8['text']== 'O' and but9['text']== 'O':
        win = 2
    elif but1['text']== 'O' and but5['text']== 'O' and but9['text']== 'O':
        win = 2
    elif but3['text']== 'O' and but5['text']== 'O' and but7['text']== 'O':
        win = 2
    else:
        win = 0
    return(win)
              
def Winner(winnerO, winnerX):
    if winnerO !=0 or winnerX !=0:
        winner = 1
    else:
        winner = 0
    return(winner)
    
def testButton(id, PlayerSymbol):
    if id == 1:
        but1.config(text= PlayerSymbol)
    elif id == 2:
        but2.config(text= PlayerSymbol)
    elif id == 3:
        but3.config(text= PlayerSymbol)
    elif id == 4:
        but4.config(text= PlayerSymbol)
    elif id == 5:
        but5.config(text= PlayerSymbol)
    elif id == 6:
        but6.config(text= PlayerSymbol)
    elif id == 7:
        but7.config(text= PlayerSymbol)
    elif id == 8:
        but8.config(text= PlayerSymbol)
    elif id == 9:
        but9.config(text= PlayerSymbol)    
    
def unButton(id):
    if id == 1:
        but1.config(text= '')
    elif id == 2:
        but2.config(text= '')
    elif id == 3:
        but3.config(text= '')
    elif id == 4:
        but4.config(text= '')
    elif id == 5:
        but5.config(text= '')
    elif id == 6:
        but6.config(text= '')
    elif id == 7:
        but7.config(text= '')
    elif id == 8:
        but8.config(text= '')
    elif id == 9:
        but9.config(text= '') 
    
def bestMove(PlayerX, PlayerO):
    possibleMoves = [Os for Os in range(1,10) if Os not in PlayerX and Os not in PlayerO]
    corners = [cor for cor in possibleMoves if cor == 1 or cor == 3 or cor == 7 or cor == 9]
    win = 0
    
    for pm in possibleMoves:
        testButton(pm, 'O')
        win = winnerO()
        unButton(pm)
        if win == 2:
            move = pm
            return(move)
    if win == 0:
        for pm in possibleMoves:
            testButton(pm, 'X')
            win = winnerX()
            unButton(pm)
            if win == 1:
                move = pm
                return(move)
    
    if win == 0:
        if 5 in possibleMoves:
            move = 5
            return(move)
        elif len(corners) != 0:
            move = random.choice(corners)
            return(move)
        else:
            move = random.choice(possibleMoves)
            return(move)

def SetSymbol(id,PlayerSymbol):
    if id == 1:
        but1.config(text= PlayerSymbol, state = 'disabled')
    elif id == 2:
        but2.config(text= PlayerSymbol, state = 'disabled')
    elif id == 3:
        but3.config(text= PlayerSymbol, state = 'disabled')
    elif id == 4:
        but4.config(text= PlayerSymbol, state = 'disabled')
    elif id == 5:
        but5.config(text= PlayerSymbol, state = 'disabled')
    elif id == 6:
        but6.config(text= PlayerSymbol, state = 'disabled')
    elif id == 7:
        but7.config(text= PlayerSymbol, state = 'disabled')
    elif id == 8:
        but8.config(text= PlayerSymbol, state = 'disabled')
    elif id == 9:
        but9.config(text= PlayerSymbol, state = 'disabled')      
                                          
def ButtonClick(id):
    global PlayerX, PlayerO       
    winO = winnerO()  
    winX = winnerX()                            
    winner = Winner(winO, winX)
    
    if winner == 0:
        SetSymbol(id, 'X')
        PlayerX.append(id)
    else:
        but1.config(state = 'disabled')
        but2.config(state = 'disabled')
        but3.config(state = 'disabled')
        but4.config(state = 'disabled')
        but5.config(state = 'disabled')
        but6.config(state = 'disabled')
        but7.config(state = 'disabled')
        but8.config(state = 'disabled')
        but9.config(state = 'disabled') 
    
    if but1['text']== 'X' and but4['text']== 'X' and but7['text']== 'X':
        but1.config(background = '#81F781')
        but4.config(background = '#81F781')
        but7.config(background = '#81F781')
        winX = 1
    elif but2['text']== 'X' and but5['text']== 'X' and but8['text']== 'X':
        but2.config(background = '#81F781')
        but5.config(background = '#81F781')
        but8.config(background = '#81F781')
        winX = 1
    elif but3['text']== 'X' and but6['text']== 'X' and but9['text']== 'X':
        but3.config(background = '#81F781')
        but6.config(background = '#81F781')
        but9.config(background = '#81F781')
        winX = 1
    elif but1['text']== 'X' and but2['text']== 'X' and but3['text']== 'X':
        but1.config(background = '#81F781')
        but2.config(background = '#81F781')
        but3.config(background = '#81F781')
        winX = 1
    elif but4['text']== 'X' and but5['text']== 'X' and but6['text']== 'X':
        but4.config(background = '#81F781')
        but5.config(background = '#81F781')
        but6.config(background = '#81F781') 
        winX = 1
    elif but7['text']== 'X' and but8['text']== 'X' and but9['text']== 'X':
        but7.config(background = '#81F781')
        but8.config(background = '#81F781')
        but9.config(background = '#81F781')
        winX = 1
    elif but1['text']== 'X' and but5['text']== 'X' and but9['text']== 'X':
        but1.config(background = '#81F781')
        but5.config(background = '#81F781')
        but9.config(background = '#81F781')
        winX = 1
    elif but3['text']== 'X' and but5['text']== 'X' and but7['text']== 'X':
        but3.config(background = '#81F781')
        but5.config(background = '#81F781')
        but7.config(background = '#81F781')   
        winX = 1  
    else:
        winX = 0
    
    winner = Winner(winO, winX)
                   
    if winner == 0:
        Os = bestMove(PlayerX, PlayerO)
        SetSymbol(Os, 'O')  
        PlayerO.append(Os)
    else:
        but1.config(state = 'disabled')
        but2.config(state = 'disabled')
        but3.config(state = 'disabled')
        but4.config(state = 'disabled')
        but5.config(state = 'disabled')
        but6.config(state = 'disabled')
        but7.config(state = 'disabled')
        but8.config(state = 'disabled')
        but9.config(state = 'disabled')
        
    if but1['text']== 'O' and but4['text']== 'O' and but7['text']== 'O':
        but1.config(background = '#F78181')
        but4.config(background = '#F78181')
        but7.config(background = '#F78181')
        winO = 2
    elif but2['text']== 'O' and but5['text']== 'O' and but8['text']== 'O':
        but2.config(background = '#F78181')
        but5.config(background = '#F78181')
        but8.config(background = '#F78181')
        winO = 2
    elif but3['text']== 'O' and but6['text']== 'O' and but9['text']== 'O':
        but3.config(background = '#F78181')
        but6.config(background = '#F78181')
        but9.config(background = '#F78181')
        winO = 2
    elif but1['text']== 'O' and but2['text']== 'O' and but3['text']== 'O':
        but1.config(background = '#F78181')
        but2.config(background = '#F78181')
        but3.config(background = '#F78181')
        winO = 2
    elif but4['text']== 'O' and but5['text']== 'O' and but6['text']== 'O':
        but4.config(background = '#F78181')
        but5.config(background = '#F78181')
        but6.config(background = '#F78181')
        winO = 2
    elif but7['text']== 'O' and but8['text']== 'O' and but9['text']== 'O':
        but7.config(background = '#F78181')
        but8.config(background = '#F78181')
        but9.config(background = '#F78181')
        winO = 2
    elif but1['text']== 'O' and but5['text']== 'O' and but9['text']== 'O':
        but1.config(background = '#F78181')
        but5.config(background = '#F78181')
        but9.config(background = '#F78181')
        winO = 2
    elif but3['text']== 'O' and but5['text']== 'O' and but7['text']== 'O':
        but3.config(background = '#F78181')
        but5.config(background = '#F78181')
        but7.config(background = '#F78181')
        winO = 2
    else:
        winO = 0
        
    winner = Winner(winO, winX)
                                                   
    if winner != 0:
        but1.config(state = 'disabled')
        but2.config(state = 'disabled')
        but3.config(state = 'disabled')
        but4.config(state = 'disabled')
        but5.config(state = 'disabled')
        but6.config(state = 'disabled')
        but7.config(state = 'disabled')
        but8.config(state = 'disabled')
        but9.config(state = 'disabled')
        
def Reset():
    global PlayerO, PlayerX, Player, tries
    but1.config(text= '', state = 'normal', background= '#CEECF5')
    but2.config(text= '', state = 'normal', background= '#CEECF5')
    but3.config(text= '', state = 'normal', background= '#CEECF5')
    but4.config(text= '', state = 'normal', background= '#CEECF5')
    but5.config(text= '', state = 'normal', background= '#CEECF5')
    but6.config(text= '', state = 'normal', background= '#CEECF5')
    but7.config(text= '', state = 'normal', background= '#CEECF5')
    but8.config(text= '', state = 'normal', background= '#CEECF5')
    but9.config(text= '', state = 'normal', background= '#CEECF5')
    PlayerO = []
    PlayerX = []
    Player = random.randint(1,2)
    if Player == 2:
        SetSymbol(5, 'O')
        but5.config(state = 'disabled')
        PlayerO.append(5)
    tries += 1
    
            
root = tk.Tk()
sW = root.winfo_screenwidth()
sH = root.winfo_screenheight()
pos = int(sW / 2)-sW * 0.12
root.title(' ΤΡΙΛΙΖΑ ')
root.geometry('+%d+50' % (pos))

but1 = tk.Button(root, text='', font= 40, background= '#CEECF5')
but1.grid(row= 0, column= 0, sticky= 'snew', ipadx= 40, ipady= 40)
but1.config(command=lambda: ButtonClick(1))

but2 = tk.Button(root, text='', font= 40, background= '#CEECF5')
but2.grid(row= 1, column= 0, sticky= 'snew', ipadx= 40, ipady= 40)
but2.config(command=lambda: ButtonClick(2))

but3 = tk.Button(root, text='', font= 40, background= '#CEECF5')
but3.grid(row= 2, column= 0, sticky= 'snew', ipadx= 40, ipady= 40)
but3.config(command=lambda: ButtonClick(3))

but4 = tk.Button(root, text='', font= 40, background= '#CEECF5')
but4.grid(row= 0, column= 1, sticky= 'snew', ipadx= 40, ipady= 40)
but4.config(command=lambda: ButtonClick(4))

but5 = tk.Button(root, text='', font= 40, background= '#CEECF5')
but5.grid(row= 1, column= 1, sticky= 'snew', ipadx= 40, ipady= 40)
but5.config(command=lambda: ButtonClick(5))

but6 = tk.Button(root, text='', font= 40, background= '#CEECF5')
but6.grid(row= 2, column= 1, sticky= 'snew', ipadx= 40, ipady= 40)
but6.config(command=lambda: ButtonClick(6))

but7 = tk.Button(root, text='', font= 40, background= '#CEECF5')
but7.grid(row= 0, column= 2, sticky= 'snew', ipadx= 40, ipady= 40)
but7.config(command=lambda: ButtonClick(7))

but8 = tk.Button(root, text='', font= 40, background= '#CEECF5')
but8.grid(row= 1, column= 2, sticky= 'snew', ipadx= 40, ipady= 40)
but8.config(command=lambda: ButtonClick(8))

but9 = tk.Button(root, text='', font= 40, background= '#CEECF5')
but9.grid(row= 2, column= 2, sticky= 'snew', ipadx= 40, ipady= 40)
but9.config(command=lambda: ButtonClick(9))

but10 = tk.Button(root, text= 'RESET', font= 40, bd= 4, background= '#CEECF5')
but10.grid(row= 3, columnspan= 3, sticky= 'snew')
but10.config(command=lambda: Reset())

if Player == 2:
    SetSymbol(5, 'O')
    but5.config(state = 'disabled')
    PlayerO.append(5)
   
root.mainloop()

stop = timeit.default_timer()       
time = round(stop - start, 2)    

print(f"\nΠΛΗΘΟΣ ΔΟΚΙΜΩΝ: {tries} ")
print(f"ΧΡΟΝΟΣ ΕΚΤΕΛΕΣΗΣ: {time}s ")
print("\n++++++++++++++++++++++++++++ ΕΥΧΑΡΙΣΤΩ ++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++ ΤΕΛΟΣ ++++++++++++++++++++++++++++++++")