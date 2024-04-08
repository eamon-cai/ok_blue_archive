from scene.MainScene import MainScene

from ok.logging.Logger import get_logger
from ok.task.FindFeatureTask import FindFeatureTask

logger = get_logger(__name__)


class BaseBaTask(FindFeatureTask):

    def go_back(self):
        self.send_key("KEYCODE_BACK")
        self.sleep(1)

    def go_home(self):
        logger.info("go home")
        return self.wait_scene(MainScene,
                               time_out=20,
                               pre_action=lambda: (self.sleep(1), self.send_key("KEYCODE_BACK"), self.sleep(1)))
