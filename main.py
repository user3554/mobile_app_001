from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MainApp(App):

    def najatie(self, btext):
        if btext.text == "C":
            self.tekst.text = ""
        elif btext.text == "=":
            self.tekst.text = str(eval(self.tekst.text))
        else:
            self.tekst.text = self.tekst.text + btext.text

    def build(self):
        okno = BoxLayout(orientation="vertical")

        self.tekst = TextInput(multiline=False,
                               readonly=False,
                               halign="center",
                               font_size=25)
        okno.add_widget(self.tekst)
        buttons = [
            ["1", "2", "3", "+"],
            ["4", "5", "6", "-"],
            ["7", "8", "9", "*"],
            ["0", ".", "C", "/"],
            ["**", "**0.5", "(", ")"],
            ["="],
        ]
        for i in buttons:
            ramka = BoxLayout()
            for j in i:
                button = Button(text=j, font_size=25)
                button.bind(on_press=self.najatie)
                ramka.add_widget(button)
            okno.add_widget(ramka)

        return okno


if __name__ == '__main__':
    MainApp().run()
