#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests



# Create your views here.


VERIFY_TOKEN = 'emojify'





a = [["😄", "Smiling Face with Open Mouth and Smiling Eyes"], ["😃", "Smiling Face with Open Mouth"], ["😀", "Grinning Face"], ["😊", "Smiling Face with Smiling Eyes"], ["☺️", "White Smiling Face"], ["😉", "Winking Face"], ["😍", "Smiling Face with Heart-Shaped Eyes"], ["😘", "Face Throwing a Kiss"], ["😚", "Kissing Face with Closed Eyes"], ["😗", "Kissing Face"], ["😙", "Kissing Face with Smiling Eyes"], ["😜", "Face with Stuck-Out Tongue and Winking Eye"], ["😝", "Face with Stuck-Out Tongue and Tightly-Closed Eyes"], ["😛", "Face with Stuck-Out Tongue"], ["😳", "Flushed Face"], ["😁", "Grinning Face with Smiling Eyes"], ["😔", "Pensive Face"], ["😌", "Relieved Face"], ["😒", "Unamused Face"], ["😞", "Disappointed Face"], ["😣", "Persevering Face"], ["😢", "Crying Face"], ["😂", "Face with Tears of Joy"], ["😭", "Loudly Crying Face"], ["😪", "Sleepy Face"], ["😥", "Disappointed but Relieved Face"], ["😰", "Face with Open Mouth and Cold Sweat"], ["😅", "Smiling Face with Open Mouth and Cold Sweat"], ["😓", "Face with Cold Sweat"], ["😩", "Weary Face"], ["😫", "Tired Face"], ["😨", "Fearful Face"], ["😱", "Face Screaming in Fear"], ["😠", "Angry Face"], ["😡", "Pouting Face"], ["😤", "Face with Look of Triumph"], ["😖", "Confounded Face"], ["😆", "Smiling Face with Open Mouth and Tightly-Closed Eyes"], ["😋", "Face Savouring Delicious Food"], ["😷", "Face with Medical Mask"], ["😎", "Smiling Face with Sunglasses"], ["😴", "Sleeping Face"], ["😵", "Dizzy Face"], ["😲", "Astonished Face"], ["🏠", "House Building"], ["🏡", "House with Garden"], ["🏫", "School"], ["🏢", "Office Building"], ["🏣", "Japanese Post Office"], ["🏥", "Hospital"], ["🏦", "Bank"], ["🏪", "Convenience Store"], ["🏩", "Love Hotel"], ["🏨", "Hotel"], ["💒", "Wedding"], ["⛪️", "Church"], ["🏬", "Department Store"], ["🏤", "European Post Office"], ["🌇", "Sunset over Buildings"], ["🌆", "Cityscape at Dusk"], ["🏯", "Japanese Castle"], ["🏰", "European Castle"], ["⛺️", "Tent"], ["🏭", "Factory"], ["🗼", "Tokyo Tower"], ["🗾", "Silhouette of Japan"], ["🗻", "Mount Fuji"], ["🌄", "Sunrise over Mountains"], ["🌅", "Sunrise"], ["🌃", "Night with Stars"], ["🗽", "Statue of Liberty"], ["🌉", "Bridge at Night"], ["🎠", "Carousel Horse"], ["🎡", "Ferris Wheel"], ["⛲️", "Fountain"], ["🎢", "Roller Coaster"], ["🚢", "Ship"], ["⛵️", "Sailboat"], ["🚤", "Speedboat"], ["🚣", "Rowboat"], ["⚓️", "Anchor"], ["🚀", "Rocket"], ["✈️", "Airplane"], ["💺", "Seat"], ["🚁", "Helicopter"], ["🚂", "Steam Locomotive"], ["🚊", "Tram"], ["🚉", "Station"], ["🐶", "Dog Face"], ["🐺", "Wolf Face"], ["🐱", "Cat Face"], ["🐭", "Mouse Face"], ["🐹", "Hamster Face"], ["🐰", "Rabbit Face"], ["🐸", "Frog Face"], ["🐯", "Tiger Face"], ["🐨", "Koala"], ["🐻", "Bear Face"], ["🐷", "Pig Face"], ["🐽", "Pig Nose"], ["🐮", "Cow Face"], ["🐗", "Boar"], ["🐵", "Monkey Face"], ["🐒", "Monkey"], ["🐴", "Horse Face"], ["🐑", "Sheep"], ["🐘", "Elephant"], ["🐼", "Panda Face"], ["🐧", "Penguin"], ["🐦", "Bird"], ["🐤", "Baby Chick"], ["🐥", "Front-Facing Baby Chick"], ["🐣", "Hatching Chick"], ["🐔", "Chicken"], ["🐍", "Snake"], ["🐢", "Turtle"], ["🐛", "Bug"], ["🐝", "Honeybee"], ["🐜", "Ant"], ["🐞", "Lady Beetle"], ["🐌", "Snail"], ["🐙", "Octopus"], ["🐚", "Spiral Shell"], ["🐠", "Tropical Fish"], ["🐟", "Fish"], ["🐬", "Dolphin"], ["🐳", "Spouting Whale"], ["🐋", "Whale"], ["🐄", "Cow"], ["🐏", "Ram"], ["🐀", "Rat"], ["🐃", "Water Buffalo"], ["🎍", "Pine Decoration"], ["💝", "Heart with Ribbon"], ["🎎", "Japanese Dolls"], ["🎒", "School Satchel"], ["🎓", "Graduation Cap"], ["🎏", "Carp Streamer"], ["🎆", "Fireworks"], ["🎇", "Firework Sparkler"], ["🎐", "Wind Chime"], ["🎑", "Moon Viewing Ceremony"], ["🎃", "Jack-o-lantern"], ["👻", "Ghost"], ["🎅", "Father Christmas"], ["🎄", "Christmas Tree"], ["🎁", "Wrapped Present"], ["🎋", "Tanabata Tree"], ["🎉", "Party Popper"], ["🎊", "Confetti Ball"], ["🎈", "Balloon"], ["🎌", "Crossed Flags"], ["🔮", "Crystal Ball"], ["🎥", "Movie Camera"], ["📷", "Camera"], ["📹", "Video Camera"], ["📼", "Videocassette"], ["💿", "Optical Disc"], ["📀", "DVD"], ["💽", "Minidisc"], ["💾", "Floppy Disk"], ["💻", "Personal Computer"], ["📱", "Mobile Phone"], ["☎️", "Black Telephone"], ["📞", "Telephone Receiver"], ["📟", "Pager"], ["📠", "Fax Machine"], ["📡", "Satellite Antenna"], ["📺", "Television"], ["📻", "Radio"], ["🔊", "Speaker with Three Sound Waves"], ["🔉", "Speaker with One Sound Wave"], ["🔈", "Speaker"], ["🔇", "Speaker with Cancellation Stroke"], ["🔔", "Bell"], ["🔕", "Bell with Cancellation Stroke"], ["1⃣", "Keycap 1"], ["2⃣", "Keycap 2"], ["3⃣", "Keycap 3"], ["4⃣", "Keycap 4"], ["5⃣", "Keycap 5"], ["6⃣", "Keycap 6"], ["7⃣", "Keycap 7"], ["8⃣", "Keycap 8"], ["9⃣", "Keycap 9"], ["0⃣", "Keycap 0"], ["🔟", "Keycap Ten"], ["🔢", "Input Symbol for Numbers"], ["#⃣", "Hash Key"], ["🔣", "Input Symbol for Symbols"], ["⬆️", "Upwards Black Arrow"], ["⬇️", "Downwards Black Arrow"], ["⬅️", "Leftwards Black Arrow"], ["➡️", "Black Rightwards Arrow"], ["🔠", "Input Symbol for Latin Capital Letters"], ["🔡", "Input Symbol for Latin Small Letters"], ["🔤", "Input Symbol for Latin Letters"], ["↗️", "North East Arrow"], ["↖️", "North West Arrow"], ["↘️", "South East Arrow"], ["↙️", "South West Arrow"], ["↔️", "Left Right Arrow"], ["↕️", "Up Down Arrow"], ["🔄", "Anticlockwise Downwards and Upwards Open Circle Arrows"], ["◀️", "Black Left-Pointing Triangle"], ["▶️", "Black Right-Pointing Triangle"], ["🔼", "Up-Pointing Small Red Triangle"], ["🔽", "Down-Pointing Small Red Triangle"], ["↩️", "Leftwards Arrow with Hook"], ["↪️", "Rightwards Arrow with Hook"], ["ℹ️", "Information Source"], ["⏪", "Black Left-Pointing Double Triangle"], ["⏩", "Black Right-Pointing Double Triangle"], ["⏫", "Black Up-Pointing Double Triangle"], ["⏬", "Black Down-Pointing Double Triangle"], ["⤵️", "Arrow Pointing Rightwards Then Curving Downwards "], ["⤴️", "Arrow Pointing Rightwards Then Curving Upwards"], ["🆗", "Squared OK"], ["🔀", "Twisted Rightwards Arrows"], ["🔁", "Clockwise Rightwards and Leftwards Open Circle Arrows"], ["🌡", "Thermometer"], ["🌢", "Black Droplet"], ["🌣", "White Sun"], ["🌤", "White Sun with Small Cloud"], ["🌥", "White Sun Behind Cloud"], ["🌦", "White Sun Behind Cloud with Rain"], ["🌧", "Cloud with Rain"], ["🌨", "Cloud with Snow"], ["🌩", "Cloud with Lightning"], ["🌪", "Cloud with Tornado"], ["🌫", "Fog"], ["🌬", "Wind Blowing Face"], ["🌶", "Hot Pepper"], ["🍽", "Fork and Knife with Plate"], ["🎔", "Heart with Tip on The Left"], ["🎕", "Bouquet of Flowers"], ["🎖", "Military Medal"], ["🎗", "Reminder Ribbon"], ["🎘", "Musical Keyboard with Jacks"], ["🎙", "Studio Microphone"], ["🎚", "Level Slider"], ["🎛", "Control Knobs"], ["🎜", "Beamed Ascending Musical Notes"], ["🎝", "Beamed Descending Musical Notes"], ["🎞", "Film Frames"], ["🎟", "Admission Tickets"], ["🏅", "Sports Medal"], ["🏋", "Weight Lifter"], ["🏌", "Golfer"], ["🏍", "Racing Motorcycle"], ["🏎", "Racing Car"], ["🏔", "Snow Capped Mountain"], ["🏕", "Camping"], ["🏖", "Beach with Umbrella"], ["🏗", "Building Construction"], ["🏘", "House Buildings"], ["🏙", "Cityscape"], ["🏚", "Derelict House Building"], ["🏛", "Classical Building"], ["🏜", "Desert"], ["🏝", "Desert Island"], ["🏞", "National Park"], ["🏟", "Stadium"], ["🏱", "White Pennant"], ["☝🏻", "White White Up Pointing Index"], ["☝🏼", "Light Brown White Up Pointing Index"], ["☝🏽", "Olive Toned White Up Pointing Index"], ["☝🏾", "Deeper Brown White Up Pointing Index"], ["☝🏿", "Black White Up Pointing Index"], ["✊🏻", "White Raised Fist"], ["✊🏼", "Light Brown Raised Fist"], ["✊🏽", "Olive Toned Raised Fist"], ["✊🏾", "Deeper Brown Raised Fist"], ["✊🏿", "Black Raised Fist"], ["✋🏻", "White Raised Hand"], ["✋🏼", "Light Brown Raised Hand"], ["✋🏽", "Olive Toned Raised Hand"], ["✋🏾", "Deeper Brown Raised Hand"], ["✋🏿", "Black Raised Hand"], ["✌🏻", "White Victory Hand"], ["✌🏼", "Light Brown Victory Hand"], ["✌🏽", "Olive Toned Victory Hand"], ["✌🏾", "Deeper Brown Victory Hand"], ["✌🏿", "Black Victory Hand"], ["🎅🏻", "White Father Christmas"], ["🎅🏼", "Light Brown Father Christmas"], ["🎅🏽", "Olive Toned Father Christmas"], ["🎅🏾", "Deeper Brown Father Christmas"], ["🎅🏿", "Black Father Christmas"], ["🏃🏻", "White Runner"], ["🏃🏼", "Light Brown Runner"], ["🏃🏽", "Olive Toned Runner"], ["🏃🏾", "Deeper Brown Runner"], ["🏃🏿", "Black Runner"], ["🏄🏻", "White Surfer"], ["🏄🏼", "Light Brown Surfer"], ["🏄🏽", "Olive Toned Surfer"], ["🏄🏾", "Deeper Brown Surfer"], ["🏄🏿", "Black Surfer"], ["🏇🏻", "White Horse Racing"], ["🏇🏼", "Light Brown Horse Racing"], ["🏇🏽", "Olive Toned Horse Racing"], ["🏇🏾", "Deeper Brown Horse Racing"], ["🏇🏿", "Black Horse Racing"], ["🏊🏻", "White Swimmer"], ["🏊🏼", "Light Brown Swimmer"], ["🏊🏽", "Olive Toned Swimmer"], ["🏊🏾", "Deeper Brown Swimmer"]]






class MyChatBotView(generic.View):
	def get(self, request, *args, **kwargs):
		if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Oops invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		incoming_message= json.loads(self.request.body.decode('utf-8'))
		print incoming_message

		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				print message
				try:
					sender_id = message['sender']['id']
					message_text = message['message']['text']
					post_facebook_message(sender_id,message_text) 
				except Exception as e:
					print e
					pass

		return HttpResponse()  

def index(request):
	return HttpResponse('Hello world')