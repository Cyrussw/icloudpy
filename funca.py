from pyicloud import PyiCloudService
from config import *

import folium
import os


def start():
    os.system("cls")


# iCloud hesabınıza oturum açın
api = PyiCloudService(username, password)


def viewDevices():
    devices = api.devices

    if devices:
        print("Cihazlarınız:")
        for device in devices:
            print("- " + device["deviceDisplayName"])
    else:
        print("Cihaz bulunamadı.")


def get_device_location():
    devices = api.devices
    print("Lütfen konumunu bulmak istediğiniz cihazı seçiniz.")
    viewDevices()
    deviceNo = int(input("Cihaz No: "))

    if not deviceNo:
        print("Geçersiz cihaz numarası.")
        return

    device_index = deviceNo - 1

    if devices:
        selected_device = devices[device_index]

        # Cihazın konumunu alın
        location = selected_device.location()

        if location:
            print("Cihazın Son Konumu:")
            print("Enlem: " + str(location["latitude"]))
            print("Boylam: " + str(location["longitude"]))
            show_location(str(location["latitude"]),
                          str(location["longitude"]))

            print("Ses çalmamı istermisiniz efendim?")
            x = input("Evet/Hayır: ")

            if x == "Evet":
                if selected_device:
                    selected_device.play_sound()
                else:
                    print("Başarısız.")

                print("Ses çalma komutu gönderildi.")
                sendMessage = api.devices.sendMessage("Merhaba!")
            elif x == "Hayır":
                print("Peki iyi günler dilerim efendim.")

        else:
            print("Cihazın konumu bulunamadı.")
    else:
        print("Cihaz bulunamadı.")


def show_location(latitude, longitude):
    location_map = folium.Map(location=[latitude, longitude], zoom_start=13)
    folium.Marker([latitude, longitude], icon=folium.Icon(
        color='red')).add_to(location_map)
    location_map.save('map.html')


def playSound():
    devices = api.devices
    print("Lütfen ses çalmak istediğiniz cihazı seçiniz.")
    viewDevices()
    deviceNo = int(input("Cihaz No: "))

    if not deviceNo:
        print("Geçersiz cihaz numarası.")
        return

    device_index = deviceNo - 1

    if devices:
        selected_device = devices[device_index]

        # Cihazda ses çal
        selected_device.play_sound()
        print("Ses çalma komutu gönderildi.")
    else:
        print("Cihaz bulunamadı.")


def get_photo_albums():
    photo_service = api.photos

    if photo_service:
        albums = photo_service.albums

        if albums:
            print("Albümler:")
            for album_name, album in albums.items():
                print("- " + album_name)

                # Albümdeki fotoğrafları listele
                photos = album.photos
                if photos:
                    print("Fotoğraflar:")
                    for photo in photos:
                        photo_name = photo.filename
                        print("-- " + photo_name)
                else:
                    print("Bu albümde fotoğraf bulunmuyor.")
        else:
            print("Albüm bulunamadı.")
    else:
        print("Fotoğraf servisi bulunamadı.")

def get_contacts():
    contacts_service = api.contacts

    if contacts_service:
        contacts = contacts_service.all()

        if contacts:
            print("Kişiler:")
            for contact in api.contacts.all():
                first_name = contact.get('firstName')
                phones = contact.get('phones')

                if first_name:
                    print("İsim: " + first_name)
                else:
                    print("İsim bilgisi bulunamadı.")

                if phones:
                    for phone in phones:
                        phone_number = phone.get('field')
                        if phone_number:
                            print("Telefon: " + phone_number)
                        else:
                            print("Telefon numarası bulunamadı.")
                        print("---------------------")
                else:
                    print("Kişi için telefon numarası bulunamadı.")
        else:
            print("Kişiler bulunamadı.")
    else:
        print("Kişiler servisi bulunamadı.")