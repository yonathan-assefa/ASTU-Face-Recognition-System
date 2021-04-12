import json
import logging
from datetime import date, datetime
from random import randint
from time import sleep

import cv2
import face_recognition as fr
import numpy as np
import requests
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import render
from django.utils import timezone

from facex.models import Student
from users_app.models import *

#import os
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rose.settings')
#import django


#from HTMLLogger import HTMLLogger
#logger=HTMLLogger(name="Test App", html_filename="templates/logs/log.html", console_log=True)







class WSConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()

	
#		for i in range(1000):
#			self.send(json.dumps({'message':randint(1,100)}))
#			sleep(1)


		
		x = Student.objects.all()

		f_encs = []
		known_face_names = []
		id_s=[]
		for i in range(len(x)):
			f_encs.append(fr.face_encodings(fr.load_image_file(x[i].image))[0])
			known_face_names.append(f"Id: {x[i].id_n}")
			id_s.append(x[i].id_n)
		#print(f_encs)
		#yona_code = fr.face_encodings(fr.load_image_file(x[0].image))[0]
		#wende_code = fr.face_encodings(fr.load_image_file(x[1].image))[0]
		
		#sk_code = fr.face_encodings(fr.load_image_file("sk.jpg"))[0]
		#mi_code = fr.face_encodings(fr.load_image_file("mi.jpg"))[0]
		#r_code = fr.face_encodings(fr.load_image_file("r.jpg"))[0]

		#ru_code = fr.face_encodings(fr.load_image_file("ruth.jpg"))[0]


	
		video_capture = cv2.VideoCapture(0)
		#video_capture.set(cv.CAP_PROP_BUFFERSIZE, 1)
		#yona_code = fr.face_encodings(fr.load_image_file("yona.jpg"))[0]

		#sk_code = fr.face_encodings(fr.load_image_file("sk.jpg"))[0]
		#mi_code = fr.face_encodings(fr.load_image_file("mi.jpg"))[0]
		#r_code = fr.face_encodings(fr.load_image_file("r.jpg"))[0]
		#ru_code = fr.face_encodings(fr.load_image_file("ruth.jpg"))[0]


		#known_face_encodings = [list(i) for i in fr.face_encodings(fr.load_image_file(x[i].image))[0]]

		known_face_encodings = [
		]

		for i in f_encs:
			known_face_encodings.append(i)
		#[	yona_code,
			#wende_code,
			#sk_code,
	#		mi_code,
	#		r_code,
	#		ru_code,
		#]


		#known_face_names = [
	#		
	#		"Name: Yonathan Assefa <br> ID: ********* <br> Sex: Male <br> Dep: CSE",
	#		"Name: Wende  \n ID: ********* \n Sex: Male \n Dep: CSE",
	#		"Name: Miraj  \n ID: ********* \n Sex: Male \n Dep: CSE",
	#		"Name: Biruk Alamirew  \n ID: ********* \n Sex: Male \n Dep: CSE",
	#		"Name: Ruth   \n ID: ********* \n Sex: Female \n Dep: CSE",


	#	]
		#logname = str(datetime.today())
		#logging.basicConfig(filename = "logs/"+logname)
		n = []
		for i in range(200):

			#date_time = datetime.now()
			#logname = str(timezone.now().date())
			#log = open("logs/"+logname+".lf", "a")

			ret, frame = video_capture.read()

			rgb_frame = frame[:,:,::-1]

			face_locations = fr.face_locations(rgb_frame)
			face_encodings = fr.face_encodings(rgb_frame, face_locations)



			for (top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
				matches = fr.compare_faces(known_face_encodings, face_encodings)

				name = "Unknown face detected"

				face_distance = fr.face_distance(known_face_encodings, face_encodings)

				best_match_index = np.argmin(face_distance)

				if matches[best_match_index]:
					name = known_face_names[best_match_index]
				font = cv2.FONT_HERSHEY_SIMPLEX
				
				if name != 'Unknown face detected':
					send_id = Student.objects.filter(id_n=id_s[best_match_index])
					#cur_time = date_time.time()
					#log.write(str(cur_time) + '$' + send_id[0].username +'|')
					#log.close()
					self.send(json.dumps({
						'name':send_id[0].user_profile.first_name,
						"id":send_id[0].id_n,
						"Department":send_id[0].department.department,
						"img":send_id[0].user_profile.profile_picture.url,
						}))
					#logger.info(str(send_id[0].id_n))
					cv2.rectangle(frame, (left,top), (right, bottom), (51,51,51), 2)
					cv2.rectangle(frame, (10, 350),(250, 500),(51,51,51),cv2.FILLED)
					sleep(3)
					
					name = name.split('\n')
					p = 0
					for i in name:
						cv2.putText(frame, i.strip(),(15, (370 + p)), font, 0.6, (255,255,255),1,cv2.LINE_AA, False)
						p+= 30
				else:
					self.send(json.dumps({'message':name}))
					sleep(2)
					cv2.rectangle(frame, (left,top), (right, bottom), (0,0,255), 2)
					cv2.rectangle(frame, (10, 400),(250, 470),(0,0,255),cv2.FILLED)
				
					
					cv2.putText(frame, name,(15, (420)), font, 0.6, (255,255,255),1,cv2.LINE_AA, False)



			cv2.imshow('A F', frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		video_capture.release()
		cv2.destroyAllWindows()

