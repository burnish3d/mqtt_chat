
import argparse

parser = argparse.ArgumentParser(description="Start a command line chat room over MQTT")

parser.add_argument('--display-name', '-d', required=True, help="Chatroom display name" )

parser.add_argument('--user-name', '-u', help="Username for authentication, if required")

parser.add_argument('--password', '-p', help="Password for authentication, if required")

parser.add_argument('--broker-address', 'b', required=True, help="Address of the MQTT broker")

parser.add_argument('--topic', '-t', required=True, help="Topic to subscribe to, looks like /mygroup/ourchat. For more information look up MQTT topics")

parser.add_argument('--obfuscate', '-o', help="Obfuscate text so that any other subscribers to the topic not in the know only see garbled text. Note this is not encryption, it is the cryptographic version of Dracula disguising himself as Alucard")