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

config = {
    'debug': True,  # Optional, default: False
    'use_gui': True,
    'capture': 'adb',  # adb/windows, see #autoui.capture
    'interaction': 'adb',  # adb/windows, see #autoui.interaction
    'window_title': 'Mumu Player 12"',  # required  when using windows capture
    'adb_host': '127.0.0.1',  # required  when using adb capture if not connected, debug host
    'adb_port': 16384,  # required  when using adb capture if not connected, debug port
    'coco_feature_folder': 'assets/coco_feature',  # required if using feature detection
    'log_file': 'logs/auto_ui.log',  # Optional, auto rotating every day
    'tasks': [  # tasks to execute
        AutoLoginTask(),
        CloseNotificationTask(),
        DailyScheduleTask(),
        DailyCafeTask(),
        ClickOkTask(),
    ], 'scenes': [  # scenes to detect
        OkDialogScene(),
        StartScene(),
        NotificationScene(),
        QuestScene(),
        MainScene(),
    ]
}
