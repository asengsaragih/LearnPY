import random

from paho.mqtt import client as mqtt_client

broker = 'p9919287.us-east-1.emqx.cloud'
port = 15786
topic = "python/mqtt"

client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'testdatausername'
password = 'testdatapassword'

def connect_mqtt():
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

# tempat program dijalankan
def run():
    # mqtt harus diinisialisasi atau dikoneksikan ke server
    client = connect_mqtt()

    # membuka file txt version
    readVersion = open("version.txt", "r")

    # mengkonversi dalam bentuk string
    msg = f"{readVersion.readline()}"

    # fungsi untuk ngepublish data
    result = client.publish(topic, msg)

    # validasi pengiriman data
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


# initial programs
if __name__ == '__main__':
    run()
