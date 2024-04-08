from ok.util.path import get_path
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
    'gui_icon': 'icon.png',  # Optional
    'gui_title': 'Blue Archive Helper',  # Optional, default: False
    'capture': 'adb',  # adb/windows, see #ok.capture
    'capture_window_title': 'Mumu Player 12',  # required  when using windows capture
    'interaction': 'adb',  # adb/windows, see #ok.interaction
    'adb_host': '127.0.0.1',  # required  when using adb capture if not connected, debug host
    'adb_port': 16385,  # required  when using adb capture if not connected, debug port
    'coco_feature_folder': get_path(__file__, 'assets/coco_feature'),  # required if using feature detection
    'log_file': 'logs/auto_helper.log',  # Optional, auto rotating every day
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
