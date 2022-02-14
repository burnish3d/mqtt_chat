import argparse
import shutil
import paho.mqtt.client as mqtt # type: ignore
import paho.mqtt.subscribe as subscribe # type: ignore


def on_message(client, userdata, message):
  incoming = str(message.payload.decode("utf-8"))
  lines = [incoming[i*max_width:(i+1)*max_width] for i in range((len(incoming) // max_width) + 1)]
  for line in lines:
    print("\033[s\033[1S\033[1A\033[1L\033[999D" + line + "\033[u", end="", flush=True)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Start a command line chat room over MQTT")
  parser.add_argument('--display-name', '-d', required=True, help="Chatroom display name" )
  parser.add_argument('--user-name', '-u', help="Username for authentication, if required")
  parser.add_argument('--password', '-p', help="Password for authentication, if required")
  parser.add_argument('--broker-address', '-b', required=True, help="Address of the MQTT broker")
  parser.add_argument('--topic', '-t', required=True, help="Topic to subscribe to, looks like /mygroup/ourchat. For more information look up MQTT topics")
  parser.add_argument('--obfuscate', '-o', help="Obfuscate text so that any other subscribers to the topic not in the know only see garbled text. Note this is not encryption, it is the cryptographic version of Dracula disguising himself as Alucard")
  parser.add_argument('--max-width', '-m', help='If set to a number less than the terminal width, will use that number as the terminal width')
  args = parser.parse_args()

  max_width = min(shutil.get_terminal_size()[0] - 1, args.max_width)
  

  client = mqtt.Client() #create new instance
  client.will_set(args.topic, payload= f"{args.display_name} has lost the connection")
  client.on_message=on_message 
  client.connect(args.broker_address) 
  client.loop_start()
  client.subscribe(args.topic)

  print("\033[999B", end="") #pushes cursor to the bottom of the window
  try:
    while True:
      message = str(input(">> "))
      message_height = len(message) // max_width + 1 #number of times to do next line
      print("\033[1T\033[K" * message_height, end="", flush=True) #ANSI escape sequence to delete previous line
      client.publish(args.topic, f"{args.display_name}: {message}")

  except KeyboardInterrupt:
    client.loop_stop()
    print("")
