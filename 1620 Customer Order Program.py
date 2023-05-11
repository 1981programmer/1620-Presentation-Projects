from tkinter import *
from tkinter import messagebox

class CUSTOMER_ORDER:
    '''
    A class representing details for a customer order object.
    '''
    def __init__(self) -> None:
        '''
        Constructor to create initial state of an GUI for a customer order with everything in order first set to 0 or emtpy.
        '''
        self.root = Tk()
        self.root.title('Customer Order')
        self.root.geometry('800x800')
        self.root.resizable(False, False)
        self.customer_cart_list: list = []
        self.customer_order_amount: float = 0.00
        self.customer_coke_quantity_total: int = 0
        self.customer_total_coke_price: float = 0.0
        self.customer_diet_coke_quantity_total: int = 0
        self.customer_total_diet_coke_price: float = 0.0
        self.customer_sprite_quantity_total: int = 0
        self.customer_total_sprite_price: float = 0.0
        self.customer_root_beer_quantity_total: int = 0
        self.customer_total_root_beer_price: float = 0.0
        self.customer_fanta_quantity_total: int = 0
        self.customer_total_fanta_price: float = 0.0
        self.customer_hamburger_quantity_total: int = 0
        self.customer_total_hamburger_price: float = 0.0
        self.customer_cheeseburger_quantity_total: int = 0
        self.customer_total_cheeseburger_price: float = 0.0
        self.customer_crispy_chicken_quantity_total: int = 0
        self.customer_total_crispy_chicken_price: float = 0.0
        self.customer_small_pizza_quantity_total: int = 0
        self.customer_total_small_pizza_price: float = 0.0        
        self.customer_medium_pizza_quantity_total: int = 0
        self.customer_total_medium_pizza_price: float = 0.0        
        self.customer_large_pizza_quantity_total: int = 0
        self.customer_total_large_pizza_price: float = 0.0        
        self.customer_spaghetti_quantity_total: int = 0
        self.customer_total_spaghetti_price: float = 0.0        
        self.customer_chicken_alfredo_quantity_total: int = 0
        self.customer_total_chicken_alfredo_price: float = 0.0        
        self.customer_chicken_parmesan_quantity_total: int = 0
        self.customer_total_chicken_parmesan_price: float = 0.0          
        self.customer_chicken_ceasar_quantity_total: int = 0
        self.customer_total_chicken_ceasar_price: float = 0.0          
        self.customer_greek_quantity_total: int = 0
        self.customer_total_greek_price: float = 0.0          
        self.customer_asian_sesame_quantity_total: int = 0
        self.customer_total_asian_sesame_price: float = 0.0
        self.customer_cookie_quantity_total: int = 0
        self.customer_total_cookie_price: float = 0.0
        self.customer_brownie_quantity_total: int = 0
        self.customer_total_brownie_price: float = 0.0
        self.customer_ice_cream_quantity_total: int = 0
        self.customer_total_ice_cream_price: float = 0.0  
        self.check_coke_in_list: list = []
        self.check_diet_coke_in_list: list = []
        self.check_sprite_in_list: list = []
        self.check_root_beer_in_list: list = []
        self.check_fanta_in_list: list = []
        self.check_hamburger_in_list: list = []
        self.check_cheeseburger_in_list: list = []
        self.check_crispy_chicken_in_list: list = []
        self.check_small_pizza_in_list: list = []
        self.check_medium_pizza_in_list: list = []
        self.check_large_pizza_in_list: list = []
        self.check_spaghetti_in_list: list = []
        self.check_chicken_alfredo_in_list: list = []
        self.check_chicken_parmesan_in_list: list = []
        self.check_chicken_ceasar_in_list: list = []
        self.check_greek_in_list: list = []
        self.check_asian_sesame_in_list: list = []
        self.check_cookie_in_list: list = []
        self.check_brownie_in_list: list = []
        self.check_ice_cream_in_list: list = []

    def make_main(self) -> None:
        '''
        Method to make the main menu screen with choices for the customer.
        These include frames, labels, radio buttons, next button, and cart button.
        '''
        self.root.configure(bg='blue')
        self.header_frame = Frame(self.root)
        self.header_label = Label(self.header_frame, text='Main Menu', font=('Helvetica bold', 35))
        self.header_frame.pack(pady=5)
        self.header_label.pack()
        self.drink_frame = Frame(self.root)
        self.drink_label = Label(self.drink_frame)
        self.radio_1 = IntVar()
        self.drink_radio_button = Radiobutton(self.drink_frame, text='Drink', font=('Helvetica bold', 20), variable=self.radio_1, value=0)
        self.drink_label.pack(padx=5, side='left')
        self.drink_frame.pack(anchor='w', padx=30, pady=10)
        self.drink_radio_button.pack(padx=5, side='left')
        self.sandwich_frame = Frame(self.root)
        self.sandwich_label = Label(self.sandwich_frame)
        self.sandwich_radio_button = Radiobutton(self.sandwich_frame, text='Sandwich', font=('Helvetica bold', 20), variable=self.radio_1, value=1)
        self.sandwich_label.pack(padx=5, side='left')
        self.sandwich_frame.pack(anchor='w', padx=30, pady=10)
        self.sandwich_radio_button.pack(padx=5, side='left')
        self.pizza_frame = Frame(self.root)
        self.pizza_label = Label(self.pizza_frame)
        self.pizza_radio_button = Radiobutton(self.pizza_frame, text='Pizza', font=('Helvetica bold', 20), variable=self.radio_1, value=2)
        self.pizza_label.pack(padx=5, side='left')
        self.pizza_frame.pack(anchor='w', padx=30, pady=10)
        self.pizza_radio_button.pack(padx=5, side='left')
        self.pasta_frame = Frame(self.root)
        self.pasta_label = Label(self.pasta_frame)
        self.pasta_radio_button = Radiobutton(self.pasta_frame, text='Pasta', font=('Helvetica bold', 20), variable=self.radio_1, value=3)
        self.pasta_label.pack(padx=5, side='left')
        self.pasta_frame.pack(anchor='w', padx=30, pady=10)
        self.pasta_radio_button.pack(padx=5, side='left')
        self.salad_frame = Frame(self.root)
        self.salad_label = Label(self.salad_frame)
        self.salad_radio_button = Radiobutton(self.salad_frame, text='Salad', font=('Helvetica bold', 20), variable=self.radio_1, value=4)
        self.salad_label.pack(padx=5, side='left')
        self.salad_frame.pack(anchor='w', padx=30, pady=10)
        self.salad_radio_button.pack(padx=5, side='left')
        self.dessert_frame = Frame(self.root)
        self.dessert_label = Label(self.dessert_frame)
        self.dessert_radio_button = Radiobutton(self.dessert_frame, text='Dessert', font=('Helvetica bold', 20), variable=self.radio_1, value=5)
        self.dessert_label.pack(padx=5, side='left')
        self.dessert_frame.pack(anchor='w', padx=30, pady=10)
        self.dessert_radio_button.pack(padx=5, side='left')
        self.radio_1.set(None)

        
        self.menu_next_button_frame = Frame(self.root)
        self.menu_next_button = Button(self.menu_next_button_frame, text='NEXT', font=('Helvetica bold', 15), command=self.menu_next_clicked)
        self.menu_next_button_frame.pack(pady=20)
        self.menu_next_button.pack()
        self.menu_cart_button_frame = Frame(self.root)
        self.menu_cart_button = Button(self.menu_cart_button_frame, text='CART', font=('Helvetica bold', 15), command=self.menu_cart_clicked)
        self.menu_cart_button_frame.pack(pady=10)
        self.menu_cart_button.pack()
        
    def menu_pack_forget(self) -> None:
        '''
        Method to delete the frames from the main menu screen.
        '''
        self.header_frame.pack_forget()
        self.drink_frame.pack_forget()
        self.sandwich_frame.pack_forget()
        self.pizza_frame.pack_forget()
        self.pasta_frame.pack_forget()
        self.salad_frame.pack_forget()
        self.dessert_frame.pack_forget()
        self.menu_next_button_frame.pack_forget()
        self.menu_cart_button_frame.pack_forget()
    
    def menu_next_clicked(self) -> None:
        '''
        Method to delete the frames from the main menu screen and create a new screen for the customer based on their selection.
        '''
        try:
            customer_choice = self.radio_1.get()
            if customer_choice == 0:
                self.menu_pack_forget()
                self.drink_menu()
                
            elif customer_choice == 1:
                self.menu_pack_forget()
                self.sandwich_menu()
            
            elif customer_choice == 2:
                self.menu_pack_forget()
                self.pizza_menu()
                
            
            elif customer_choice == 3:
                self.menu_pack_forget()
                self.pasta_menu()
            
            elif customer_choice == 4:
                self.menu_pack_forget()
                self.salad_menu()
            
            elif customer_choice == 5:
                self.menu_pack_forget()
                self.dessert_menu()
                
        except:
            messagebox.showinfo('NO SELECTION', 'You Did Not Make a Selection!')
            
    def menu_cart_clicked(self) -> None:
        '''
        Method to delete the frames from the main menu screen and create the cart menu screen if cart button selected.
        '''
        self.menu_pack_forget()
        self.cart_menu()
        
    def drink_menu(self) -> None:
        '''
        Method to create the frames, labels, radio buttons, back to menu button, and add to cart button
        for the drinks choices the customer may chose from.
        '''
        self.root.configure(bg='purple')
        self.drink_header_frame = Frame(self.root)
        self.drink_header_label = Label(self.drink_header_frame, text='Drink Menu', font=('Helvetica bold', 35))
        self.drink_header_frame.pack(pady=5)
        self.drink_header_label.pack()
        self.drink_choose_frame = Frame(self.root)
        self.drink_choose_label = Label(self.drink_choose_frame, text='Please Choose a Drink', font=('Helvetica bold', 13))
        self.drink_choose_frame.pack(pady=10)
        self.drink_choose_label.pack()
        self.radio_2 = IntVar()
        self.drink_coke_frame = Frame(self.root, height=45, width=200)
        self.drink_coke_button = Radiobutton(self.drink_coke_frame, text='Coke: $1.00', font=('Helvetica bold', 15), variable=self.radio_2, value=0, command=self.getdrinkbutton)
        self.drink_coke_label = Label(self.drink_coke_frame, text='How Many:', font=('Helvetica bold', 15))
        self.drink_coke_amount_entry_box = Entry(self.drink_coke_frame, width=2, font=('Helvetica bold', 15))
        self.drink_coke_frame.pack(anchor='w', padx=30, pady=10)
        self.drink_coke_frame.pack_propagate(0)
        self.drink_coke_button.pack(padx=5, side='left')
        self.drink_diet_coke_frame = Frame(self.root, height=45, width=200)
        self.drink_diet_coke_button = Radiobutton(self.drink_diet_coke_frame, text='Diet Coke: $1.00', font=('Helvetica bold', 15), variable=self.radio_2, value=1, command=self.getdrinkbutton)
        self.drink_diet_coke_label = Label(self.drink_diet_coke_frame, text='How Many:', font=('Helvetica bold', 15))
        self.drink_diet_coke_amount_entry_box = Entry(self.drink_diet_coke_frame, width=2, font=('Helvetica bold', 15))
        self.drink_diet_coke_frame.pack(anchor='w', padx=30, pady=10)
        self.drink_diet_coke_frame.pack_propagate(0)
        self.drink_diet_coke_button.pack(padx=5, side='left')
        self.drink_sprite_frame = Frame(self.root, height=45, width=200)
        self.drink_sprite_button = Radiobutton(self.drink_sprite_frame, text='Sprite: $1.00', font=('Helvetica bold', 15), variable=self.radio_2, value=2, command=self.getdrinkbutton)
        self.drink_sprite_label = Label(self.drink_sprite_frame, text='How Many:', font=('Helvetica bold', 15))
        self.drink_sprite_amount_entry_box = Entry(self.drink_sprite_frame, width=2, font=('Helvetica bold', 15))
        self.drink_sprite_frame.pack(anchor='w', padx=30, pady=10)
        self.drink_sprite_frame.pack_propagate(0)
        self.drink_sprite_button.pack(padx=5, side='left')
        self.drink_root_beer_frame = Frame(self.root, height=45, width=200)
        self.drink_root_beer_button = Radiobutton(self.drink_root_beer_frame, text='Root Beer: $1.00', font=('Helvetica bold', 15), variable=self.radio_2, value=3, command=self.getdrinkbutton)
        self.drink_root_beer_label = Label(self.drink_root_beer_frame, text='How Many:', font=('Helvetica bold', 15))
        self.drink_root_beer_amount_entry_box = Entry(self.drink_root_beer_frame, width=2, font=('Helvetica bold', 15))
        self.drink_root_beer_frame.pack(anchor='w', padx=30, pady=10)
        self.drink_root_beer_frame.pack_propagate(0)
        self.drink_root_beer_button.pack(padx=5, side='left')
        self.drink_fanta_frame = Frame(self.root, height=45, width=200)
        self.drink_fanta_button = Radiobutton(self.drink_fanta_frame, text='Fanta: $1.00', font=('Helvetica bold', 15), variable=self.radio_2, value=4, command=self.getdrinkbutton)
        self.drink_fanta_label = Label(self.drink_fanta_frame, text='How Many:', font=('Helvetica bold', 15))
        self.drink_fanta_amount_entry_box = Entry(self.drink_fanta_frame, width=2, font=('Helvetica bold', 15))
        self.drink_fanta_frame.pack(anchor='w', padx=30, pady=10)
        self.drink_fanta_frame.pack_propagate(0)
        self.drink_fanta_button.pack(padx=5, side='left')
        self.radio_2.set(None)
        
        self.drink_button_frame = Frame(self.root, bg='purple')
        self.drink_back_button = Button(self.drink_button_frame, text='BACK TO MENU', font=('Helvetica bold', 15), command=self.drinkbackclicked)
        self.drink_next_button = Button(self.drink_button_frame, text='ADD TO ORDER', font=('Helvetica bold', 15), command=self.drinkaddclicked)
        self.drink_button_frame.pack(pady=30)
        self.drink_back_button.pack(padx= 30, side='left')   
        self.drink_next_button.pack(padx= 30, side='right')
        
    def drink_pack_forget(self) -> None:
        '''
        Method to delete the frames from the drink menu screen.
        '''
        self.drink_header_frame.pack_forget()
        self.drink_choose_frame.pack_forget()
        self.drink_coke_frame.pack_forget()
        self.drink_diet_coke_frame.pack_forget()
        self.drink_sprite_frame.pack_forget()
        self.drink_root_beer_frame.pack_forget()
        self.drink_fanta_frame.pack_forget()
        self.drink_button_frame.pack_forget()
        
    def drinkbackclicked(self) -> None:
        '''
        Method to delete the frames from the drink menu screen and create the main menu screen if the customer
        does not want to get a drink and return to the main menu.
        '''
        self.drink_pack_forget()
        self.make_main()
        
    def drinkaddclicked(self) -> None:
        '''
        Method to add the drink and amount the customer chooses to the cart then have a message box pop up saying the selection
        has been added to the cart. Once that happens the drink menu screen will be deleted and the main menu screen
        will be created.
        '''
        try:
            drink_choice_order_save = self.radio_2.get()
            if drink_choice_order_save == 0:
                if int(self.drink_coke_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_coke_quantity_total += int(self.drink_coke_amount_entry_box.get())
                    self.customer_total_coke_price = self.customer_coke_quantity_total
                    if self.check_coke_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_coke_in_list)
                        self.customer_cart_list.append(f'{self.customer_coke_quantity_total} Cokes at $1.00 is ${self.customer_total_coke_price:.2f}')
                        self.customer_order_amount +=  int(self.drink_coke_amount_entry_box.get()) * 1.00
                        self.check_coke_in_list = f'{self.customer_coke_quantity_total} Cokes at $1.00 is ${self.customer_total_coke_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_coke_quantity_total} Cokes at $1.00 is ${self.customer_total_coke_price:.2f}')
                        self.check_coke_in_list = f'{self.customer_coke_quantity_total} Cokes at $1.00 is ${self.customer_total_coke_price:.2f}'
                        self.customer_order_amount += int(self.drink_coke_amount_entry_box.get()) * 1.00
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.drink_pack_forget()
                    self.make_main()
            elif drink_choice_order_save == 1:
                if int(self.drink_diet_coke_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_diet_coke_quantity_total += int(self.drink_diet_coke_amount_entry_box.get())
                    self.customer_total_diet_coke_price = self.customer_diet_coke_quantity_total
                    if self.check_diet_coke_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_diet_coke_in_list)
                        self.customer_cart_list.append(f'{self.customer_diet_coke_quantity_total} Diet Cokes at $1.00 is ${self.customer_total_diet_coke_price:.2f}')
                        self.customer_order_amount += int(self.drink_diet_coke_amount_entry_box.get()) * 1.00
                        self.check_diet_coke_in_list = f'{self.customer_diet_coke_quantity_total} Diet Cokes at $1.00 is ${self.customer_total_diet_coke_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_diet_coke_quantity_total} Diet Cokes at $1.00 is ${self.customer_total_diet_coke_price:.2f}')
                        self.check_diet_coke_in_list = f'{self.customer_diet_coke_quantity_total} Diet Cokes at $1.00 is ${self.customer_total_diet_coke_price:.2f}'
                        self.customer_order_amount += int(self.drink_diet_coke_amount_entry_box.get()) * 1.00
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.drink_pack_forget()
                    self.make_main()
            elif drink_choice_order_save == 2:
                if int(self.drink_sprite_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_sprite_quantity_total += int(self.drink_sprite_amount_entry_box.get())
                    self.customer_total_sprite_price = self.customer_sprite_quantity_total
                    if self.check_sprite_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_sprite_in_list)
                        self.customer_cart_list.append(f'{self.customer_sprite_quantity_total} Sprites at $1.00 is ${self.customer_total_sprite_price:.2f}')
                        self.customer_order_amount += int(self.drink_sprite_amount_entry_box.get()) * 1.00
                        self.check_sprite_in_list = f'{self.customer_sprite_quantity_total} Sprites at $1.00 is ${self.customer_total_sprite_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_sprite_quantity_total} Sprites at $1.00 is ${self.customer_total_sprite_price:.2f}')
                        self.check_sprite_in_list = f'{self.customer_sprite_quantity_total} Sprites at $1.00 is ${self.customer_total_sprite_price:.2f}'
                        self.customer_order_amount += int(self.drink_sprite_amount_entry_box.get()) * 1.00
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.drink_pack_forget()
                    self.make_main()
            elif drink_choice_order_save == 3:
                if int(self.drink_root_beer_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_root_beer_quantity_total += int(self.drink_root_beer_amount_entry_box.get())
                    self.customer_total_root_beer_price = self.customer_root_beer_quantity_total
                    if self.check_root_beer_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_root_beer_in_list)
                        self.customer_cart_list.append(f'{self.customer_root_beer_quantity_total} Root Beers at $1.00 is ${self.customer_total_root_beer_price:.2f}')
                        self.customer_order_amount += int(self.drink_root_beer_amount_entry_box.get()) * 1.00
                        self.check_root_beer_in_list = f'{self.customer_root_beer_quantity_total} Root Beers at $1.00 is ${self.customer_total_root_beer_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_root_beer_quantity_total} Root Beers at $1.00 is ${self.customer_total_root_beer_price:.2f}')
                        self.check_root_beer_in_list = f'{self.customer_root_beer_quantity_total} Root Beers at $1.00 is ${self.customer_total_root_beer_price:.2f}'
                        self.customer_order_amount += int(self.drink_root_beer_amount_entry_box.get()) * 1.00
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.drink_pack_forget()
                    self.make_main()    
            elif drink_choice_order_save == 4:
                if int(self.drink_fanta_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_fanta_quantity_total += int(self.drink_fanta_amount_entry_box.get())
                    self.customer_total_fanta_price = self.customer_fanta_quantity_total
                    if self.check_fanta_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_fanta_in_list)
                        self.customer_cart_list.append(f'{self.customer_fanta_quantity_total} Fantas at $1.00 is ${self.customer_total_fanta_price:.2f}')
                        self.customer_order_amount += int(self.drink_fanta_amount_entry_box.get()) * 1.00
                        self.check_fanta_in_list = f'{self.customer_fanta_quantity_total} Fantas at $1.00 is ${self.customer_total_fanta_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_fanta_quantity_total} Fantas at $1.00 is ${self.customer_total_fanta_price:.2f}')
                        self.check_fanta_in_list = f'{self.customer_fanta_quantity_total} Fantas at $1.00 is ${self.customer_total_fanta_price:.2f}'
                        self.customer_order_amount += int(self.drink_fanta_amount_entry_box.get()) * 1.00
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.drink_pack_forget()
                    self.make_main()
        except:
            messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
        
    def getdrinkbutton(self) -> None:
        '''
        Method to create an amount entry box for the particular drink the customer would like.
        '''
        self.drink_coke_frame.config(height=45, width=200)
        self.drink_coke_amount_entry_box.pack_forget()
        self.drink_coke_label.pack_forget()
        self.drink_diet_coke_frame.config(height=45, width=200)
        self.drink_diet_coke_amount_entry_box.pack_forget()
        self.drink_diet_coke_label.pack_forget()
        self.drink_sprite_frame.config(height=45, width=200)
        self.drink_sprite_amount_entry_box.pack_forget()
        self.drink_sprite_label.pack_forget()
        self.drink_root_beer_frame.config(height=45, width=200)
        self.drink_root_beer_amount_entry_box.pack_forget()
        self.drink_root_beer_label.pack_forget()
        self.drink_fanta_frame.config(height=45, width=200)
        self.drink_fanta_amount_entry_box.pack_forget()
        self.drink_fanta_label.pack_forget()
        
        drink_choice_save = self.radio_2.get()
        try:
            if drink_choice_save == 0:
                self.drink_coke_frame.config(height=45, width=350)
                self.drink_coke_amount_entry_box.pack(padx=5, side='right')    
                self.drink_coke_label.pack(padx=5, side='right')
                self.drink_coke_amount_entry_box.focus_set()
                self.drink_coke_amount_entry_box.delete(0, END)
            elif drink_choice_save == 1:
                self.drink_diet_coke_frame.config(height=45, width=350)
                self.drink_diet_coke_amount_entry_box.pack(padx=5, side='right')    
                self.drink_diet_coke_label.pack(padx=5, side='right')
                self.drink_diet_coke_amount_entry_box.focus_set()
                self.drink_diet_coke_amount_entry_box.delete(0, END)
            elif drink_choice_save == 2:
                self.drink_sprite_frame.config(height=45, width=350)
                self.drink_sprite_amount_entry_box.pack(padx=5, side='right')    
                self.drink_sprite_label.pack(padx=5, side='right')
                self.drink_sprite_amount_entry_box.focus_set()
                self.drink_sprite_amount_entry_box.delete(0, END)
            elif drink_choice_save == 3:
                self.drink_root_beer_frame.config(height=45, width=350)
                self.drink_root_beer_amount_entry_box.pack(padx=5, side='right')    
                self.drink_root_beer_label.pack(padx=5, side='right')
                self.drink_root_beer_amount_entry_box.focus_set()
                self.drink_root_beer_amount_entry_box.delete(0, END)
            elif drink_choice_save == 4:
                self.drink_fanta_frame.config(height=45, width=350)
                self.drink_fanta_amount_entry_box.pack(padx=5, side='right')    
                self.drink_fanta_label.pack(padx=5, side='right')
                self.drink_fanta_amount_entry_box.focus_set()
                self.drink_fanta_amount_entry_box.delete(0, END)
        except:
            messagebox.showinfo('NO SELECTION', 'You Did Not Make a Selection!')

    def sandwich_menu(self) -> None:
        '''
        Method to create the frames, labels, radio buttons, back to menu button, and add to cart button
        for the sandwich choices the customer may chose from.
        '''
        self.root.configure(bg='purple')
        self.sandwich_header_frame = Frame(self.root)
        self.sandwich_header_label = Label(self.sandwich_header_frame, text='Sandwich Menu', font=('Helvetica bold', 35))
        self.sandwich_header_frame.pack(pady=5)
        self.sandwich_header_label.pack()
        self.sandwich_choose_frame = Frame(self.root)
        self.sandwich_choose_label = Label(self.sandwich_choose_frame, text='Please Choose a Sandwich', font=('Helvetica bold', 13))
        self.sandwich_choose_frame.pack(pady=10)
        self.sandwich_choose_label.pack()
        self.radio_3 = IntVar()
        self.hamburger_frame = Frame(self.root, height=45, width=250)
        self.hamburger_button = Radiobutton(self.hamburger_frame, text='Hamburger: $19.99', font=('Helvetica bold', 15), variable=self.radio_3, value=0, command=self.getsandwichbutton)
        self.hamburger_label = Label(self.hamburger_frame, text='How Many:', font=('Helvetica bold', 15))
        self.hamburger_amount_entry_box = Entry(self.hamburger_frame, width=2, font=('Helvetica bold', 15))
        self.hamburger_frame.pack(anchor='w', padx=30, pady=10)
        self.hamburger_frame.pack_propagate(0)
        self.hamburger_button.pack(padx=5, side='left')
        self.cheeseburger_frame = Frame(self.root, height=45, width=250)
        self.cheeseburger_button = Radiobutton(self.cheeseburger_frame, text='Cheeseburger: $19.99', font=('Helvetica bold', 15), variable=self.radio_3, value=1, command=self.getsandwichbutton)
        self.cheeseburger_label = Label(self.cheeseburger_frame, text='How Many:', font=('Helvetica bold', 15))
        self.cheeseburger_amount_entry_box = Entry(self.cheeseburger_frame, width=2, font=('Helvetica bold', 15))
        self.cheeseburger_frame.pack(anchor='w', padx=30, pady=10)
        self.cheeseburger_frame.pack_propagate(0)
        self.cheeseburger_button.pack(padx=5, side='left')
        self.crispy_chicken_frame = Frame(self.root, height=45, width=250)
        self.crispy_chicken_button = Radiobutton(self.crispy_chicken_frame, text='Crispy Chicken: $19.99', font=('Helvetica bold', 15), variable=self.radio_3, value=2, command=self.getsandwichbutton)
        self.crispy_chicken_label = Label(self.crispy_chicken_frame, text='How Many:', font=('Helvetica bold', 15))
        self.crispy_chicken_amount_entry_box = Entry(self.crispy_chicken_frame, width=2, font=('Helvetica bold', 15))
        self.crispy_chicken_frame.pack(anchor='w', padx=30, pady=10)
        self.crispy_chicken_frame.pack_propagate(0)
        self.crispy_chicken_button.pack(padx=5, side='left')
        self.radio_3.set(None)
        
        self.sandwich_button_frame = Frame(self.root, bg='purple')
        self.sandwich_back_button = Button(self.sandwich_button_frame, text='BACK TO MENU', font=('Helvetica bold', 15), command=self.sandwichbackclicked)
        self.sandwich_next_button = Button(self.sandwich_button_frame, text='ADD TO CART', font=('Helvetica bold', 15), command=self.sandwichnextclicked)
        self.sandwich_button_frame.pack(pady=30)
        self.sandwich_back_button.pack(padx= 30, side='left') 
        self.sandwich_next_button.pack(padx= 30, side='right')
        
    def getsandwichbutton(self) -> None:
        '''
        Method to create an amount entry box for the particular sandwich the customer would like.
        '''
        self.hamburger_frame.config(height=45, width=250)
        self.hamburger_amount_entry_box.pack_forget()
        self.hamburger_label.pack_forget()
        self.cheeseburger_frame.config(height=45, width=250)
        self.cheeseburger_amount_entry_box.pack_forget()
        self.cheeseburger_label.pack_forget()
        self.crispy_chicken_frame.config(height=45, width=250)
        self.crispy_chicken_amount_entry_box.pack_forget()
        self.crispy_chicken_label.pack_forget()
        
        sandwich_choice_save = self.radio_3.get()
        try:
            if sandwich_choice_save == 0:
                self.hamburger_frame.config(height=45, width=400)
                self.hamburger_amount_entry_box.pack(padx=5, side='right')    
                self.hamburger_label.pack(padx=5, side='right')
                self.hamburger_amount_entry_box.focus_set()
                self.hamburger_amount_entry_box.delete(0, END)
            elif sandwich_choice_save == 1:
                self.cheeseburger_frame.config(height=45, width=400)
                self.cheeseburger_amount_entry_box.pack(padx=5, side='right')    
                self.cheeseburger_label.pack(padx=5, side='right')
                self.cheeseburger_amount_entry_box.focus_set()
                self.cheeseburger_amount_entry_box.delete(0, END)
            elif sandwich_choice_save == 2:
                self.crispy_chicken_frame.config(height=45, width=400)
                self.crispy_chicken_amount_entry_box.pack(padx=5, side='right')    
                self.crispy_chicken_label.pack(padx=5, side='right')
                self.crispy_chicken_amount_entry_box.focus_set()
                self.crispy_chicken_amount_entry_box.delete(0, END)
        except:
            messagebox.showinfo('NO SELECTION', 'You Did Not Make a Selection!')
        
    def sandwich_pack_forget(self) -> None:
        '''
        Method to delete the frames from the sandwich menu screen.
        '''
        self.sandwich_header_frame.pack_forget()
        self.sandwich_choose_frame.pack_forget()
        self.hamburger_frame.pack_forget()
        self.cheeseburger_frame.pack_forget()
        self.crispy_chicken_frame.pack_forget()
        self.sandwich_button_frame.pack_forget()
    
    def sandwichbackclicked(self) -> None:
        '''
        Method to delete the frames from the sandwich menu screen and create the main menu screen if the customer
        does not want to get a sandwich and return to the main menu.
        '''
        self.sandwich_pack_forget()
        self.make_main()
        
    def sandwichnextclicked(self) -> None:
        '''
        Method to add the sandwich and amount the customer chooses to the cart then have a message box pop up saying the selection
        has been added to the cart. Once that happens the sandwich menu screen will be deleted and the main menu screen
        will be created.
        '''
        try:
            sandwich_choice_order_save = self.radio_3.get()
            if sandwich_choice_order_save == 0:
                if int(self.hamburger_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_hamburger_quantity_total += int(self.hamburger_amount_entry_box.get())
                    self.customer_total_hamburger_price = self.customer_hamburger_quantity_total * 19.99
                    if self.check_hamburger_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_hamburger_in_list)
                        self.customer_cart_list.append(f'{self.customer_hamburger_quantity_total} Hamburgers at $19.99 is ${self.customer_total_hamburger_price:.2f}')
                        self.customer_order_amount +=  int(self.hamburger_amount_entry_box.get()) * 19.99
                        self.check_hamburger_in_list = f'{self.customer_hamburger_quantity_total} Hamburgers at $19.99 is ${self.customer_total_hamburger_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_hamburger_quantity_total} Hamburgers at $19.99 is ${self.customer_total_hamburger_price:.2f}')
                        self.check_hamburger_in_list = f'{self.customer_hamburger_quantity_total} Hamburgers at $19.99 is ${self.customer_total_hamburger_price:.2f}'
                        self.customer_order_amount += int(self.hamburger_amount_entry_box.get()) * 19.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.sandwich_pack_forget()
                    self.make_main()
            elif sandwich_choice_order_save == 1:
                if int(self.cheeseburger_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_cheeseburger_quantity_total += int(self.cheeseburger_amount_entry_box.get())
                    self.customer_total_cheeseburger_price =  self.customer_cheeseburger_quantity_total * 20.99
                    if self.check_cheeseburger_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_cheeseburger_in_list)
                        self.customer_cart_list.append(f'{self.customer_cheeseburger_quantity_total} Cheeseburgers at $20.99 is ${self.customer_total_cheeseburger_price:.2f}')
                        self.customer_order_amount += int(self.cheeseburger_amount_entry_box.get()) * 20.99
                        self.check_cheeseburger_in_list = f'{self.customer_cheeseburger_quantity_total} Cheeseburgers at $20.99 is ${self.customer_total_cheeseburger_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_cheeseburger_quantity_total} Cheeseburgers at $20.99 is ${self.customer_total_cheeseburger_price:.2f}')
                        self.check_cheeseburger_in_list = f'{self.customer_cheeseburger_quantity_total} Cheeseburgers at $20.99 is ${self.customer_total_cheeseburger_price:.2f}'
                        self.customer_order_amount += int(self.cheeseburger_amount_entry_box.get()) * 20.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.sandwich_pack_forget()
                    self.make_main()
            elif sandwich_choice_order_save == 2:
                if int(self.crispy_chicken_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_crispy_chicken_quantity_total += int(self.crispy_chicken_amount_entry_box.get())
                    self.customer_total_crispy_chicken_price = self.customer_crispy_chicken_quantity_total * 19.99
                    if self.check_crispy_chicken_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_crispy_chicken_in_list)
                        self.customer_cart_list.append(f'{self.customer_crispy_chicken_quantity_total} Crispy Chickens at $19.99 is ${self.customer_total_crispy_chicken_price:.2f}')
                        self.customer_order_amount += int(self.crispy_chicken_amount_entry_box.get()) * 19.99
                        self.check_crispy_chicken_in_list = f'{self.customer_crispy_chicken_quantity_total} Crispy Chickens at $19.99 is ${self.customer_total_crispy_chicken_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_crispy_chicken_quantity_total} Crispy Chickens at $19.99 is ${self.customer_total_crispy_chicken_price:.2f}')
                        self.check_crispy_chicken_in_list = f'{self.customer_crispy_chicken_quantity_total} Crispy Chickens at $19.99 is ${self.customer_total_crispy_chicken_price:.2f}'
                        self.customer_order_amount += int(self.crispy_chicken_amount_entry_box.get()) * 19.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.sandwich_pack_forget()
                    self.make_main()
        except:
            messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')

    def pizza_menu(self) -> None:
        '''
        Method to create the frames, labels, radio buttons, back to menu button, and add to cart button
        for the pizza choices the customer may chose from.
        '''
        self.root.configure(bg='brown')
        self.pizza_header_frame = Frame(self.root)
        self.pizza_header_label = Label(self.pizza_header_frame, text='Pizza Menu', font=('Helvetica bold', 35))
        self.pizza_header_frame.pack(pady=5)
        self.pizza_header_label.pack()
        self.pizza_choose_frame = Frame(self.root)
        self.pizza_choose_label = Label(self.pizza_choose_frame, text='Please Choose a Pizza', font=('Helvetica bold', 13))
        self.pizza_choose_frame.pack(pady=10)
        self.pizza_choose_label.pack()
        self.radio_4 = IntVar()
        self.small_pizza_frame = Frame(self.root, height=45, width=250)
        self.small_pizza_button = Radiobutton(self.small_pizza_frame, text='Small Pizza: $9.99', font=('Helvetica bold', 15), variable=self.radio_4, value=0, command=self.getpizzabutton)
        self.small_pizza_label = Label(self.small_pizza_frame, text='How Many:', font=('Helvetica bold', 15))
        self.small_pizza_amount_entry_box = Entry(self.small_pizza_frame, width=2, font=('Helvetica bold', 15))
        self.small_pizza_frame.pack(anchor='w', padx=30, pady=10)
        self.small_pizza_frame.pack_propagate(0)
        self.small_pizza_button.pack(padx=5, side='left')
        self.medium_pizza_frame = Frame(self.root, height=45, width=250)
        self.medium_pizza_button = Radiobutton(self.medium_pizza_frame, text='Medium Pizza: $14.99', font=('Helvetica bold', 15), variable=self.radio_4, value=1, command=self.getpizzabutton)
        self.medium_pizza_label = Label(self.medium_pizza_frame, text='How Many:', font=('Helvetica bold', 15))
        self.medium_pizza_amount_entry_box = Entry(self.medium_pizza_frame, width=2, font=('Helvetica bold', 15))
        self.medium_pizza_frame.pack(anchor='w', padx=30, pady=10)
        self.medium_pizza_frame.pack_propagate(0)
        self.medium_pizza_button.pack(padx=5, side='left')
        self.large_pizza_frame = Frame(self.root, height=45, width=250)
        self.large_pizza_button = Radiobutton(self.large_pizza_frame, text='Large Pizza: $19.99', font=('Helvetica bold', 15), variable=self.radio_4, value=2, command=self.getpizzabutton)
        self.large_pizza_label = Label(self.large_pizza_frame, text='How Many:', font=('Helvetica bold', 15))
        self.large_pizza_amount_entry_box = Entry(self.large_pizza_frame, width=2, font=('Helvetica bold', 15))
        self.large_pizza_frame.pack(anchor='w', padx=30, pady=10)
        self.large_pizza_frame.pack_propagate(0)
        self.large_pizza_button.pack(padx=5, side='left')
        self.radio_4.set(None)
        
        self.pizza_button_frame = Frame(self.root, bg='brown')
        self.pizza_back_button = Button(self.pizza_button_frame, text='BACK TO MENU', font=('Helvetica bold', 15), command=self.pizzabackclicked)
        self.pizza_next_button = Button(self.pizza_button_frame, text='ADD TO CART', font=('Helvetica bold', 15), command=self.pizzanextclicked)
        self.pizza_button_frame.pack(pady=30)
        self.pizza_back_button.pack(padx= 30, side='left') 
        self.pizza_next_button.pack(padx=30, side='right')
        
    def getpizzabutton(self) -> None:
        '''
        Method to create an amount entry box for the particular pizza the customer would like.
        '''
        self.small_pizza_frame.config(height=45, width=250)
        self.small_pizza_amount_entry_box.pack_forget()
        self.small_pizza_label.pack_forget()
        self.medium_pizza_frame.config(height=45, width=250)
        self.medium_pizza_amount_entry_box.pack_forget()
        self.medium_pizza_label.pack_forget()
        self.large_pizza_frame.config(height=45, width=250)
        self.large_pizza_amount_entry_box.pack_forget()
        self.large_pizza_label.pack_forget()
        
        pizza_choice_save = self.radio_4.get()
        try:
            if pizza_choice_save == 0:
                self.small_pizza_frame.config(height=45, width=400)
                self.small_pizza_amount_entry_box.pack(padx=5, side='right')    
                self.small_pizza_label.pack(padx=5, side='right')
                self.small_pizza_amount_entry_box.focus_set()
                self.small_pizza_amount_entry_box.delete(0, END)
            elif pizza_choice_save == 1:
                self.medium_pizza_frame.config(height=45, width=400)
                self.medium_pizza_amount_entry_box.pack(padx=5, side='right')    
                self.medium_pizza_label.pack(padx=5, side='right')
                self.medium_pizza_amount_entry_box.focus_set()
                self.medium_pizza_amount_entry_box.delete(0, END)
            elif pizza_choice_save == 2:
                self.large_pizza_frame.config(height=45, width=400)
                self.large_pizza_amount_entry_box.pack(padx=5, side='right')    
                self.large_pizza_label.pack(padx=5, side='right')
                self.large_pizza_amount_entry_box.focus_set()
                self.large_pizza_amount_entry_box.delete(0, END)
        except:
            messagebox.showinfo('NO SELECTION', 'You Did Not Make a Selection!')
        
    def pizza_pack_forget(self) -> None:
        '''
        Method to delete the frames from the pizza menu screen.
        '''
        self.pizza_header_frame.pack_forget()
        self.pizza_choose_frame.pack_forget()
        self.small_pizza_frame.pack_forget()
        self.medium_pizza_frame.pack_forget()
        self.large_pizza_frame.pack_forget()
        self.pizza_button_frame.pack_forget()
        
    def pizzabackclicked(self) -> None:
        '''
        Method to delete the frames from the pizza menu screen and create the main menu screen if the customer
        does not want to get a pizza and return to the main menu.
        '''
        self.pizza_pack_forget()
        self.make_main()
        
    def pizzanextclicked(self) -> None:
        '''
        Method to add the pizza and amount the customer chooses to the cart then have a message box pop up saying the selection
        has been added to the cart. Once that happens the pizza menu screen will be deleted and the main menu screen
        will be created.
        '''
        try:
            pizza_choice_order_save = self.radio_4.get()
            if pizza_choice_order_save == 0:
                if int(self.small_pizza_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_small_pizza_quantity_total += int(self.small_pizza_amount_entry_box.get())
                    self.customer_total_small_pizza_price = self.customer_small_pizza_quantity_total * 9.99
                    if self.check_small_pizza_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_small_pizza_in_list)
                        self.customer_cart_list.append(f'{self.customer_small_pizza_quantity_total} Small Pizzas at $9.99 is ${self.customer_total_small_pizza_price:.2f}')
                        self.customer_order_amount +=  int(self.small_pizza_amount_entry_box.get()) * 9.99
                        self.check_small_pizza_in_list = f'{self.customer_small_pizza_quantity_total} Small Pizzas at $9.99 is ${self.customer_total_small_pizza_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_small_pizza_quantity_total} Small Pizzas at $9.99 is ${self.customer_total_small_pizza_price:.2f}')
                        self.check_small_pizza_in_list = f'{self.customer_small_pizza_quantity_total} Small Pizzas at $9.99 is ${self.customer_total_small_pizza_price:.2f}'
                        self.customer_order_amount += int(self.small_pizza_amount_entry_box.get()) * 9.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.pizza_pack_forget()
                    self.make_main()
            elif pizza_choice_order_save == 1:
                if int(self.medium_pizza_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_medium_pizza_quantity_total += int(self.medium_pizza_amount_entry_box.get())
                    self.customer_total_medium_pizza_price =  self.customer_medium_pizza_quantity_total * 14.99
                    if self.check_medium_pizza_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_medium_pizza_in_list)
                        self.customer_cart_list.append(f'{self.customer_medium_pizza_quantity_total} medium_pizzas at $14.99 is ${self.customer_total_medium_pizza_price:.2f}')
                        self.customer_order_amount += int(self.medium_pizza_amount_entry_box.get()) * 14.99
                        self.check_medium_pizza_in_list = f'{self.customer_medium_pizza_quantity_total} medium_pizzas at $14.99 is ${self.customer_total_medium_pizza_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_medium_pizza_quantity_total} medium_pizzas at $14.99 is ${self.customer_total_medium_pizza_price:.2f}')
                        self.check_medium_pizza_in_list = f'{self.customer_medium_pizza_quantity_total} medium_pizzas at $14.99 is ${self.customer_total_medium_pizza_price:.2f}'
                        self.customer_order_amount += int(self.medium_pizza_amount_entry_box.get()) * 14.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.pizza_pack_forget()
                    self.make_main()
            elif pizza_choice_order_save == 2:
                if int(self.large_pizza_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_large_pizza_quantity_total += int(self.large_pizza_amount_entry_box.get())
                    self.customer_total_large_pizza_price = self.customer_large_pizza_quantity_total * 19.99
                    if self.check_large_pizza_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_large_pizza_in_list)
                        self.customer_cart_list.append(f'{self.customer_large_pizza_quantity_total} Large Pizzas at $19.99 is ${self.customer_total_large_pizza_price:.2f}')
                        self.customer_order_amount += int(self.large_pizza_amount_entry_box.get()) * 19.99
                        self.check_large_pizza_in_list = f'{self.customer_large_pizza_quantity_total} Large Pizzas at $19.99 is ${self.customer_total_large_pizza_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_large_pizza_quantity_total} Large Pizzas at $19.99 is ${self.customer_total_large_pizza_price:.2f}')
                        self.check_large_pizza_in_list = f'{self.customer_large_pizza_quantity_total} Large Pizzas at $19.99 is ${self.customer_total_large_pizza_price:.2f}'
                        self.customer_order_amount += int(self.large_pizza_amount_entry_box.get()) * 19.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.pizza_pack_forget()
                    self.make_main()
        except:
            messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')

    def pasta_menu(self) -> None:
        '''
        Method to create the frames, labels, radio buttons, back to menu button, and add to cart button
        for the pasta choices the customer may chose from.
        '''
        self.root.configure(bg='magenta')
        self.pasta_header_frame = Frame(self.root)
        self.pasta_header_label = Label(self.pasta_header_frame, text='Pasta Menu', font=('Helvetica bold', 35))
        self.pasta_header_frame.pack(pady=5)
        self.pasta_header_label.pack()
        self.pasta_choose_frame = Frame(self.root)
        self.pasta_choose_label = Label(self.pasta_choose_frame, text='Please Choose a Pasta', font=('Helvetica bold', 15))
        self.pasta_choose_frame.pack(pady=10)
        self.pasta_choose_label.pack()
        self.radio_5 = IntVar()
        self.spaghetti_frame = Frame(self.root, height=45, width=300)
        self.spaghetti_button = Radiobutton(self.spaghetti_frame, text='Spaghetti: $19.99', font=('Helvetica bold', 15), variable=self.radio_5, value=0, command=self.getpastabutton)
        self.spaghetti_label = Label(self.spaghetti_frame, text='How Many:', font=('Helvetica bold', 15))
        self.spaghetti_amount_entry_box = Entry(self.spaghetti_frame, width=2, font=('Helvetica bold', 15))
        self.spaghetti_frame.pack(anchor='w', padx=30, pady=10)
        self.spaghetti_frame.pack_propagate(0)
        self.spaghetti_button.pack(padx=5, side='left')
        self.chicken_alfredo_frame = Frame(self.root, height=45, width=300)
        self.chicken_alfredo_button = Radiobutton(self.chicken_alfredo_frame, text='Chicken Alfredo: $19.99', font=('Helvetica bold', 15), variable=self.radio_5, value=1, command=self.getpastabutton)
        self.chicken_alfredo_label = Label(self.chicken_alfredo_frame, text='How Many:', font=('Helvetica bold', 15))
        self.chicken_alfredo_amount_entry_box = Entry(self.chicken_alfredo_frame, width=2, font=('Helvetica bold', 15))
        self.chicken_alfredo_frame.pack(anchor='w', padx=30, pady=10)
        self.chicken_alfredo_frame.pack_propagate(0)
        self.chicken_alfredo_button.pack(padx=5, side='left')
        self.chicken_parmesan_frame = Frame(self.root, height=45, width=300)
        self.chicken_parmesan_button = Radiobutton(self.chicken_parmesan_frame, text='Chicken Parmesan: $19.99', font=('Helvetica bold', 15), variable=self.radio_5, value=2, command=self.getpastabutton)
        self.chicken_parmesan_label = Label(self.chicken_parmesan_frame, text='How Many:', font=('Helvetica bold', 15))
        self.chicken_parmesan_amount_entry_box = Entry(self.chicken_parmesan_frame, width=2, font=('Helvetica bold', 15))
        self.chicken_parmesan_frame.pack(anchor='w', padx=30, pady=10)
        self.chicken_parmesan_frame.pack_propagate(0)
        self.chicken_parmesan_button.pack(padx=5, side='left')
        self.radio_5.set(None)
        
        self.pasta_button_frame = Frame(self.root, bg='magenta')
        self.pasta_back_button = Button(self.pasta_button_frame, text='BACK TO MENU', font=('Helvetica bold', 15), command=self.pastabackclicked)
        self.pasta_next_button = Button(self.pasta_button_frame, text='ADD TO CART', font=('Helvetica bold', 15), command=self.pastanextclicked)
        self.pasta_button_frame.pack(pady=30)
        self.pasta_back_button.pack(padx= 30, side='left') 
        self.pasta_next_button.pack(padx= 30, side='right')
        
    def getpastabutton(self) -> None:
        '''
        Method to create an amount entry box for the particular pasta the customer would like.
        '''
        self.spaghetti_frame.config(height=45, width=300)
        self.spaghetti_amount_entry_box.pack_forget()
        self.spaghetti_label.pack_forget()
        self.chicken_alfredo_frame.config(height=45, width=300)
        self.chicken_alfredo_amount_entry_box.pack_forget()
        self.chicken_alfredo_label.pack_forget()
        self.chicken_parmesan_frame.config(height=45, width=300)
        self.chicken_parmesan_amount_entry_box.pack_forget()
        self.chicken_parmesan_label.pack_forget()
        
        pasta_choice_save = self.radio_5.get()
        try:
            if pasta_choice_save == 0:
                self.spaghetti_frame.config(height=45, width=450)
                self.spaghetti_amount_entry_box.pack(padx=5, side='right')    
                self.spaghetti_label.pack(padx=5, side='right')
                self.spaghetti_amount_entry_box.focus_set()
                self.spaghetti_amount_entry_box.delete(0, END)
            elif pasta_choice_save == 1:
                self.chicken_alfredo_frame.config(height=45, width=450)
                self.chicken_alfredo_amount_entry_box.pack(padx=5, side='right')    
                self.chicken_alfredo_label.pack(padx=5, side='right')
                self.chicken_alfredo_amount_entry_box.focus_set()
                self.chicken_alfredo_amount_entry_box.delete(0, END)
            elif pasta_choice_save == 2:
                self.chicken_parmesan_frame.config(height=45, width=450)
                self.chicken_parmesan_amount_entry_box.pack(padx=5, side='right')    
                self.chicken_parmesan_label.pack(padx=5, side='right')
                self.chicken_parmesan_amount_entry_box.focus_set()
                self.chicken_parmesan_amount_entry_box.delete(0, END)
        except:
            messagebox.showinfo('NO SELECTION', 'You Did Not Make a Selection!')

    def pasta_pack_forget(self) -> None:
        '''
        Method to delete the frames from the pasta menu screen.
        '''
        self.pasta_header_frame.pack_forget()
        self.pasta_choose_frame.pack_forget()
        self.spaghetti_frame.pack_forget()
        self.chicken_alfredo_frame.pack_forget()
        self.chicken_parmesan_frame.pack_forget()
        self.pasta_button_frame.pack_forget()

    def pastabackclicked(self) -> None:
        '''
        Method to delete the frames from the pasta menu screen and create the main menu screen if the customer
        does not want to get a pasta and return to the main menu.
        '''
        self.pasta_pack_forget()
        self.make_main()
        
    def pastanextclicked(self) -> None:
        '''
        Method to add the pasta and amount the customer chooses to the cart then have a message box pop up saying the selection
        has been added to the cart. Once that happens the pasta menu screen will be deleted and the main menu screen
        will be created.
        '''
        try:
            pasta_choice_order_save = self.radio_5.get()
            if pasta_choice_order_save == 0:
                if int(self.spaghetti_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_spaghetti_quantity_total += int(self.spaghetti_amount_entry_box.get())
                    self.customer_total_spaghetti_price = self.customer_spaghetti_quantity_total * 19.99
                    if self.check_spaghetti_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_spaghetti_in_list)
                        self.customer_cart_list.append(f'{self.customer_spaghetti_quantity_total} Spaghettis at $19.99 is ${self.customer_total_spaghetti_price:.2f}')
                        self.customer_order_amount +=  int(self.spaghetti_amount_entry_box.get()) * 19.99
                        self.check_spaghetti_in_list = f'{self.customer_spaghetti_quantity_total} Spaghettis at $19.99 is ${self.customer_total_spaghetti_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_spaghetti_quantity_total} Spaghettis at $19.99 is ${self.customer_total_spaghetti_price:.2f}')
                        self.check_spaghetti_in_list = f'{self.customer_spaghetti_quantity_total} Spaghettis at $19.99 is ${self.customer_total_spaghetti_price:.2f}'
                        self.customer_order_amount += int(self.spaghetti_amount_entry_box.get()) * 19.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.pasta_pack_forget()
                    self.make_main()
            elif pasta_choice_order_save == 1:
                if int(self.chicken_alfredo_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_chicken_alfredo_quantity_total += int(self.chicken_alfredo_amount_entry_box.get())
                    self.customer_total_chicken_alfredo_price =  self.customer_chicken_alfredo_quantity_total * 19.99
                    if self.check_chicken_alfredo_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_chicken_alfredo_in_list)
                        self.customer_cart_list.append(f'{self.customer_chicken_alfredo_quantity_total} Chicken Alfredos at $19.99 is ${self.customer_total_chicken_alfredo_price:.2f}')
                        self.customer_order_amount += int(self.chicken_alfredo_amount_entry_box.get()) * 19.99
                        self.check_chicken_alfredo_in_list = f'{self.customer_chicken_alfredo_quantity_total} Chicken Alfredos at $19.99 is ${self.customer_total_chicken_alfredo_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_chicken_alfredo_quantity_total} Chicken Alfredos at $19.99 is ${self.customer_total_chicken_alfredo_price:.2f}')
                        self.check_chicken_alfredo_in_list = f'{self.customer_chicken_alfredo_quantity_total} Chicken Alfredos at $19.99 is ${self.customer_total_chicken_alfredo_price:.2f}'
                        self.customer_order_amount += int(self.chicken_alfredo_amount_entry_box.get()) * 19.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.pasta_pack_forget()
                    self.make_main()
            elif pasta_choice_order_save == 2:
                if int(self.chicken_parmesan_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_chicken_parmesan_quantity_total += int(self.chicken_parmesan_amount_entry_box.get())
                    self.customer_total_chicken_parmesan_price = self.customer_chicken_parmesan_quantity_total * 19.99
                    if self.check_chicken_parmesan_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_chicken_parmesan_in_list)
                        self.customer_cart_list.append(f'{self.customer_chicken_parmesan_quantity_total} Chicken Parmesans at $19.99 is ${self.customer_total_chicken_parmesan_price:.2f}')
                        self.customer_order_amount += int(self.chicken_parmesan_amount_entry_box.get()) * 19.99
                        self.check_chicken_parmesan_in_list = f'{self.customer_chicken_parmesan_quantity_total} Chicken Parmesans at $19.99 is ${self.customer_total_chicken_parmesan_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_chicken_parmesan_quantity_total} Chicken Parmesans at $19.99 is ${self.customer_total_chicken_parmesan_price:.2f}')
                        self.check_chicken_parmesan_in_list = f'{self.customer_chicken_parmesan_quantity_total} Chicken Parmesans at $19.99 is ${self.customer_total_chicken_parmesan_price:.2f}'
                        self.customer_order_amount += int(self.chicken_parmesan_amount_entry_box.get()) * 19.99
                    self.pasta_pack_forget()
                    self.make_main()
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
        except:
            messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')

    def salad_menu(self) -> None:
        '''
        Method to create the frames, labels, radio buttons, back to menu button, and add to cart button
        for the salad choices the customer may chose from.
        '''
        self.root.configure(bg='cyan')
        self.salad_header_frame = Frame(self.root)
        self.salad_header_label = Label(self.salad_header_frame, text='Salad Menu', font=('Helvetica bold', 35))
        self.salad_header_frame.pack(pady=5)
        self.salad_header_label.pack()
        self.salad_choose_frame = Frame(self.root)
        self.salad_choose_label = Label(self.salad_choose_frame, text='Please Choose a Salad', font=('Helvetica bold', 15))
        self.salad_choose_frame.pack(pady=10)
        self.salad_choose_label.pack()
        self.radio_6 = IntVar()
        self.chicken_ceasar_frame = Frame(self.root, height=45, width=270)
        self.chicken_ceasar_button = Radiobutton(self.chicken_ceasar_frame, text='Chicken Ceasar: $12.99', font=('Helvetica bold', 15), variable=self.radio_6, value=0, command=self.getsaladbutton)
        self.chicken_ceasar_label = Label(self.chicken_ceasar_frame, text='How Many:', font=('Helvetica bold', 15))
        self.chicken_ceasar_amount_entry_box = Entry(self.chicken_ceasar_frame, width=2, font=('Helvetica bold', 15))
        self.chicken_ceasar_frame.pack(anchor='w', padx=30, pady=10)
        self.chicken_ceasar_frame.pack_propagate(0)
        self.chicken_ceasar_button.pack(padx=5, side='left')
        self.greek_frame = Frame(self.root, height=45, width=270)
        self.greek_button = Radiobutton(self.greek_frame, text='Greek: $9.99', font=('Helvetica bold', 15), variable=self.radio_6, value=1, command=self.getsaladbutton)
        self.greek_label = Label(self.greek_frame, text='How Many:', font=('Helvetica bold', 15))
        self.greek_amount_entry_box = Entry(self.greek_frame, width=2, font=('Helvetica bold', 15))
        self.greek_frame.pack(anchor='w', padx=30, pady=10)
        self.greek_frame.pack_propagate(0)
        self.greek_button.pack(padx=5, side='left')
        self.asian_sesame_frame = Frame(self.root, height=45, width=270)
        self.asian_sesame_button = Radiobutton(self.asian_sesame_frame, text='Asian Sesame: $9.99', font=('Helvetica bold', 15), variable=self.radio_6, value=2, command=self.getsaladbutton)
        self.asian_sesame_label = Label(self.asian_sesame_frame, text='How Many:', font=('Helvetica bold', 15))
        self.asian_sesame_amount_entry_box = Entry(self.asian_sesame_frame, width=2, font=('Helvetica bold', 15))
        self.asian_sesame_frame.pack(anchor='w', padx=30, pady=10)
        self.asian_sesame_frame.pack_propagate(0)
        self.asian_sesame_button.pack(padx=5, side='left')
        self.radio_6.set(None)
        
        self.salad_button_frame = Frame(self.root, bg='cyan')
        self.salad_back_button = Button(self.salad_button_frame, text='BACK TO MENU', font=('Helvetica bold', 15), command=self.saladbackclicked)
        self.salad_next_button = Button(self.salad_button_frame, text='ADD TO CART', font=('Helvetica bold', 15), command=self.saladnextclicked)
        self.salad_button_frame.pack(pady=30)
        self.salad_back_button.pack(padx= 30, side='left') 
        self.salad_next_button.pack(padx= 30, side='right')
        
    def getsaladbutton(self) -> None:
        '''
        Method to create an amount entry box for the particular salad the customer would like.
        '''
        self.chicken_ceasar_frame.config(height=45, width=270)
        self.chicken_ceasar_amount_entry_box.pack_forget()
        self.chicken_ceasar_label.pack_forget()
        self.greek_frame.config(height=45, width=270)
        self.greek_amount_entry_box.pack_forget()
        self.greek_label.pack_forget()
        self.asian_sesame_frame.config(height=45, width=270)
        self.asian_sesame_amount_entry_box.pack_forget()
        self.asian_sesame_label.pack_forget()
        
        salad_choice_save = self.radio_6.get()
        try:
            if salad_choice_save == 0:
                self.chicken_ceasar_frame.config(height=45, width=420)
                self.chicken_ceasar_amount_entry_box.pack(padx=5, side='right')    
                self.chicken_ceasar_label.pack(padx=5, side='right')
                self.chicken_ceasar_amount_entry_box.focus_set()
                self.chicken_ceasar_amount_entry_box.delete(0, END)
            elif salad_choice_save == 1:
                self.greek_frame.config(height=45, width=420)
                self.greek_amount_entry_box.pack(padx=5, side='right')    
                self.greek_label.pack(padx=5, side='right')
                self.greek_amount_entry_box.focus_set()
                self.greek_amount_entry_box.delete(0, END)
            elif salad_choice_save == 2:
                self.asian_sesame_frame.config(height=45, width=420)
                self.asian_sesame_amount_entry_box.pack(padx=5, side='right')    
                self.asian_sesame_label.pack(padx=5, side='right')
                self.asian_sesame_amount_entry_box.focus_set()
                self.asian_sesame_amount_entry_box.delete(0, END)
        except:
            messagebox.showinfo('NO SELECTION', 'You Did Not Make a Selection!')
        
    def salad_pack_forget(self) -> None:
        '''
        Method to delete the frames from the salad menu screen.
        '''
        self.salad_header_frame.pack_forget()
        self.salad_choose_frame.pack_forget()
        self.chicken_ceasar_frame.pack_forget()
        self.greek_frame.pack_forget()
        self.asian_sesame_frame.pack_forget()
        self.salad_button_frame.pack_forget()
        
    def saladbackclicked(self) -> None:
        '''
        Method to delete the frames from the salad menu screen and create the main menu screen if the customer
        does not want to get a salad and return to the main menu.
        '''
        self.salad_pack_forget()
        self.make_main()
        
    def saladnextclicked(self) -> None:
        '''
        Method to add the salad and amount the customer chooses to the cart then have a message box pop up saying the selection
        has been added to the cart. Once that happens the salad menu screen will be deleted and the main menu screen
        will be created.
        '''
        try:
            salad_choice_order_save = self.radio_6.get()
            if salad_choice_order_save == 0:
                if int(self.chicken_ceasar_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_chicken_ceasar_quantity_total += int(self.chicken_ceasar_amount_entry_box.get())
                    self.customer_total_chicken_ceasar_price = self.customer_chicken_ceasar_quantity_total * 12.99
                    if self.check_chicken_ceasar_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_chicken_ceasar_in_list)
                        self.customer_cart_list.append(f'{self.customer_chicken_ceasar_quantity_total} Chicken Ceasar Salads at $12.99 is ${self.customer_total_chicken_ceasar_price:.2f}')
                        self.customer_order_amount +=  int(self.chicken_ceasar_amount_entry_box.get()) * 12.99
                        self.check_chicken_ceasar_in_list = f'{self.customer_chicken_ceasar_quantity_total} Chicken Ceasar Salads at $12.99 is ${self.customer_total_chicken_ceasar_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_chicken_ceasar_quantity_total} Chicken Ceasar Salads at $12.99 is ${self.customer_total_chicken_ceasar_price:.2f}')
                        self.check_chicken_ceasar_in_list = f'{self.customer_chicken_ceasar_quantity_total} Chicken Ceasar Salads at $12.99 is ${self.customer_total_chicken_ceasar_price:.2f}'
                        self.customer_order_amount += int(self.chicken_ceasar_amount_entry_box.get()) * 12.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.salad_pack_forget()
                    self.make_main()
            elif salad_choice_order_save == 1:
                if int(self.greek_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_greek_quantity_total += int(self.greek_amount_entry_box.get())
                    self.customer_total_greek_price =  self.customer_greek_quantity_total * 9.99
                    if self.check_greek_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_greek_in_list)
                        self.customer_cart_list.append(f'{self.customer_greek_quantity_total} Greek Salads at $9.99 is ${self.customer_total_greek_price:.2f}')
                        self.customer_order_amount += int(self.greek_amount_entry_box.get()) * 9.99
                        self.check_greek_in_list = f'{self.customer_greek_quantity_total} Greek Salads at $9.99 is ${self.customer_total_greek_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_greek_quantity_total} Greek Salads at $9.99 is ${self.customer_total_greek_price:.2f}')
                        self.check_greek_in_list = f'{self.customer_greek_quantity_total} Greek Salads at $9.99 is ${self.customer_total_greek_price:.2f}'
                        self.customer_order_amount += int(self.greek_amount_entry_box.get()) * 9.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.salad_pack_forget()
                    self.make_main()
            elif salad_choice_order_save == 2:
                if int(self.asian_sesame_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_asian_sesame_quantity_total += int(self.asian_sesame_amount_entry_box.get())
                    self.customer_total_asian_sesame_price = self.customer_asian_sesame_quantity_total * 9.99
                    if self.check_asian_sesame_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_asian_sesame_in_list)
                        self.customer_cart_list.append(f'{self.customer_asian_sesame_quantity_total} Asian Sesames at $9.99 is ${self.customer_total_asian_sesame_price:.2f}')
                        self.customer_order_amount += int(self.asian_sesame_amount_entry_box.get()) * 9.99
                        self.check_asian_sesame_in_list = f'{self.customer_asian_sesame_quantity_total} Asian Sesames at $9.99 is ${self.customer_total_asian_sesame_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_asian_sesame_quantity_total} Asian Sesames at $9.99 is ${self.customer_total_asian_sesame_price:.2f}')
                        self.check_asian_sesame_in_list = f'{self.customer_asian_sesame_quantity_total} Asian Sesames at $9.99 is ${self.customer_total_asian_sesame_price:.2f}'
                        self.customer_order_amount += int(self.asian_sesame_amount_entry_box.get()) * 9.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.salad_pack_forget()
                    self.make_main()     
        except:
            messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
    
    def dessert_menu(self) -> None:
        '''
        Method to create the frames, labels, radio buttons, back to menu button, and add to cart button
        for the dessert choices the customer may chose from.
        '''
        self.root.configure(bg='orange')
        self.dessert_header_frame = Frame(self.root)
        self.dessert_header_label = Label(self.dessert_header_frame, text='Dessert Menu', font=('Helvetica bold', 35))
        self.dessert_header_frame.pack(pady=5)
        self.dessert_header_label.pack()
        self.dessert_choose_frame = Frame(self.root)
        self.dessert_choose_label = Label(self.dessert_choose_frame, text='Please Choose a Dessert', font=('Helvetica bold', 15))
        self.dessert_choose_frame.pack(pady=10)
        self.dessert_choose_label.pack()
        self.radio_7 = IntVar()
        self.cookie_frame = Frame(self.root, height=45, width=230)
        self.cookie_button = Radiobutton(self.cookie_frame, text='Cookie: $1.99', font=('Helvetica bold', 15), variable=self.radio_7, value=0, command=self.getdessertbutton)
        self.cookie_label = Label(self.cookie_frame, text='How Many:', font=('Helvetica bold', 15))
        self.cookie_amount_entry_box = Entry(self.cookie_frame, width=2, font=('Helvetica bold', 15))
        self.cookie_frame.pack(anchor='w', padx=30, pady=10)
        self.cookie_frame.pack_propagate(0)
        self.cookie_button.pack(padx=5, side='left')
        self.brownie_frame = Frame(self.root, height=45, width=230)
        self.brownie_button = Radiobutton(self.brownie_frame, text='Brownie: $2.99', font=('Helvetica bold', 15), variable=self.radio_7, value=1, command=self.getdessertbutton)
        self.brownie_label = Label(self.brownie_frame, text='How Many:', font=('Helvetica bold', 15))
        self.brownie_amount_entry_box = Entry(self.brownie_frame, width=2, font=('Helvetica bold', 15))
        self.brownie_frame.pack(anchor='w', padx=30, pady=10)
        self.brownie_frame.pack_propagate(0)
        self.brownie_button.pack(padx=5, side='left')
        self.ice_cream_frame = Frame(self.root, height=45, width=230)
        self.ice_cream_button = Radiobutton(self.ice_cream_frame, text='Ice Cream: $3.99', font=('Helvetica bold', 15), variable=self.radio_7, value=2, command=self.getdessertbutton)
        self.ice_cream_label = Label(self.ice_cream_frame, text='How Many:', font=('Helvetica bold', 15))
        self.ice_cream_amount_entry_box = Entry(self.ice_cream_frame, width=2, font=('Helvetica bold', 15))
        self.ice_cream_frame.pack(anchor='w', padx=30, pady=10)
        self.ice_cream_frame.pack_propagate(0)
        self.ice_cream_button.pack(padx=5, side='left')
        self.radio_7.set(None)
        
        self.dessert_button_frame = Frame(self.root, bg='orange')
        self.dessert_back_button = Button(self.dessert_button_frame, text='BACK TO MENU', font=('Helvetica bold', 15), command=self.dessertbackclicked)
        self.dessert_next_button = Button(self.dessert_button_frame, text='ADD TO CART', font=('Helvetica bold', 15), command=self.dessertnextclicked)
        self.dessert_button_frame.pack(pady=30)
        self.dessert_back_button.pack(padx= 30, side='left') 
        self.dessert_next_button.pack(padx= 30, side='right')
        
    def getdessertbutton(self) -> None:
        '''
        Method to create an amount entry box for the particular dessert the customer would like.
        '''
        self.cookie_frame.config(height=45, width=230)
        self.cookie_amount_entry_box.pack_forget()
        self.cookie_label.pack_forget()
        self.brownie_frame.config(height=45, width=230)
        self.brownie_amount_entry_box.pack_forget()
        self.brownie_label.pack_forget()
        self.ice_cream_frame.config(height=45, width=230)
        self.ice_cream_amount_entry_box.pack_forget()
        self.ice_cream_label.pack_forget()
        
        dessert_choice_save = self.radio_7.get()
        try:
            if dessert_choice_save == 0:
                self.cookie_frame.config(height=45, width=380)
                self.cookie_amount_entry_box.pack(padx=5, side='right')    
                self.cookie_label.pack(padx=5, side='right')
                self.cookie_amount_entry_box.focus_set()
                self.cookie_amount_entry_box.delete(0, END)
            elif dessert_choice_save == 1:
                self.brownie_frame.config(height=45, width=380)
                self.brownie_amount_entry_box.pack(padx=5, side='right')    
                self.brownie_label.pack(padx=5, side='right')
                self.brownie_amount_entry_box.focus_set()
                self.brownie_amount_entry_box.delete(0, END)
            elif dessert_choice_save == 2:
                self.ice_cream_frame.config(height=45, width=380)
                self.ice_cream_amount_entry_box.pack(padx=5, side='right')    
                self.ice_cream_label.pack(padx=5, side='right')
                self.ice_cream_amount_entry_box.focus_set()
                self.ice_cream_amount_entry_box.delete(0, END)
        except:
            messagebox.showinfo('NO SELECTION', 'You Did Not Make a Selection!')
    
    def dessert_pack_forget(self) -> None:
        '''
        Method to delete the frames from the dessert menu screen.
        '''
        self.dessert_header_frame.pack_forget()
        self.dessert_choose_frame.pack_forget()
        self.cookie_frame.pack_forget()
        self.brownie_frame.pack_forget()
        self.ice_cream_frame.pack_forget()
        self.dessert_button_frame.pack_forget()        

    def dessertbackclicked(self) -> None:
        '''
        Method to delete the frames from the dessert menu screen and create the main menu screen if the customer
        does not want to get a dessert and return to the main menu.
        '''
        self.dessert_pack_forget()
        self.make_main()
        
    def dessertnextclicked(self) -> None:
        '''
        Method to add the dessert and amount the customer chooses to the cart then have a message box pop up saying the selection
        has been added to the cart. Once that happens the dessert menu screen will be deleted and the main menu screen
        will be created.
        '''
        try:
            dessert_choice_order_save = self.radio_7.get()
            if dessert_choice_order_save == 0:
                if int(self.cookie_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_cookie_quantity_total += int(self.cookie_amount_entry_box.get())
                    self.customer_total_cookie_price = self.customer_cookie_quantity_total * 1.99
                    if self.check_cookie_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_cookie_in_list)
                        self.customer_cart_list.append(f'{self.customer_cookie_quantity_total} Cookies at $1.99 is ${self.customer_total_cookie_price:.2f}')
                        self.customer_order_amount +=  int(self.cookie_amount_entry_box.get()) * 1.99
                        self.check_cookie_in_list = f'{self.customer_cookie_quantity_total} Cookies at $1.99 is ${self.customer_total_cookie_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_cookie_quantity_total} Cookies at $1.99 is ${self.customer_total_cookie_price:.2f}')
                        self.check_cookie_in_list = f'{self.customer_cookie_quantity_total} Cookies at $1.99 is ${self.customer_total_cookie_price:.2f}'
                        self.customer_order_amount += int(self.cookie_amount_entry_box.get()) * 1.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.dessert_pack_forget()
                    self.make_main()
            elif dessert_choice_order_save == 1:
                if int(self.brownie_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_brownie_quantity_total += int(self.brownie_amount_entry_box.get())
                    self.customer_total_brownie_price =  self.customer_brownie_quantity_total * 2.99
                    if self.check_brownie_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_brownie_in_list)
                        self.customer_cart_list.append(f'{self.customer_brownie_quantity_total} Brownies at $2.99 is ${self.customer_total_brownie_price:.2f}')
                        self.customer_order_amount += int(self.brownie_amount_entry_box.get()) * 2.99
                        self.check_brownie_in_list = f'{self.customer_brownie_quantity_total} Brownies at $2.99 is ${self.customer_total_brownie_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_brownie_quantity_total} Brownies at $2.99 is ${self.customer_total_brownie_price:.2f}')
                        self.check_brownie_in_list = f'{self.customer_brownie_quantity_total} Brownies at $2.99 is ${self.customer_total_brownie_price:.2f}'
                        self.customer_order_amount += int(self.brownie_amount_entry_box.get()) * 2.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.dessert_pack_forget()
                    self.make_main()
            elif dessert_choice_order_save == 2:
                if int(self.ice_cream_amount_entry_box.get()) < 1:
                    messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                else:
                    self.customer_ice_cream_quantity_total += int(self.ice_cream_amount_entry_box.get())
                    self.customer_total_ice_cream_price = self.customer_ice_cream_quantity_total * 3.99
                    if self.check_ice_cream_in_list in self.customer_cart_list:
                        self.customer_cart_list.remove(self.check_ice_cream_in_list)
                        self.customer_cart_list.append(f'{self.customer_ice_cream_quantity_total} Ice Creams at $3.99 is ${self.customer_total_ice_cream_price:.2f}')
                        self.customer_order_amount += int(self.ice_cream_amount_entry_box.get()) * 3.99
                        self.check_ice_cream_in_list = f'{self.customer_ice_cream_quantity_total} Ice Creams at $3.99 is ${self.customer_total_ice_cream_price:.2f}'
                    else:
                        self.customer_cart_list.append(f'{self.customer_ice_cream_quantity_total} Ice Creams at $3.99 is ${self.customer_total_ice_cream_price:.2f}')
                        self.check_ice_cream_in_list = f'{self.customer_ice_cream_quantity_total} Ice Creams at $3.99 is ${self.customer_total_ice_cream_price:.2f}'
                        self.customer_order_amount += int(self.ice_cream_amount_entry_box.get()) * 3.99
                    messagebox.showinfo('ADDED TO CART', 'Your Selection Has Been Added to Cart')
                    self.dessert_pack_forget()
                    self.make_main()
        except:
            messagebox.showinfo('NOT VALID', 'Please Enter A Positive Number')
                    
    def cart_menu(self) -> None:
        '''
        Method to create the frames, labels, menu button, text that show what the customer has ordered, and pay button
        for the cart menu.
        '''
        self.root.configure(bg='green')
        self.cart_header_frame = Frame(self.root, height=60, width=750, bg='green')
        self.cart_header_label = Label(self.cart_header_frame, text='Your Cart', font=('Helvetica bold', 35), bg='green')
        self.cart_header_frame.pack(pady=5)
        self.cart_header_frame.pack_propagate(0)
        self.cart_menu_button = Button(self.cart_header_frame, text='MENU', font=('Helvetica bold', 15), command=self.cart_pack_forget)
        self.cart_menu_button.pack(padx=5, pady=5, side='right')
        self.cart_header_label.pack(side='right', padx= 185, pady= 5)
        self.cart_want_frame = Frame(self.root)
        self.cart_want_label = Label(self.cart_want_frame, text='Food and Drinks You Want to Order', font=('Helvetica bold', 14))
        self.cart_want_frame.pack(pady=5)
        self.cart_want_label.pack()

        self.cart_text_output = Text(self.root, height=20, width=40, font=('Helvetica bold', 15))
        self.cart_text_output.pack(pady=5)

        for item in self.customer_cart_list:
            self.cart_text_output.insert(END, item + "\n")

        self.order_tax_amount = .055 * self.customer_order_amount
        self.customer_order_total_amount = self.order_tax_amount + self.customer_order_amount
        
        self.order_before_tax_total_frame = Frame(self.root)
        self.order_before_tax_total_label = Label(self.order_before_tax_total_frame, text=f'Total Before Tax: ${self.customer_order_amount:.2f}', font=('Helvetica bold', 14))
        self.order_before_tax_total_frame.pack()
        self.order_before_tax_total_label.pack()
        self.order_tax_frame = Frame(self.root)
        self.order_tax_label = Label(self.order_tax_frame, text=f'Order Tax Amount: ${self.order_tax_amount:.2f}', font=('Helvetica bold', 14))
        self.order_tax_frame.pack(pady=5)
        self.order_tax_label.pack()
        self.order_total_price_frame = Frame(self.root)
        self.order_total_price_label = Label(self.order_total_price_frame, text=f'Your Order Total: ${self.customer_order_total_amount:.2f}', font=('Helvetica bold', 14))
        self.order_total_price_frame.pack(pady=5)
        self.order_total_price_label.pack()
    
        self.cart_pay_button_frame = Frame(self.root, bg='green')
        self.cart_pay_button = Button(self.cart_pay_button_frame, text='PAY', font=('Helvetica bold', 15), command=self.cart_pay_pack)
        self.cart_pay_button_frame.pack(pady=10)
        self.cart_pay_button.pack()
            
    def cart_pack_forget(self) -> None:
        '''
        Method to delete the frames from the cart menu screen and make the main menu screen.
        '''
        self.cart_header_frame.pack_forget()
        self.cart_want_frame.pack_forget()
        self.cart_text_output.pack_forget()
        self.order_total_price_frame.pack_forget()
        self.order_before_tax_total_frame.pack_forget()
        self.order_tax_frame.pack_forget()
        self.order_total_price_frame.pack_forget()
        self.cart_pay_button_frame.pack_forget()
        self.make_main()
        
    def cart_pay_pack(self) -> None:
        '''
        Method to delete the frames from the cart menu screen and make the order paid screen.
        '''
        self.cart_header_frame.pack_forget()
        self.cart_want_frame.pack_forget()
        self.cart_text_output.pack_forget()
        self.order_total_price_frame.pack_forget()
        self.order_before_tax_total_frame.pack_forget()
        self.order_tax_frame.pack_forget()
        self.order_total_price_frame.pack_forget()
        self.cart_pay_button_frame.pack_forget()
        self.order_paid()
        
    def order_paid(self) -> None:
        '''
        Method to create the frame and label for the order paid screen.
        '''
        self.root.configure(bg='yellow')
        self.header_order_paid_frame = Frame(self.root)
        self.header_order_paid_label = Label(self.header_order_paid_frame, text='THANK YOU COME AGAIN', font=('Helvetica bold', 40))
        self.header_order_paid_frame.pack(pady=50)
        self.header_order_paid_label.pack()
        
        self.root.mainloop()

def main() -> None:
    customer_order_1 = CUSTOMER_ORDER()
    making_customer_order_1 = customer_order_1.make_main()

if __name__ == '__main__':
    main()