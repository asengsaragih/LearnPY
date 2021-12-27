import random

from paho.mqtt import client as mqtt_client

# broker dan port didapakan dari website
broker = 'p9919287.us-east-1.emqx.cloud'
port = 15786 #port wajib pakai version mqtt

# topic ini bebas
topic = "python/mqtt"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

# username dan password didapatkan dari website
username = 'testdatausername'
password = 'testdatapassword'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# global version of subscriber
v = "0"

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global v

        # ngambil version pertama kali
        if v == "0" :
            v = msg.payload.decode()

        if v == msg.payload.decode():
            print("Version : " + v)
        else:
            inputUser = input("Apakah Ingin Memperbarui Version? (y/n) ")
            if inputUser == 'y':
                # Update versi client
                v = msg.payload.decode()
                print("Thanks For Update, Your current version is : " + v)
            elif inputUser == 'n':
                # Tidak mengupdate versi Client
                print("Your version not updated, your version is : " + v)
            else:
                print("Updating Error")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
