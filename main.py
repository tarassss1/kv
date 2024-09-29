from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class ScrButton(Button):
  def __init__(self, screen, direction='right', goal='main', **kwargs):
      super().__init__(**kwargs)
      self.screen = screen
      self.direction = direction
      self.goal = goal
  def on_press(self):
      self.screen.manager.transition.direction = self.direction
      self.screen.manager.current = self.goal
    
class MainScr(Screen):
  def __init__(self, **kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
      hl = BoxLayout()
      txt = Label(text= 'Вибери екран')
      vl.add_widget(ScrButton(self, direction='down', goal='first', text="1"))
      vl.add_widget(ScrButton(self, direction='left', goal='second', text="2"))
      hl.add_widget(txt)
      hl.add_widget(vl)
      self.add_widget(hl)

class FirstScr(Screen):
  def __init__(self, **kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation='vertical')
      btn = Button(text= 'Вибір: 1')
      btn_back = ScrButton(self, direction='up', goal='main', text="Назад")
      vl.add_widget(btn)	
      vl.add_widget(btn_back)
      self.add_widget(vl)

class SecondScr(Screen):
  def __init__(self, **kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation='vertical')
      self.txt = Label(text= 'Вибір: 2')
      vl.add_widget(self.txt)
      hl = BoxLayout()
      btn_back = ScrButton(self, direction='right', goal='main', text="Назад")
      hl.add_widget(btn_back)
      vl.add_widget(hl)
      self.add_widget(vl)
   

   

class MyApp(App):
  def build(self):
      sm = ScreenManager()
      sm.add_widget(MainScr(name='main'))
      sm.add_widget(FirstScr(name='first'))
      sm.add_widget(SecondScr(name='second'))

      return sm
MyApp().run()

# 1. Створити клас для нового вікна
# 2. Додати кнопку на головне вікно
# 3. Додати об'єкт до ScreenManagar
