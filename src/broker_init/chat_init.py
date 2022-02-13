import sys
import shutil
import paho.mqtt.publish as publish 


this_ip = str(sys.argv[1])
with open("te","a") as f:
  f.write(this_ip)

def on_message_print(client, userdata, message):
  print("%s %s" % (message.topic, message.payload))
max_width = shutil.get_terminal_size()[0] - 1
broker_address="test.mosquitto.org"
broker_address = "5.196.95.208"
messages = [ {'topic':"ECE/chatroom/up", 'payload':1, 'qos':0, 'retain':False}
           , {'topic':"ECE/chatroom/where", 'payload':this_ip, 'qos':0, 'retain':True} ]

publish.multiple(messages, hostname = broker_address)
