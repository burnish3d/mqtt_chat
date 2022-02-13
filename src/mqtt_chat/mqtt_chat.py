import time
import sys
import shutil
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe


def get_chat_ip():
  return subscribe.simple("ECE/chatroom/where",hostname="test.mosquitto.org").payload.decode("utf-8")

def on_message(client, userdata, message):
  incoming = str(message.payload.decode("utf-8"))
  chopped = [incoming[i*max_width:(i+1)*max_width] for i in range(len(incoming)//max_width + 1)]
  for piece in chopped:
    print("\033[s\033[1S\033[1A\033[1L\033[999D" + piece + "\033[u", end="", flush=True)

max_width = shutil.get_terminal_size()[0] - 1
broker_address = get_chat_ip()
mqtt_subscribe_t = "ECE/chatroom/chat"
mqtt_publish_t = "ECE/chatroom/chat"
if (len(sys.argv) > 1):
  mqtt_handle = str(sys.argv[1])
else:
  mqtt_handle = str(input("What is your name? "))

print("\033[999B", end="") #pushes cursor to the bottom of the window

client = mqtt.Client(mqtt_handle) #create new instance
client.will_set(mqtt_publish_t, payload= f"{mqtt_handle} GONE")
client.on_message=on_message 
client.connect(broker_address) 
client.loop_start()
client.subscribe(mqtt_subscribe_t)

try:
  while True:
    message = str(input(">> "))
    t = len(message) // max_width + 1 #number of times to do next line
    print("\033[1T\033[K" * t,end="",flush=True) #ANSI escape sequence to delete previous line
    client.publish(mqtt_publish_t,mqtt_handle+": " + message)

except KeyboardInterrupt:
  client.loop_stop()
  print("")
