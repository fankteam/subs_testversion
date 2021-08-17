from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from random import random


from func import getting, get_week_number
from func import check_dz, add_dz, edit_dz, delete_dz, next_dz, get_dz_by_id

from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.config import Config

# Config.set('graphics', 'resizable', True)
# Config.write()
# Window.fullscreen = False

Window.clearcolor = (.84, .84, .84, 1)
# Window.borderless = '1'
nede_text = 1
# Config.set('graphics', 'resizable', True)
# Config.set('graphics', 'width', '100')
# Config.set('graphics', 'height', '500')
Window.size = (350, 650)

# popup = Popup()
def create_popup(self, instance):
    global t, ned, date, num, sub, idd
    global popup
    global textinput_dz

    poplayout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    # print(self.text)
    t = self.text

    # day_id2 = t[5:].find('-')
    # day_id1 = t[day_id2+5+1:].find('-')
    # day_id0 = t[day_id2+6:day_id1+day_id2+6]

    # a = '[ref=&week&7&/week&id&1&/id&date&06.09.21&/date&num&4&/num&sub&matesha&/sub]'
    ned = t[t.rfind('&week')+6:(t.find('&/week'))]
    idd = t[t.rfind('&id')+4:(t.find('&/id'))]
    date = t[t.rfind('&date')+6:(t.find('&/date'))]
    num = t[t.rfind('&num')+5:(t.find('&/num'))]
    sub = t[t.rfind('&sub')+5:(t.find('&/sub'))]
    # print(ned, idd, date, num, sub)

    dz = get_dz_by_id(idd)
    if dz:
        textdz = dz
    else:
        textdz = ''

    popup = Popup(title='Редактирование дз. '+date+'. '+num+'.'+sub, content=poplayout, size_hint=(.90, .50), 
        separator_color=[1, 1, 1, 1], separator_height=1, title_align='center', title_color=[.1, .1, .1, 1], background_color=[1, 1, 1, 1], background='')

    # popup.add_widget(poplayout)
    textinput_dz = TextInput(text=textdz, cursor_color=[0, 0, 0, 1], font_size=16, readonly=False)
    poplayout.add_widget(textinput_dz)
    poplayout.add_widget(Button(text='Сохранить', background_color=[.55, .55, .55, 1], background_normal='', size_hint=(1, .25), on_press=popup_save_dz))
    popup.open()

def popup_save_dz(instance):

    chdz = check_dz(idd)
    # print(chdz)
    if chdz:
        edit_dz(int(idd), textinput_dz.text)
    else:
        add_dz(int(idd), textinput_dz.text)

    popup.dismiss()
    global nede_text
    nede_text = int(ned)

    random_text = str(random())

    sm.add_widget(SecondScreen(name='second-'+str(nede_text)+random_text))
    sm.current = 'second-'+str(nede_text)+random_text


def dz_info_popup(self, instance):

    t = self.text

    ned = t[t.rfind('&week')+6:(t.find('&/week'))]
    idd = t[t.rfind('&id')+4:(t.find('&/id'))]
    date = t[t.rfind('&date')+6:(t.find('&/date'))]
    num = t[t.rfind('&num')+5:(t.find('&/num'))]
    sub = t[t.rfind('&sub')+5:(t.find('&/sub'))]
    dz = t[t.rfind('&dz')+4:(t.find('&/dz'))]

    dz_poplayout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    dz_popup = Popup(title='Домашнее задание на '+date+'. '+num+'.'+sub, content=dz_poplayout, size_hint=(.90, .40), 
        separator_color=[1, 1, 1, 1], separator_height=1, title_align='center', title_color=[.1, .1, .1, 1], background_color=[1, 1, 1, 1], background='')

    textinput_dz = TextInput(text=dz, cursor_color=[0, 0, 0, 1], font_size=16, readonly=True)
    dz_poplayout.add_widget(textinput_dz)
    # dz_poplayout.add_widget(Button(text='Сохранить', background_color=[.55, .55, .55, 1], background_normal='', size_hint=(1, .25), on_press=popup_save_dz))
    dz_popup.open()


# popup = Popup(title='Test popup', content=Label(text='Hello world'), size_hint=(None, None), size=(400, 400),
            # separator_color=[1, 1, 1, 1], separator_height=1, title_align='center', title_color=[1, 1, 1, 1], background_color=[1, 0, 1, 1])

