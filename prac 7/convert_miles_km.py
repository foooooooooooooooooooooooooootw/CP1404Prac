from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty
from kivy.core.window import Window

MILE_TO_KM = 1.60934


class mtkm(App):
    message = StringProperty()

    # create and start the App running

    def build(self):
        Window.size = (400, 200)
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_press(self):
        self.message = self.root.ids.input_number.text

    def handle_calc(self, value):
        if value.replace(".", "") == "" or value.replace(".", "").isspace() or value.replace(".",
                                                                                             "").isnumeric() == False:
            self.root.ids.output_label.text = str("0.0")
        else:
            result = round((float(value) * MILE_TO_KM), 3)
            self.root.ids.output_label.text = str(result)

    def handle_increase(self, value):
        if value.replace(".", "") == "" or value.replace(".", "").isspace() or value.replace(".",
                                                                                             "").isnumeric() == False:
            self.root.ids.input_number.text = str("0.0")
            temp = float(self.root.ids.input_number.text)
            temp += 1
            self.root.ids.input_number.text = str(temp)

        else:
            temp = float(self.root.ids.input_number.text)
            temp += 1
            self.root.ids.input_number.text = str(temp)

    def handle_decrease(self, value):
        if value.replace(".", "") == "" or value.replace(".", "").isspace() or value.replace(".",
                                                                                             "").isnumeric() == False:
            self.root.ids.input_number.text = str("0.0")
            temp = float(self.root.ids.input_number.text)
            temp -= 1
            self.root.ids.input_number.text = str(temp)

        else:
            temp = float(self.root.ids.input_number.text)
            temp -= 1
            self.root.ids.input_number.text = str(temp)


mtkm().run()
