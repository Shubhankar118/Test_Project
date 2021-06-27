import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class spartanGrid(GridLayout): #created gridlayout main class
    def __init__(self,**kwargs):  
        super(spartanGrid, self).__init__()
        self.cols = 3 


        self.add_widget(Label(text="student Name:"))

        self.s_name = TextInput()
        self.add_widget(self.s_name)
        self.add_widget(Label(text="Student Marks:"))
        self.s_marks= TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender"))
        self.s_gender=TextInput()
        self.add_widget(self.s_gender)
        self.press = Button(text="submit")
        self.press.bind(on_presss=self.click_me)
        self.add_widget(self.press)


    def click_me(self,instance):
        print("name of student is"+self.name.text)
        print("markx of student are" +self.s_marks.text)
        print("gender of student is "+ self.s_gender.text)




class SpartenApp(App):#child class
    def build(self):
        return spartanGrid()


if __name__ == '__main__':
    SpartenApp().run()
