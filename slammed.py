from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kings import kings_game
from trivia import drunk_trivia_game
from most_likely import most_likely_game
from roulette import roulette_game
from would_you_rather import would_you_rather_game

class BackgroundScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.bg = Image(source='toxic.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg)
        self.content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(self.content)
        self.add_widget(layout)

class HomeScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        welcome_label = Label(text="[b]Welcome to Slammed, the last game you'll ever want to play[/b]", font_size='24sp', halign='center', valign='middle', color=(1, 0, 0, 1), markup=True)
        enter_button = Button(text='Enter', font_size='20sp', size_hint=(1, 0.1), on_press=self.enter)
        self.content.add_widget(welcome_label)
        self.content.add_widget(enter_button)

    def enter(self, instance):
        self.manager.current = 'game_selection'

class GameSelectionScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spinner = Spinner(
            text='Menu',
            values=('Cast Instructions', 'Kings', 'Drunk Trivia', 'Most Likely To', 'Roulette', 'Would You Rather'),
            size_hint=(None, None),
            size=(200, 44)
        )
        self.spinner.bind(text=self.show_screen)
        self.content.add_widget(self.spinner)

    def show_screen(self, spinner, text):
        if text == 'Cast Instructions':
            self.manager.current = 'cast_instructions'
        elif text == 'Kings':
            self.manager.current = 'game'
        elif text == 'Roulette':
            self.manager.current = 'roulette'
        elif text == 'Drunk Trivia':
            self.manager.current = 'drunk_trivia'
        elif text == 'Most Likely To':
            self.manager.current = 'most_likely'
        elif text == 'Would You Rather':
            self.manager.current = 'would_you_rather'
        self.spinner.text = 'Menu'  # Reset the spinner text after selection

class GameScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='[b]Game Screen[/b]', font_size='24sp', text_size=(self.width, None), size_hint=(1, 0.6), halign='center', valign='middle', color=(1, 0, 0, 1), markup=True)
        self.label.bind(size=self._update_text_width)
        self.draw_card_button = Button(text='Draw Card', font_size='20sp', size_hint=(1, 0.2), on_press=self.draw_card)
        back_button = Button(text='Back', font_size='20sp', size_hint=(1, 0.2), on_press=self.go_back)
        self.content.add_widget(self.label)
        self.content.add_widget(self.draw_card_button)
        self.content.add_widget(back_button)

    def _update_text_width(self, *_):
        self.label.text_size = (self.label.width * 0.9, None)

    def draw_card(self, instance):
        card, rule, instruction = kings_game.draw_card()
        if card:
            self.label.text = f"[b]Card:[/b] {card}\n[b]Rule:[/b] {rule}\n[b]Instruction:[/b] {instruction}"
        else:
            self.label.text = '[b]No more cards![/b]'

    def go_back(self, instance):
        self.manager.current = 'game_selection'

class RouletteGameScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='[b]Draw a Card![/b]', font_size='24sp', size_hint=(1, 0.6), color=(1, 0, 0, 1), markup=True)
        self.card_label = Label(text='', font_size='20sp', text_size=(self.width, None), size_hint=(1, 0.6), halign='center', valign='middle', color=(1, 0, 0, 1), markup=True)
        self.card_label.bind(size=self._update_text_width)
        self.draw_card_button = Button(text='Draw Card', font_size='20sp', size_hint=(1, 0.2), on_press=self.draw_card)
        back_button = Button(text='Back', font_size='20sp', size_hint=(1, 0.2), on_press=self.go_back)
        self.content.add_widget(self.label)
        self.content.add_widget(self.card_label)
        self.content.add_widget(self.draw_card_button)
        self.content.add_widget(back_button)

    def _update_text_width(self, *_):
        self.card_label.text_size = (self.card_label.width * 0.9, None)

    def draw_card(self, instance):
        card = roulette_game.draw_card()
        if card:
            self.card_label.text = f"[b]Challenge:[/b] {card}"
        else:
            self.card_label.text = '[b]No more cards![/b]'

    def go_back(self, instance):
        self.manager.current = 'game_selection'

class DrunkTriviaGameScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='[b]Drunk Trivia[/b]', font_size='24sp', size_hint=(1, 0.6), color=(1, 0, 0, 1), markup=True)
        self.question_label = Label(text='', font_size='20sp', text_size=(self.width, None), size_hint=(1, 0.4), halign='center', valign='middle', color=(1, 0, 0, 1), markup=True)
        self.answer_label = Label(text='', font_size='20sp', text_size=(self.width, None), size_hint=(1, 0.4), halign='center', valign='middle', color=(1, 0, 0, 1), markup=True)
        self.question_label.bind(size=self._update_text_width)
        self.answer_label.bind(size=self._update_text_width)
        self.next_question_button = Button(text='Next Question', font_size='20sp', size_hint=(1, 0.1), on_press=self.next_question)
        self.show_answer_button = Button(text='Answer', font_size='20sp', size_hint=(1, 0.1), on_press=self.show_answer)
        back_button = Button(text='Back', font_size='20sp', size_hint=(1, 0.1), on_press=self.go_back)
        self.content.add_widget(self.label)
        self.content.add_widget(self.question_label)
        self.content.add_widget(self.answer_label)
        self.content.add_widget(self.next_question_button)
        self.content.add_widget(self.show_answer_button)
        self.content.add_widget(back_button)
        self.current_answer = None

    def _update_text_width(self, *_):
        self.question_label.text_size = (self.question_label.width * 0.9, None)
        self.answer_label.text_size = (self.answer_label.width * 0.9, None)

    def next_question(self, instance):
        question, self.current_answer = drunk_trivia_game.get_question()
        self.question_label.text = f"[b]Question:[/b] {question}"
        self.answer_label.text = ''

    def show_answer(self, instance):
        if self.current_answer:
            self.answer_label.text = f"[b]Answer:[/b] {self.current_answer}"

    def go_back(self, instance):
        self.manager.current = 'game_selection'

class MostLikelyGameScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='[b]Most Likely To[/b]', font_size='24sp', size_hint=(1, 0.6), color=(1, 0, 0, 1), markup=True)
        self.prompt_label = Label(text='', font_size='20sp', text_size=(self.width, None), size_hint=(1, 0.6), halign='center', valign='middle', color=(1, 0, 0, 1), markup=True)
        self.prompt_label.bind(size=self._update_text_width)
        self.next_prompt_button = Button(text='Next Prompt', font_size='20sp', size_hint=(1, 0.2), on_press=self.next_prompt)
        back_button = Button(text='Back', font_size='20sp', size_hint=(1, 0.2), on_press=self.go_back)
        self.content.add_widget(self.label)
        self.content.add_widget(self.prompt_label)
        self.content.add_widget(self.next_prompt_button)
        self.content.add_widget(back_button)

    def _update_text_width(self, *_):
        self.prompt_label.text_size = (self.prompt_label.width * 0.9, None)

    def next_prompt(self, instance):
        prompt = most_likely_game.get_prompt()
        self.prompt_label.text = prompt

    def go_back(self, instance):
        self.manager.current = 'game_selection'

class WouldYouRatherGameScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='[b]Would You Rather[/b]', font_size='24sp', size_hint=(1, 0.6), color=(1, 0, 0, 1), markup=True)
        self.prompt_label = Label(text='', font_size='20sp', text_size=(self.width, None), size_hint=(1, 0.6), halign='center', valign='middle', color=(1, 0, 0, 1), markup=True)
        self.prompt_label.bind(size=self._update_text_width)
        self.next_prompt_button = Button(text='Next Prompt', font_size='20sp', size_hint=(1, 0.2), on_press=self.next_prompt)
        back_button = Button(text='Back', font_size='20sp', size_hint=(1, 0.2), on_press=self.go_back)
        self.content.add_widget(self.label)
        self.content.add_widget(self.prompt_label)
        self.content.add_widget(self.next_prompt_button)
        self.content.add_widget(back_button)

    def _update_text_width(self, *_):
        self.prompt_label.text_size = (self.prompt_label.width * 0.9, None)

    def next_prompt(self, instance):
        prompt = would_you_rather_game.get_prompt()
        self.prompt_label.text = prompt

    def go_back(self, instance):
        self.manager.current = 'game_selection'

class CastInstructionsScreen(BackgroundScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instructions = """
        To cast your screen:

        Android:
        1. Open the Google Home app and select the device you want to cast your screen to.
        2. Tap the "Cast my screen" button.

        Or:
        1. Swipe down from the top of your screen to open the Quick Settings panel.
        2. Look for the "Cast" or "Screen Cast" icon and tap it.
        3. Select the device you want to cast to.

        iOS:
        1. Swipe down from the upper-right corner of the screen to open the Control Center.
        2. Tap the "Screen Mirroring" button.
        3. Select the device you want to cast your screen to from the list.
        """
        self.instructions_label = Label(text=instructions, font_size='16sp', halign='left', valign='top', text_size=(self.width * 0.9, None), size_hint=(1, 0.8), color=(1, 0, 0, 1), markup=True)
        self.instructions_label.bind(size=self._update_text_width)
        back_button = Button(text='Back', font_size='20sp', size_hint=(1, 0.2), on_press=self.go_back)
        self.content.add_widget(self.instructions_label)
        self.content.add_widget(back_button)

    def _update_text_width(self, *_):
        self.instructions_label.text_size = (self.instructions_label.width * 0.9, None)

    def go_back(self, instance):
        self.manager.current = 'game_selection'

class SlammedApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(GameSelectionScreen(name='game_selection'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(CastInstructionsScreen(name='cast_instructions'))
        sm.add_widget(RouletteGameScreen(name='roulette'))
        sm.add_widget(DrunkTriviaGameScreen(name='drunk_trivia'))
        sm.add_widget(MostLikelyGameScreen(name='most_likely'))
        sm.add_widget(WouldYouRatherGameScreen(name='would_you_rather'))
        return sm

if __name__ == '__main__':
    SlammedApp().run()
