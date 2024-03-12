from scene.StartScence import StartScene
from typing_extensions import override

from autoui.task.FindFeatureTask import FindFeatureTask


class AutoLoginTask(FindFeatureTask):

    @override
    def run_frame(self):
        if self.is_scene(StartScene):
            self.logger.info(f"Start scene click")
            self.click_relative(0.5, 0.5)
            self.sleep(1)
            return True
