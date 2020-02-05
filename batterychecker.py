import threading
import time
import psutil
import rumps
import pync

def battery():
    return psutil.sensors_battery().percent


class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("App")
        battery_per = battery()
        self.notific(battery_per,50)
        self.roop_time = 60
        self.battery_per_cache = None
        self.notification_status = 0
        battery_check_thread = threading.Thread(target=self.battery_check)
        battery_check_thread.start()



    @rumps.clicked("通知を停止")
    def onoff(self, sender):
        sender.state = not sender.state
        self.notification_status = sender.state
        print(self.notification_status)

    @rumps.clicked("設定")
    def prefs(self, _):
        rumps.alert("まだでけてへん。")


    @rumps.clicked("テスト通知")
    def sayhi(self, _):
        # self.notify("てすと。","icon/100%.png")
        # rumps.notification("バッテリーチェッカー",battery()+"%やで","")
        # os.system("""osascript -e 'display notification "てすと。" with title "ばってりーちぇっかー。"'""")
        pync.notify("てすと通知。",title="ばってりーちぇっかー。", appIcon="icon.icns")
        # self.notific(10000000)

    def notific(self,parsent,icon):
        # rumps.notification("バッテリーチェッカー", str(parsent)+"%やで","",icon="icon/{}%.png".format(str(parsent)))
        pync.notify(str(parsent)+"%やで",title="ばってりーちぇっかー。", appIcon="icon/{}%.png".format(str(icon)))

        print("notific",str(parsent)+"%やで")
        self.icon = "icon/{}%.png".format(str(parsent))

    # def notify(self, message,icon):
    #     t = '-title {!r}'.format("ばってりーちぇっかー。")
    #     s = '-subtitle {!r}'.format("")
    #     m = '-message {!r}'.format(message)
    #     i = '-appIcon {!r}'.format(icon)
    #     os.system('terminal-notifier {}'.format(' '.join([m, t, s, i])))


    def battery_check(self):
        while True:
            battery_per = battery()
            if battery_per % 10 == 0:
                if not (self.battery_per_cache == battery_per):
                    if not (self.notification_status == 1):
                        self.notific(battery_per,battery_per)
                        self.battery_per_cache = battery_per
                        print("BATTERY!",battery_per)

            time.sleep(self.roop_time)


if __name__ == "__main__":
    AwesomeStatusBarApp().run()