class DayInfo(BoxLayout):
    def __init__(self, **kwargs):
        super(DayInfo, self).__init__(**kwargs)

        with self.canvas.before:
            Color(.55, .55, .55, 1)
            # print(self.pos, self.size)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):        
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class DayInfo1(BoxLayout):
    def __init__(self, **kwargs):
        super(DayInfo1, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1, 1, 1, 1)
            # print(self.pos, self.size)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):        
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        global nede_text

        # print(nede_text)
        # nede_text = 2
        # print(nede_text)
        gl = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=[50, 20])
        gl.bind(minimum_height=gl.setter('height'))


        def testtt(self, instance):
            print('AUF!')

        def getd(day):

            print(day)
            count = len(day)


            if count == 0:
                day = [['', '', '', 'day']]
                holiday = True
            for i in range(count):
                if day[i][2] != None:
                    holiday = False
                    break
                else:
                    holiday = True


            if holiday:
                bl = GridLayout(cols=1, size_hint_y=None, height=30)
                bl.clearcolor = (1, 1, 1, 1)
            else:
                bl = GridLayout(cols=1, size_hint_y=None, height=60*count+30, spacing=1)

            if holiday:
                di = DayInfo()
                bl.add_widget(di)
                txt = Label(text='[ref=]'+str(day[0][1])+' '+str(day[0][3])+'[/ref]', markup=True, on_ref_press=testtt)
                # txt.on_ref_press(testtt)
                di.add_widget(txt)

            else:
                di = DayInfo(size_hint=[1, 1/(count*2)])
                bl.add_widget(di)
                di.add_widget(Label(text=str(day[0][1]+' '+str(day[0][3]))))    

            if not holiday:
                print(holiday)
                bl2 = BoxLayout(orientation='vertical', spacing=1)
                for i in range(count):
                    # bl2.add_widget(Button(text=str(i+1)))
                # bl2.add_widget(Button(text='b'))
                    bl3 = BoxLayout()
                    di3 = DayInfo1(orientation='vertical')
                    dii = DayInfo(size_hint=[.15, 1])
                    bl3.add_widget(dii)
                    # bl3.add_widget(Button(text=str(day[i][0]), size_hint=[.15, 1]))
                    dii.add_widget(Label(text=str(day[i][0])))
                    bl3.add_widget(di3)

                    lbl = Label(text=str(day[i][2]), color=[0, 0, 0, 1], halign='left', font_size=18)
                    lbl.bind(size=lbl.setter('text_size'))
                    sub_name = BoxLayout(padding=(10, 0, 5, 0))
                    sub_name.add_widget(lbl)
                    di3.add_widget(sub_name)

                    sub_buts = BoxLayout(size_hint=[.26, 1])
                    # sub_buts.add_widget(Button(text='[ref='+str(nede_text)+'-'+str(day[i][6])+'-'+day[i][3]+'-'+str(day[i][0])+']+[/ref]', markup=True, bold=True, font_size=30, color=[.8, .8, .8, 1], background_color=[1, 1, 1, 1], background_normal='', background_down='', on_ref_press=create_popup))
                    sub_buts.add_widget(Button(text = '[ref=&week&'+str(nede_text)+'&/week&id&'+str(day[i][6])+'&/id&date&'+day[i][3]+'&/date&num&'+str(day[i][0])+'&/num&sub&'+str(day[i][2])+'&/sub]+[/ref]', markup=True, bold=True, font_size=30, color=[.8, .8, .8, 1], background_color=[1, 1, 1, 1], background_normal='', background_down='', on_ref_press=create_popup))
                    sub_buts.add_widget(Button(text='=', bold=True, font_size=30, color=[.8, .8, .8, 1], background_color=[1, 1, 1, 1], background_normal='', background_down=''))
                    sub_name.add_widget(sub_buts)

                    dz_name = BoxLayout(padding=(10, 0))
                    if day[i][4]:
                        # print(day[i][4])
                        lbldz = Label(text='[ref=&week&'+str(nede_text)+'&/week&id&'+str(day[i][6])+'&/id&date&'+day[i][3]+'&/date&num&'+str(day[i][0])+'&/num&sub&'+str(day[i][2])+'&/sub&dz&'+day[i][4]+'&/dz]'+day[i][4]+'[/ref]', shorten=True, markup=True, on_ref_press=dz_info_popup,
                            shorten_from='right', font_size=14, max_lines=2, color=[.3, .3, .3, 1], halign='left', valign='center')
                        lbldz.bind(size=lbldz.setter('text_size'))
                        
                        dz_name.add_widget(lbldz)

                    di3.add_widget(dz_name)
                    bl2.add_widget(bl3)

                bl.add_widget(bl2)

            gl.add_widget(bl)


        def getweek(week):
            bl = BoxLayout(size_hint_y=None, height=50)
            ned_layout = DayInfo(spacing=1)
            bl.add_widget(ned_layout)
            ned_layout.add_widget(Button(text='<', size_hint=[.3, 1], background_color=[.55, .55, .55, 1], background_normal='', background_down='', on_press=self.get_prev))
            lbl = Label(text='Неделя ' + str(week))
            ned_layout.add_widget(lbl)
            ned_layout.add_widget(Button(text='>', size_hint=[.3, 1], background_color=[.55, .55, .55, 1], background_normal='', background_down='', on_press=self.get_next))
            gl.add_widget(bl)


        week = get_week_number()
        nede_text = int(week)
        print(nede_text)
        self.lbln = Label(text=str(week))
        print(week)

        days = getting(week)
        print(days)
        getweek(week)
        for day in days:
            getd(day)
        getweek(week)


        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(gl)
        self.add_widget(root)

    def get_prev(self, instance):
        global nede_text
        nede_text = int(self.lbln.text)-1
        self.manager.add_widget(SecondScreen(name='second'))
        self.manager.current = 'second'
        # self.pars_prev(self.lbln.text)
        # if nede_text != '':
        

    def get_next(self, instance):
        global nede_text
        nede_text = int(self.lbln.text)+1
        print(self.lbln.text)
        self.manager.add_widget(SecondScreen(name='second'))
        self.manager.current = 'second'
        # self.pars_next(self.lbln.text)
        # print(self.week)


    # def pars_next(self, text):
    #     text=str(int(text)+1)
    #     text1='Неделя '+text
    #     sm.get_screen('second').lbln.text=text1
    # def pars_prev(self, text):
    #     text=str(int(text)-1)
    #     text1='Неделя '+text
    #     sm.get_screen('second').lbln.text=text1

   


