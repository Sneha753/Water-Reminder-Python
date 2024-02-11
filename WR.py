import time
from plyer import notification

while True:
    if __name__ == "__main__":
        notification.notify(title='Drink Water',
                            message="Drink water and stay healthy",
                            app_icon="icon/glass.ico")
        time.sleep(60*60)

