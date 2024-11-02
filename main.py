import random  # Import the random module
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from alpha_beta import AlphaBeta
from kivy.lang import Builder

Builder.load_file("TicTacToeApp.kv")

class TicTacToeApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_popup = None  # Track the current popup

    def build(self):
        self.game_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.alpha_beta_algo = AlphaBeta(self.game_state)
        self.layout = TicTacToeGrid(self)

        # Randomly choose who goes first
        self.user_turn = random.choice([True, False])  # True for user, False for AI
        if not self.user_turn:
            self.ai_move()  # AI makes the first move if it goes first

        return self.layout

    def reset_game(self):
        # Reset the game state and UI
        self.game_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.alpha_beta_algo = AlphaBeta(self.game_state)
        self.layout.update_buttons()
        self.user_turn = random.choice([True, False])  # Randomly choose who goes first again
        if not self.user_turn:
            self.ai_move()  # AI makes the first move if it goes first

    def show_popup(self, message):
        # Close the existing popup if it's open
        if self.current_popup:
            self.current_popup.dismiss()

        popup_content = GridLayout(cols=1, padding=10, spacing=10)
        popup_content.add_widget(Label(text=message))

        # Restart Button
        restart_button = Button(text='Restart', size_hint=(1, 0.2))
        restart_button.bind(on_release=lambda instance: self.restart_game())
        popup_content.add_widget(restart_button)

        # Close Button
        close_button = Button(text='Close', size_hint=(1, 0.2))
        close_button.bind(on_release=self.stop)  # Close the app
        popup_content.add_widget(close_button)

        # Create and open the popup
        self.current_popup = Popup(title='Game Over', content=popup_content, size_hint=(0.6, 0.4))
        self.current_popup.open()

    def restart_game(self):
        # Close the popup and reset the game state
        if self.current_popup:
            self.current_popup.dismiss()
        self.reset_game()  # Call reset_game to restart the game

    def ai_move(self):
        ai_move = self.alpha_beta_algo.best_move(self.game_state)
        if ai_move:  # Ensure the AI has a valid move
            self.game_state[ai_move[0]][ai_move[1]] = 'X'
            self.layout.update_buttons()
            self.user_turn = True
            self.check_game_status()

    def check_game_status(self):
        # Check for win condition
        if self.alpha_beta_algo.is_terminal(self.game_state):
            if self.alpha_beta_algo.utility(self.game_state) == 1:
                self.show_popup("AI wins!")
            elif self.alpha_beta_algo.utility(self.game_state) == -1:
                self.show_popup("You win!")
            else:
                self.show_popup("It's a tie!")


class TicTacToeGrid(GridLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.cols = 3
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                btn = Button(text='', font_size=32)
                btn.bind(on_release=self.on_button_click)
                btn.row, btn.col = row, col
                self.add_widget(btn)
                button_row.append(btn)
            self.buttons.append(button_row)

    def on_button_click(self, instance):
        row, col = instance.row, instance.col
        # Check if the current tile is empty and it's the user's turn
        if self.app.game_state[row][col] == ' ' and self.app.user_turn:
            self.app.game_state[row][col] = 'O'  # User places 'O'
            instance.text = 'O'  # Update button text
            self.app.user_turn = False  # Switch turn to AI

            # Check for win condition for the player
            if self.app.alpha_beta_algo.is_terminal(self.app.game_state):
                if self.app.alpha_beta_algo.utility(self.app.game_state) == -1:
                    self.app.show_popup("You win!")
                elif self.app.alpha_beta_algo.utility(self.app.game_state) == 1:
                    self.app.show_popup("AI wins!")
                else:
                    self.app.show_popup("It's a tie!")
                return

            # AI's move
            self.app.ai_move()  # Call AI move function

            # Check if game is still ongoing after AI's move
            if not self.app.alpha_beta_algo.is_terminal(self.app.game_state):
                self.update_buttons()  # Only update buttons if the game is ongoing

            # Check for win condition for the AI
            self.app.check_game_status()  # Check game status after AI move


    def update_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].text = self.app.game_state[row][col]

if __name__ == '__main__':
    TicTacToeApp().run()