class SecondScreen(Screen):
    # ned_count = nede_text + 1
    # lbln = Label(text='Неделя '+str(nede_text))
    global ned_text
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        # global nede_text
        print('nt', nede_text)

        # lbln = self.lbln

        ned_count = nede_text + 1
        # print('N_C', ned_count)
        lbln = Label(text='Неделя '+str(nede_text))
        self.lbln = lbln

        print('NEDE_TEXT:' + str(nede_text))
        gl = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=[50, 20])
        gl.bind(minimum_height=gl.setter('height'))


        def testtt(self, instance):
            print('AUF!')

        def getd(day):

            print(day)
            count = len(day)


            if count == 0:
                day = [['', '', '', 'day']]
                holiday = True
            for i in range(count):
                if day[i][2] != None:
                    holiday = False
                    break
                else:
                    holiday = True


            if holiday:
                bl = GridLayout(cols=1, size_hint_y=None, height=30)
                bl.clearcolor = (1, 1, 1, 1)
            else:
                bl = GridLayout(cols=1, size_hint_y=None, height=60*count+30, spacing=1)

            if holiday:
                di = DayInfo()
                bl.add_widget(di)
                txt = Label(text='[ref=1]'+str(day[0][1])+' '+str(day[0][3])+'[/ref]', markup=True, on_ref_press=testtt)
                # txt.on_ref_press(testtt)
                di.add_widget(txt)

            else:
                di = DayInfo(size_hint=[1, 1/(count*2)])
                bl.add_widget(di)
                di.add_widget(Label(text=str(day[0][1]+' '+str(day[0][3]))))    

            if not holiday:
                print(holiday)
                bl2 = BoxLayout(orientation='vertical', spacing=1)
                for i in range(count):
                    # bl2.add_widget(Button(text=str(i+1)))
                # bl2.add_widget(Button(text='b'))
                    bl3 = BoxLayout()
                    di3 = DayInfo1(orientation='vertical')
                    dii = DayInfo(size_hint=[.15, 1])
                    bl3.add_widget(dii)
                    # bl3.add_widget(Button(text=str(day[i][0]), size_hint=[.15, 1]))
                    dii.add_widget(Label(text=str(day[i][0])))
                    bl3.add_widget(di3)

                    lbl = Label(text=str(day[i][2]), color=[0, 0, 0, 1], halign='left', font_size=18)
                    lbl.bind(size=lbl.setter('text_size'))
                    sub_name = BoxLayout(padding=(10, 0, 5, 0))
                    sub_name.add_widget(lbl)
                    di3.add_widget(sub_name)

                    sub_buts = BoxLayout(size_hint=[.26, 1])
                    sub_buts.add_widget(Button(text = '[ref=&week&'+str(nede_text)+'&/week&id&'+str(day[i][6])+'&/id&date&'+day[i][3]+'&/date&num&'+str(day[i][0])+'&/num&sub&'+str(day[i][2])+'&/sub]+[/ref]', markup=True, bold=True, font_size=30, color=[.8, .8, .8, 1], background_color=[1, 1, 1, 1], background_normal='', background_down='', on_ref_press=create_popup))
                    sub_buts.add_widget(Button(text='=', bold=True, font_size=30, color=[.8, .8, .8, 1], background_color=[1, 1, 1, 1], background_normal='', background_down=''))
                    sub_name.add_widget(sub_buts)

                    dz_name = BoxLayout(padding=(10, 0))
                    if day[i][4]:
                        # print(day[i][4])
                        lbldz = Label(text='[ref=&week&'+str(nede_text)+'&/week&id&'+str(day[i][6])+'&/id&date&'+day[i][3]+'&/date&num&'+str(day[i][0])+'&/num&sub&'+str(day[i][2])+'&/sub&dz&'+day[i][4]+'&/dz]'+day[i][4]+'[/ref]', shorten=True, markup=True, on_ref_press=dz_info_popup,
                            shorten_from='right', font_size=14, max_lines=2, color=[.3, .3, .3, 1], halign='left', valign='center')
                        lbldz.bind(size=lbldz.setter('text_size'))
                        
                        dz_name.add_widget(lbldz)

                    di3.add_widget(dz_name)
                    bl2.add_widget(bl3)

                bl.add_widget(bl2)

            gl.add_widget(bl)


        def getweek(lbln):
            bl = BoxLayout(size_hint_y=None, height=50)
            ned_layout = DayInfo(spacing=1)
            bl.add_widget(ned_layout)
            ned_layout.add_widget(Button(text='<', size_hint=[.3, 1], background_color=[.55, .55, .55, 1], background_normal='', background_down='', on_press=self.get_prev))
            ned_layout.add_widget(Label(text=lbln.text))
            
            print(type(lbln), 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            # lbln = Label()
            # ned_layout.add_widget(lbln)
            ned_layout.add_widget(Button(text='>', size_hint=[.3, 1], background_color=[.55, .55, .55, 1], background_normal='', background_down='', on_press=self.get_next))
            gl.add_widget(bl)

            # bl = BoxLayout(size_hint_y=None, height=50)
            # ned_layout = DayInfo(spacing=1)
            # bl.add_widget(ned_layout)
            # ned_layout.add_widget(Button(text='<', size_hint=[.3, 1], background_color=[.55, .55, .55, 1], background_normal='', background_down='', on_press=self.get_prev))
            # lbl = Label(text='Неделя ' + str(week))
            # ned_layout.add_widget(lbl)
            # ned_layout.add_widget(Button(text='>', size_hint=[.3, 1], background_color=[.55, .55, .55, 1], background_normal='', background_down='', on_press=self.get_next))
            # gl.add_widget(bl)


        # week = get_week_number()
        # print(week)

        days = getting(self.lbln.text[7:])
        print(self.lbln.text)
        print(days)
        getweek(lbln)
        for day in days:
            getd(day)
        # getweek(lbln)


        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(gl)
        self.add_widget(root)



    def get_prev(self, instance):
        global nede_text
        nede_text = int(self.lbln.text[7:])-1
        # print(random())
        # print(nede_text, 'NEDETEXT ETO')

        self.manager.add_widget(SecondScreen(name='second-'+str(nede_text)))
        self.manager.current = 'second-'+str(nede_text)

    def get_next(self, instance):
        global nede_text
        nede_text = int(self.lbln.text[7:])+1
        # print(random())
        # print(nede_text, 'NEDETEXT ETO')

        self.manager.add_widget(SecondScreen(name='second'+str(nede_text)))
        self.manager.current = 'second'+str(nede_text)
        # print(self.week)


    # def pars_next(self, text):
    #     text=str(int(text)+1)
    #     text1='Неделя '+text
    #     sm.get_screen('second1').lbln.text=text1
    # def pars_prev(self, text):
    #     text=str(int(text)-1)
    #     text1='Неделя '+text
    #     sm.get_screen('second').lbln.text=text1


    # pass

class TScreen(SecondScreen):
    pass



# nede_text = 1
sm = ScreenManager()
sscr = StartScreen(name='start')
sm.add_widget(sscr)
# sm.add_widget(SecondScreen(name='second'))
# sm.get_screen('second').lbln.text = '1'


class TestApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()

