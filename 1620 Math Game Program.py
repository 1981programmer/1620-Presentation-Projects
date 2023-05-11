from tkinter import *
import random

class MATH_GAME:
    '''
    A class representing details for a math game object.
    '''
    def __init__(self) -> None:
        '''
        Constructor to create initial state of an GUI for a math game with scores set to zero and time set to 5 seconds.
        TIME CAN BE CHANGED.
        '''
        self.root = Tk()
        self.root.title('Math Game')
        self.root.geometry('400x400')
        self.root.resizable(False, False)
        self.canvas = Canvas(width=200, height=5)
        self.minutes: int = 0
        self.seconds: int = 30
        self.player_correct_score: int = 0
        self.player_incorrect_score: int = 0
        self.which_sign_for_game: int = 0
        self.which_number_player_will_guess: int = 0
        
    def make_game(self) -> None:
        '''
        Method to create start game screen with title and button to start a game.
        '''
        self.root.configure(bg='blue')
        self.math_game_frame = Frame(self.root)
        self.math_game_label = Label(self.math_game_frame, text='Math Game', font=('Helvetica bold', 30))
        self.math_game_frame.pack(pady=10)
        self.math_game_label.pack()
        self.start_game_button_frame = Frame(self.root)
        self.start_game_button = Button(self.start_game_button_frame, text='Click to Start Game', font=('Helvetica bold', 15), command=self.start_game)
        self.start_game_button_frame.pack(pady=20)
        self.start_game_button.pack()
        
    def start_game(self) -> None:
        '''
        Method to delete math game frame and call the game screen with a problem and timer that will make the game.
        '''
        self.root.configure(bg='green')
        self.math_game_frame.pack_forget()
        self.start_game_button_frame.pack_forget()
        self.game_started_button_frame = Frame(self.root)
        self.game_started_button = Label(self.game_started_button_frame)
        self.game_started_button_frame.pack(pady=20)
        self.game_started_button.pack()

        self.game_screen()
        self.update_timer()
        
    def update_timer(self) -> None:
        '''
        Method to update timer every ONE second.
        CAN BE CHANGED. The after method is based on milliseconds, so 1000 milliseconds is one second.
        '''
        try:
            self.minutes_format = f'{self.minutes:02d}'
            self.seconds_format = f'{self.seconds:02d}'
            self.game_started_button.config(text=self.minutes_format + ':' + self.seconds_format, font=('Helvetica bold', 20))
            self.minutes = int(self.minutes_format)
            self.seconds = int(self.seconds_format)
            
            if self.minutes > 0 and self.seconds == 0:
                self.minutes -= 1
                self.seconds = 59   
            elif self.minutes > -1 and self.seconds != 0:
                self.seconds -= 1  
            else:
                self.game_over()
                
            self.game_started_button.after(1000, self.update_timer)
        except:
            print('The Game Is Over')

    def game_screen(self) -> None:
        '''
        Method to create enter button, frames that will hold numbers and label that will be updated based on if that previous
        problem was answered correctly or incorrectly by the player.
        '''
        self.enter_answer_frame_button_1 = Frame(self.root)
        self.enter_answer_button_1 = Button(self.enter_answer_frame_button_1, text='ENTER', command=self.enter_answer_1)
        self.enter_answer_frame_button_1.pack(pady=10)
        self.enter_answer_button_1.pack()
        self.game_frame_1 = Frame(self.root, height=45, width=350, bg='green')
        self.game_frame_2 = Frame(self.root, height=45, width=350, bg='green')
        self.canvas.create_line(40,5,190,5,width=2)
        self.game_frame_3 = Frame(self.root, height=45, width=350, bg='green')
        self.game_frame_1.pack(anchor='e', padx=15, pady=5)
        self.game_frame_1.pack_propagate(0)
        self.game_frame_2.pack(anchor='e', padx=5)
        self.game_frame_2.pack_propagate(0)
        self.canvas.create_line(40,5,190,5,width=2)
        self.canvas.pack(anchor='e')
        self.game_frame_3.pack(anchor='e', padx=5)
        self.game_frame_3.pack_propagate(0)
        self.last_answer_was_correct_or_incorrect = Label(self.game_frame_1, bg='green', font=('Helvetica bold', 13))
        self.last_answer_was_correct_or_incorrect.pack(side='left')
        self.update_screen()
        
    def update_screen(self) -> None:
        '''
        Method to make problems and which number the player must enter to make the math problem true. The problem will be either an
        addition problem or a multiplication problem chosen at random.
        '''
        self.which_sign_for_game = random.randint(1, 2)
        self.which_number_player_will_guess = random.randint(1, 3)
        if self.which_sign_for_game == 1:
            self.x = random.randint(1, 10)
            self.y = random.randint(1, 10)
        elif self.which_sign_for_game == 2:
            self.x = random.randint(1, 50)
            self.y = random.randint(1, 50)            
        self.product_result = self.x * self.y
        self.add_result = self.x + self.y
        self.first_entry_multiply_number = Entry(self.game_frame_1, width=2, font=('Helvetica bold', 40), justify=RIGHT)
        self.multiply_sign_for_second_entry = Label(self.game_frame_2, width=1, text='X', font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.second_entry_multiply_number = Entry(self.game_frame_2, width=2, font=('Helvetica bold', 40), justify=RIGHT)
        self.canvas.create_line(40,5,190,5,width=2)
        self.third_entry_multiply_number = Entry(self.game_frame_3, width=3, font=('Helvetica bold', 40), justify=RIGHT)
        self.first_multiply_text_number = Label(self.game_frame_1, width=2, text=self.x, font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.second_multiply_text_number = Label(self.game_frame_2, width=4, text=f'X  {self.y}', font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.third_multiply_text_number = Label(self.game_frame_3, width=3, text=self.product_result, font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.first_entry_add_number = Entry(self.game_frame_1, width=2, font=('Helvetica bold', 40), justify=RIGHT)
        self.add_sign_for_second_entry = Label(self.game_frame_2, width=1, text='+', font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.second_entry_add_number = Entry(self.game_frame_2, width=2, font=('Helvetica bold', 40), justify=RIGHT)
        self.canvas.create_line(40,5,190,5,width=2)
        self.third_entry_add_number = Entry(self.game_frame_3, width=3, font=('Helvetica bold', 40), justify=RIGHT)
        self.first_add_text_number = Label(self.game_frame_1, width=2, text=self.x, font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.second_add_text_number = Label(self.game_frame_2, width=4, text=f'+  {self.y}', font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.third_add_text_number = Label(self.game_frame_3, width=3, text=self.add_result, font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        
        if self.which_sign_for_game == 1:
            if self.which_number_player_will_guess == 1:
                self.first_entry_multiply_number.pack(side='right')
                self.first_entry_multiply_number.focus_set()
                self.second_multiply_text_number.pack(side='right')
                self.third_multiply_text_number.pack(side='right')
            elif self.which_number_player_will_guess == 2:
                self.first_multiply_text_number.pack(side='right')
                self.second_entry_multiply_number.pack(side='right')
                self.second_entry_multiply_number.focus_set()
                self.multiply_sign_for_second_entry.pack(side='right')
                self.third_multiply_text_number.pack(side='right')

            elif self.which_number_player_will_guess == 3:
                self.first_multiply_text_number.pack(side='right')
                self.second_multiply_text_number.pack(side='right')
                self.third_entry_multiply_number.pack(side='right')
                self.third_entry_multiply_number.focus_set()
                
        elif self.which_sign_for_game == 2:
            if self.which_number_player_will_guess == 1:
                self.first_entry_add_number.pack(side='right')
                self.first_entry_add_number.focus_set()
                self.second_add_text_number.pack(side='right')
                self.third_add_text_number.pack(side='right')

            elif self.which_number_player_will_guess == 2:
                self.first_add_text_number.pack(side='right')
                self.second_entry_add_number.pack(side='right')
                self.second_entry_add_number.focus_set()
                self.add_sign_for_second_entry.pack(side='right')
                self.third_add_text_number.pack(side='right')

            elif self.which_number_player_will_guess == 3:
                self.first_add_text_number.pack(side='right')
                self.second_add_text_number.pack(side='right')
                self.third_entry_add_number.pack(side='right')
                self.third_entry_add_number.focus_set()
      
    def enter_answer_1(self) -> None:
        '''
        Method to check if the number the player has entered is true or false. Based on that the correct score or incorrect score
        will be updated. The labels will be deleted and text will be shown to say the previous problem was correct or incorrect.
        The game will then make a new problem for the player.
        '''
        try:
            if self.which_sign_for_game == 1:
                if self.which_number_player_will_guess == 1:
                    player_guess = int(self.first_entry_multiply_number.get())
                    if player_guess == self.x:
                        self.player_correct_score +=1
                        self.first_entry_multiply_number.pack_forget()
                        self.second_multiply_text_number.pack_forget()
                        self.third_multiply_text_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Correct')
                        self.update_screen()

                    elif player_guess != self.x:
                        self.player_incorrect_score += 1
                        self.first_entry_multiply_number.pack_forget()
                        self.second_multiply_text_number.pack_forget()
                        self.third_multiply_text_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Incorrect')
                        self.update_screen()
 
                elif self.which_number_player_will_guess == 2:
                    player_guess = int(self.second_entry_multiply_number.get())
                    if player_guess == self.y:
                        self.player_correct_score +=1
                        self.first_multiply_text_number.pack_forget()
                        self.second_entry_multiply_number.pack_forget()
                        self.multiply_sign_for_second_entry.pack_forget()
                        self.third_multiply_text_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Correct')
                        self.update_screen()

                    elif player_guess != self.y:
                        self.player_incorrect_score += 1
                        self.first_multiply_text_number.pack_forget()
                        self.second_entry_multiply_number.pack_forget()
                        self.multiply_sign_for_second_entry.pack_forget()
                        self.third_multiply_text_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Incorrect')
                        self.update_screen()
                        
                elif self.which_number_player_will_guess == 3:
                    player_guess = int(self.third_entry_multiply_number.get())
                    if player_guess == self.product_result:
                        self.player_correct_score +=1
                        self.first_multiply_text_number.pack_forget()
                        self.second_multiply_text_number.pack_forget()
                        self.third_entry_multiply_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Correct')
                        self.update_screen()

                    elif player_guess != self.product_result:
                        self.player_incorrect_score += 1
                        self.first_multiply_text_number.pack_forget()
                        self.second_multiply_text_number.pack_forget()
                        self.third_entry_multiply_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Incorrect')
                        self.update_screen()
                        
            elif self.which_sign_for_game == 2:
                if self.which_number_player_will_guess == 1:
                    player_guess = int(self.first_entry_add_number.get())
                    if player_guess == self.x:
                        self.player_correct_score +=1
                        self.first_entry_add_number.pack_forget()
                        self.second_add_text_number.pack_forget()
                        self.third_add_text_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Correct')
                        self.update_screen()

                    elif player_guess != self.x:
                        self.player_incorrect_score += 1
                        self.first_entry_add_number.pack_forget()
                        self.second_add_text_number.pack_forget()
                        self.third_add_text_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Incorrect')
                        self.update_screen()
     
                elif self.which_number_player_will_guess == 2:
                    player_guess = int(self.second_entry_add_number.get())
                    if player_guess == self.y:
                        self.player_correct_score +=1
                        self.first_add_text_number.pack_forget()
                        self.second_entry_add_number.pack_forget()
                        self.add_sign_for_second_entry.pack_forget()
                        self.third_add_text_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Correct')
                        self.update_screen()

                    elif player_guess != self.y:
                        self.player_incorrect_score += 1
                        self.first_add_text_number.pack_forget()
                        self.second_entry_add_number.pack_forget()
                        self.add_sign_for_second_entry.pack_forget()
                        self.third_add_text_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Incorrect')
                        self.update_screen()
                        
                elif self.which_number_player_will_guess == 3:
                    player_guess = int(self.third_entry_add_number.get())
                    if player_guess == self.add_result:
                        self.player_correct_score +=1
                        self.first_add_text_number.pack_forget()
                        self.second_add_text_number.pack_forget()
                        self.third_entry_add_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Correct')
                        self.update_screen()

                    elif player_guess != self.add_result:
                        self.player_incorrect_score += 1
                        self.first_add_text_number.pack_forget()
                        self.second_add_text_number.pack_forget()
                        self.third_entry_add_number.pack_forget()
                        self.last_answer_was_correct_or_incorrect.config(text='Previous Problem Incorrect')
                        self.update_screen()
         
        except:
            self.first_entry_multiply_number.delete(0, END)

    def game_over(self) -> None:
        '''
        Method to stop the game. This deletes the frames from the game and puts a game over message with the number of
        correct problems and incorrect problems for the player.
        '''
        self.root.configure(bg='red')
        self.enter_answer_frame_button_1.pack_forget()
        self.game_frame_1.pack_forget()
        self.game_frame_2.pack_forget()
        self.canvas.pack_forget()
        self.game_frame_3.pack_forget()
        self.game_over_button_frame = Frame(self.root)
        self.game_over_button = Label(self.game_over_button_frame, text='GAME OVER', font=('Helvetica bold', 30))
        self.game_over_button_frame.pack(pady=30)
        self.game_over_button.pack()
        self.player_correct_score_frame = Frame(self.root)
        self.player_correct_score_button = Label(self.player_correct_score_frame, text=f'Your Correct Score: {self.player_correct_score} Correct', font=('Helvetica bold', 14))
        self.player_correct_score_frame.pack(pady=30)
        self.player_correct_score_button.pack()
        self.player_incorrect_score_frame = Frame(self.root)
        self.player_incorrect_score_button = Label(self.player_incorrect_score_frame, text=f'Your Incorrect Score: {self.player_incorrect_score} Incorrect', font=('Helvetica bold', 14))
        self.player_incorrect_score_frame.pack(pady=30)
        self.player_incorrect_score_button.pack()
        
        self.root.mainloop()

def main() -> None:
    first_try = MATH_GAME()
    the_return = first_try.make_game()

if __name__ == '__main__':
    main()
    