import threading

import adbutils

from autoui.capture.HwndWindow import HwndWindow
from autoui.capture.adb.ADBCaptureMethod import ADBCaptureMethod
from autoui.feature.FeatureSet import FeatureSet
from autoui.gui.App import App
from autoui.interaction.ADBInteraction import ADBBaseInteraction
from autoui.task.TaskExecutor import TaskExecutor
from scene.MainScene import MainScene
from scene.NotificationScence import NotificationScene
from scene.OkDialogScene import OkDialogScene
from scene.QuestScene import QuestScene
from scene.StartScence import StartScene
from task.AutoLoginTask import AutoLoginTask
from task.ClickOkTask import ClickOkTask
from task.CloseNotificationTask import CloseNotificationTask
from task.DailyCafeTask import DailyCafeTask
from task.DailyScheduleTask import DailyScheduleTask

exit_event = threading.Event()
# Example usage
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
adb.connect("127.0.0.1:16384")
for info in adb.list():
    print(info.serial, info.state)
    # <serial> <device|offline>

android_package = "com.YostarJP.BlueArchive"
android_activity = "com.yostarjp.bluearchive.MxUnityPlayerActivity"

device = adb.device()
device.shell(f"am start {android_package}/{android_activity}")

adb_capture = ADBCaptureMethod(device)
hwnd_window = HwndWindow(title="Mumu Player 12", frame_width=adb_capture.width, frame_height=adb_capture.height,
                         exit_event=exit_event)

# windows_capture = WindowsGraphicsCaptureMethod(hwnd_window)
# capture = windows_capture
capture = adb_capture

# Setup UI overlay for detection box display, optional
# overlay = TkOverlay(hwnd_window, exit_event)
interaction = ADBBaseInteraction(device, capture, adb_capture.width, adb_capture.height)

coco_folder = 'assets/coco_feature'
feature_set = FeatureSet(coco_folder, adb_capture.width, adb_capture.height,
                         default_horizontal_variance=0.1, default_vertical_variance=0.1, default_threshold=0.8)

task_executor = TaskExecutor(capture, interaction=interaction, exit_event=exit_event, tasks=[
    AutoLoginTask(feature_set),
    CloseNotificationTask(feature_set),
    DailyCafeTask(feature_set),
    DailyScheduleTask(feature_set),
    ClickOkTask(feature_set),
], scenes=[
    OkDialogScene(feature_set),
    StartScene(feature_set),
    NotificationScene(feature_set),
    QuestScene(feature_set),
    MainScene(feature_set),
])

app = App(exit_event)
app.start()
