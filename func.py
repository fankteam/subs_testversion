import datetime


from db import dBase
from static import *



def getting(ned):
	a = []
	for i in range(1, 8):
		db = dBase('test9.db')
		b = db.for_one_day_pro(ned, days_for_getting[str(i)])
		a.append(b)
	return a

def get_week_number():
	dn = datetime.date.today()
	# dn = datetime.date(2021, 10, 1)

	db = dBase('test9.db')
	first_date, first_week = db.date_first()[0]
	first_date = datetime.datetime.strptime(first_date, '%d.%m.%y').date()

	last_date, last_week = db.date_last()[0]
	last_date = datetime.datetime.strptime(last_date, '%d.%m.%y').date()

	if (dn - first_date).days < 0:
		ned = first_week
	elif (dn - last_date).days > 0:
		ned = last_week
	else:
		ned = db.get_week_for_date(dn)[0][0]
	return ned





def create_all():
	db = dBase('test9.db')
	nedelya = 1
	d = datetime.date(2021, 9, 1)
	while d != datetime.date(2021, 11, 1):
		data = d.strftime('%d.%m.%y')
		day_n = d.strftime('%w')
		if day_n != '0' and day_n != '6':
			rasp_d = sss[day_n]
			for i in range(len(rasp_d)):
				db.create_lesson(nedelya, i + 1, data, days[day_n], rasp_d[i])
			d = d + datetime.timedelta(1)
		elif day_n == '6':
			d = d + datetime.timedelta(1)
		else:
			d = d + datetime.timedelta(1)
			nedelya += 1


def create_all_full():
	db = dBase('test9.db')
	nedelya = 1
	d = datetime.date(2021, 9, 1)
	while d != datetime.date(2021, 11, 1):
		data = d.strftime('%d.%m.%y')
		day_n = d.strftime('%w')
		if day_n != '0' and day_n != '6':
			rasp_d = sss[day_n]
			for i in range(len(rasp_d)):
				db.create_lesson(nedelya, i + 1, data, days[day_n], rasp_d[i])
			d = d + datetime.timedelta(1)
		elif day_n == '6':
			db.create_lesson(nedelya, 1, data, days[day_n], None)
			d = d + datetime.timedelta(1)
		else:
			db.create_lesson(nedelya, 1, data, days[day_n], None)
			d = d + datetime.timedelta(1)
			nedelya += 1







def delete_all():
	db = dBase('test9.db')
	db.delete_all()



def check_dz(id):
	db = dBase('test9.db')
	dzcheck = db.check_dz(id)[0][0]
	return dzcheck


def add_dz(id, text):
	print('!!!!!', id)
	print('!!!!!', text)
	db = dBase('test9.db')
	db.add_dz1(text)
	dzid = db.add_dz2()[0][0]
	print('!!!!!', dzid)
	db.add_dz3(id, dzid)


def next_dz(id):
	db = dBase('test9.db')
	dzperem = db.next_dz1(id)
	sub = dzperem[0][0]
	dz = dzperem[0][1]
	# print(dzperem, sub, dz)
	newid = db.next_dz2(sub, id)[0][0]
	db.next_dz3(dz, newid)
	db.next_dz4(id)


def delete_dz(id):
	db = dBase('test9.db')
	db.del_dz(id)


def edit_dz(id, text):
	db = dBase('test9.db')
	dzid = db.next_dz1(id)[0][1]
	db.edit_dz(dzid, text)


def get_dz_by_id(id):
	db = dBase('test9.db')
	dz = db.get_dz_by_id(id)
	if dz == []:
		dz_ = None
	else:
		dz_ = dz[0][0]
	return dz_


# text='[ref='+str(nede_text)+'-'+str(day[i][6])+'-'+day[i][3]+'-'+str(day[i][0])+']+[/ref]'
# text = '[ref=&week&'+str(nede_text)+'&/week&id&'+str(day[i][6])+'&/id&date&'+day[i][3]+'&/date&num&'+str(day[i][0])+'&/num&sub&'+str(day[i][2])+'&/sub]+[/ref]'

# a = '[ref=&week&7&/week&id&1&/id&date&06.09.21&/date&num&4&/num&sub&matesha&/sub]'
# ned = a[a.rfind('&week')+6:(a.find('&/week'))]
# id = a[a.rfind('&id')+4:(a.find('&/id'))]
# date = a[a.rfind('&date')+6:(a.find('&/date'))]
# num = a[a.rfind('&num')+5:(a.find('&/num'))]
# sub = a[a.rfind('&sub')+5:(a.find('&/sub'))]

# print(sub)


# def create_popup(self, instance):
#     global t
#     global popup
#     global textinput_dz

#     poplayout = BoxLayout(orientation='vertical', padding=10, spacing=10)
#     print(self.text)
#     t = self.text

#     day_id2 = t[5:].find('-')
#     day_id1 = t[day_id2+5+1:].find('-')
#     day_id0 = t[day_id2+6:day_id1+day_id2+6]

#     dz = get_dz_by_id(day_id0)
#     if dz:
#         textdz = dz
#     else:
#         textdz = ''

#     popup = Popup(title='Редактирование д/з', content=poplayout, size_hint=(.95, .70), 
#         separator_color=[1, 1, 1, 1], separator_height=1, title_align='center', title_color=[.1, .1, .1, 1], background_color=[1, 1, 1, 1], background='')

#     # popup.add_widget(poplayout)
#     textinput_dz = TextInput(text=textdz, cursor_color=[0, 0, 0, 1], font_size=16, readonly=False)
#     poplayout.add_widget(textinput_dz)
#     poplayout.add_widget(Button(text='Сохранить', background_color=[.55, .55, .55, 1], background_normal='', size_hint=(1, .25), on_press=popup_save_dz))
#     popup.open()

# # [ref=1-463-01.09.21-3]+[/ref]
# def popup_save_dz(instance):
#     tt = t[5:].find('-')
#     t_ned = t[5:tt+5]
#     t_id_pre = t[tt+5+1:].find('-')
#     t_id = t[tt+6:t_id_pre+tt+6]
#     # print(t_id_pre, t[tt+5+1:], t_id)
#     # print(tt)
#     # print(textinput_dz.text)
#     # add_dz(int(t_id), textinput_dz.text)

#     chdz = check_dz(t_id)
#     # print(chdz)
#     if chdz:
#         edit_dz(int(t_id), textinput_dz.text)
#     else:
#         add_dz(int(t_id), textinput_dz.text)

#     popup.dismiss()
#     global nede_text
#     nede_text = int(t_ned)

#     random_text = str(random())

#     sm.add_widget(SecondScreen(name='second-'+str(nede_text)+random_text))
#     sm.current = 'second-'+str(nede_text)+random_text
